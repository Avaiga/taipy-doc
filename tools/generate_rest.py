import copy
import json

from taipy.rest.api.views import register_views
from taipy.rest.app import create_app
from taipy.rest.extensions import apispec


def _split_into_components(specs: dict):
    paths = ["cycle", "scenario", "pipeline", "datanode", "task", "job"]

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


if __name__ == "__main__":

    app = create_app()
    with app.app_context():
        register_views()
        specs = apispec.swagger_json().json

    _split_into_components(specs)
