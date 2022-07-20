import copy
import json
from subprocess import call

from taipy.rest.api.views import register_views
from taipy.rest.app import create_app
from taipy.rest.extensions import apispec

enterprise_warnings = """!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

"""


def _split_into_components(specs: dict):
    """
    Require node and widdershins to be installed on local machine.

    `npm i -g widdershins`
    """
    paths = ["cycle", "scenario", "pipeline", "datanode", "task", "job", "auth"]
    enterprise_paths = ["auth"]

    for p in paths:
        tmp = copy.deepcopy(specs)
        if p != "job":
            filtered_schema = {k: v for k, v in tmp["components"]["schemas"].items() if p in k.lower()}
        else:
            filtered_schema = {k: v for k, v in tmp["components"]["schemas"].items() if p or "callable" in k.lower()}
        filtered_path = {k: v for k, v in tmp["paths"].items() if p in k.lower()}

        tmp["components"]["schemas"] = filtered_schema
        tmp["paths"] = filtered_path
        with open(f"docs/manuals/rest/{p}.json", "w") as f:
            json.dump(tmp, f)
        call(
            f"widdershins --omitHeader true --search false --language_tabs --summary docs/manuals/rest/{p}.json -o docs/manuals/rest/{p}.md",
            shell=True,
        )

        if p in enterprise_paths:
            with open(f"docs/manuals/rest/{p}.md", "r") as f:
                content = f.read()
            with open(f"docs/manuals/rest/{p}.md", "w") as f:
                f.write(enterprise_warnings + content)


if __name__ == "__main__":

    app = create_app()
    with app.app_context():
        register_views()
        specs = apispec.swagger_json().json

    _split_into_components(specs)
