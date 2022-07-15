import os
import re
import logging

SITE_DIR = "site"

def to_unix(p):
    return p.replace("\\","/")
# Assuming that this script is located in <taipy-doc>/tools
tools_dir = os.path.dirname(__file__)
site_path = os.path.join(os.path.dirname(tools_dir), SITE_DIR)
ref_site_path = to_unix(site_path)

logger = logging.getLogger("taipy-doc-checker")
logging.basicConfig(level=logging.INFO)
logger.info(f"Site: {site_path}")
if not os.path.isdir(site_path):
    logger.critical("Site does not exist. Please run 'mkdocs build' first.")
    exit(1)

A_RE = re.compile(r"<a href=\"(.*?)\"")
for root, _, file_list in os.walk(site_path):
    this_dir = to_unix(root)
    for f in file_list:
        if f.endswith(".html"):
            filename = to_unix(os.path.join(root, f))
            ref_filename = filename[len(ref_site_path):]
            with open(filename) as html_file:
                ref_root = to_unix(root)
                try:
                    html_content = html_file.read()
                    for anchor in A_RE.finditer(html_content):
                        href = anchor.group(1)
                        if href.startswith("/en/develop/"):
                            href = href[12:]
                        if href != "." and href != ".." and not href.startswith("http") and not href.startswith("mailto"):
                            if href.startswith("#"):
                                id=href[1:]
                                if not id in html_content:
                                    logger.error(f"No id {id} in {ref_filename}")
                            else:
                                if href.endswith("/"):
                                    target = to_unix(os.path.join(ref_root, href))[:-1]
                                    if not os.path.isdir(target) or not os.path.isfile(target + "/index.html"):
                                        logger.error(f"Bad xref '{href}' in {ref_filename}")
                except Exception as e:
                    logger.error(f"Couldn't read HTML file {filename}")
                    raise e
