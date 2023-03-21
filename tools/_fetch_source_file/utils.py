import os
import re


def read_doc_version_from_mkdocs_yml_template_file(root_dir):
    """Read version from mkdocs.yml template"""
    mkdocs_yml_template = None
    mkdocs_yml_template_path = os.path.join(root_dir, "mkdocs.yml_template")
    with open(mkdocs_yml_template_path, "r") as mkdocs_file:
        mkdocs_yml_template = mkdocs_file.read()
    if mkdocs_yml_template is None:
        raise IOError(f"Couldn't open '{mkdocs_yml_template_path}'")
    mkdocs_yml_version = re.search(r"site_url:\s*https://docs\.taipy\.io/en/(develop|release-(\d\.\d))$",
                                   mkdocs_yml_template, re.MULTILINE)
    if mkdocs_yml_version is None:
        raise ValueError(
            f"'{mkdocs_yml_template_path}' has an invalid site_url value. This must be 'develop' or 'release-[M].[m]'.")
    return mkdocs_yml_version.group(2) if mkdocs_yml_version.group(2) else mkdocs_yml_version.group(1)
