# ################################################################################
# check_site.py
#   Checks all links (local and external) in all files of a generated web site.
# ################################################################################

import os
import re
import requests
import threading

all_local_files = {}
external_links = {}


# This runs in a separate thread (one per external URL)
def is_valid_url(url: str, source_path: str) -> None:
    """Check if an external URL is reachable."""
    broken_source = source_path
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code < 400:
            broken_source = ""
    except requests.RequestException:
            ...
    external_links[url] = broken_source


def check_links_in_html(file_path, file_dir, base_path, threads, stop_on_error: bool):
    """Parse an HTML file and check all links."""
    # Extract all href links from the file
    links: list[str] = []
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # Drop XML comments
        content, _ = re.subn(r"<!--.*?-->", "", content, flags=re.DOTALL)
        # Drop canonical link
        content, _ = re.subn(r"<link\s+rel=\"canonical\"\s+href=\".*?\">\s*", "", content, flags=re.DOTALL)
        # Find hrefs
        refs = re.findall(r'href=(["\'])(.*?)\1', content)
        if refs:
            # Replace URL-encoded characters
            refs = [r[1].replace("%20", " ").replace("%26", "&") for r in refs]
            # Anchors in index.html
            refs = [re.sub(r"^(.*/)#[^/]+$", r"\1index.html", r) for r in refs]
            # Other anchors
            refs = [re.sub(r"^(.*)#[^/]+$", r"\1", r) for r in refs]
            # Links to directory (-> index.html) for local hrefs
            refs = [re.sub(r"^((?!http).*/)$", r"\1index.html", r) for r in refs]
            links.extend(refs)
    broken_links = []

    for href in links:
        href = href.strip()
        if href.startswith("/en"):
            slash2 = href.find("/", href.find("/", 1) + 1)  # Find the third "/"
            href = href[slash2 + 1 :]
            if href == ".":
                continue

        if href.startswith("http"):  # External link
            if (question_mark := href.find("?", 4)) != -1:
                href = href[:question_mark]
            if threads is not None and href not in external_links:
                external_links[href] = ""
                thread = threading.Thread(target=is_valid_url, args=(href, file_path))
                thread.start()
                threads.append(thread)

        elif (
            href.startswith("javascript:") or href.startswith("mailto:") or href.startswith("#")
        ):  # Scrip, mail or internal ref link
            ...

        else:  # Local link
            rel_path = file_dir
            new_href = href
            while new_href.startswith("../"):
                rel_path = rel_path[: rel_path.rfind("/")]
                new_href = new_href[3:]
            target_path = rel_path + "/" + new_href
            if target_path not in all_local_files:
                all_local_files[target_path] = ""
                if not os.path.exists(target_path):
                    broken_links.append((file_path, href, "Missing local file"))
                    if stop_on_error:
                        print(f"Broken link in {file_path}. {href=} {new_href=} {target_path=}")
                        exit(0)

    return broken_links


def check_links(site_directory, filter, external_check: bool, stop_on_error: bool):
    """Scan all HTML files in the given site directory for broken links."""
    all_broken_links = []
    # Precompute a dict of all local files and their directory
    for root, _, files in os.walk(site_directory):
        root = root.replace("\\", "/")
        for file in files:
            if not filter or any(f in root for f in filter):
                all_local_files[root + "/" + file] = root

    # Use multithreading for external link checking
    threads = [] if external_check else None

    file_counter = 0
    progress_bar_length = 40
    number_of_html_files = sum(1 for f in all_local_files if f.endswith(".html"))
    for file_path, root in all_local_files.copy().items():
        if file_path.endswith(".html"):
            percent = (file_counter / number_of_html_files)
            filled_length = int(progress_bar_length * percent)
            bar = '=' * filled_length + '-' * (progress_bar_length - filled_length)
            print(f"\rProgress: |{bar}| {percent * 100:.2f}% ({file_counter}/{number_of_html_files})", end="")
            broken_links = check_links_in_html(file_path, root, site_directory, threads, stop_on_error)
            all_broken_links.extend(broken_links)
            file_counter += 1

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    for url, source in external_links.items():
        if source:
            all_broken_links.append((source, url, "Broken external link"))

    return all_broken_links


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check all links in a static website directory.")
    parser.add_argument(
        "site_directory", nargs="?", default="site", help="Path to the generated site directory (default: site)."
    )
    parser.add_argument(
        "-f",
        "--filter",
        "--filters",
        nargs="+",
        help="List of strings that must appear in the tested path.",
        required=False,
    )
    parser.add_argument(
        "-s", "--stop_on_error", action="store_true", help="If True, stop at the first error (default is False)"
    )
    parser.add_argument("--no-external", action="store_true", help="Skip checking external links.")
    args = parser.parse_args()

    if not os.path.isdir(args.site_directory):
        print(f"Couldn't find generated site directory '{args.site_directory}'.")
        print("Was the site generated (mkdocs build)?")
        exit(1)

    broken_links = check_links(
        args.site_directory, args.filter, external_check=not args.no_external, stop_on_error=args.stop_on_error
    )

    if broken_links:
        print("Broken Links Found:")
        for file, href, reason in broken_links:
            print(f"{reason} in file: {file}, Link: {href}")
    else:
        print("No broken links found!")
