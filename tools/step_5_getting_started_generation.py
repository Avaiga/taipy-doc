import glob
from pathlib import Path


def generate_getting_started():

    def format_getting_started_navigation(filepath: str) -> str:
        readme_path = f"{filepath}/ReadMe.md".replace('\\', '/')
        readme_content = Path('docs', readme_path).read_text().split('\n')
        step_name = next(filter(lambda l: "# Step" in l, readme_content))[len("# "):]
        return f"    - '{step_name}': '{readme_path}'"

    step_folders = glob.glob("docs/getting_started/step_*")
    step_folders.sort()
    step_folders = map(lambda s: s[len('docs/'):], step_folders)
    step_folders = map(format_getting_started_navigation, step_folders)
    getting_started_navigation = "\n".join(step_folders) + '\n'
    return getting_started_navigation
