from taipy.rest.app import create_app as rest_create_app
from taipy.rest.extensions import apispec as rest_apispec
from taipy.rest.api.views import register_views as rest_register_views
from constants import ENTERPRISE_BANNER, REST_REF_DIR_PATH, ROOT_DIR, ROOT_PACKAGE, TOOLS_DIR
from utils import restore_top_package_location


def generate_rest_api():
    app = rest_create_app()
    with app.app_context():
        rest_register_views()
        rest_specs = rest_apispec.swagger_json().json

    rest_navigation = ""

    rest_path_descs = {
        "cycle": "Entry points that interact with `Cycle^` entities.",
        "scenario": "Entry points that interact with `Scenario^` entities.",
        "pipeline": "Entry points that interact with `Pipeline^` entities.",
        "datanode": "Entry points that interact with `DataNode^` entities.",
        "task": "Entry points that interact with `Task^` entities.",
        "job": "Entry points that interact with `Job^` entities.",
        "auth": "Entry points that deal with authentication."
    }
    rest_path_files = {}
    enterprise_rest_paths = ["auth"]

    response_statuses = {
        "200": ("OK", "https://httpwg.org/specs/rfc7231.html#status.200"),
        "201": ("Created", "https://httpwg.org/specs/rfc7231.html#status.201"),
        "202": ("Accepted", "https://httpwg.org/specs/rfc7231.html#status.202"),
        "204": ("No Content", "https://httpwg.org/specs/rfc7231.html#status.204"),
        "401": ("Unauthorized", "https://httpwg.org/specs/rfc7235.html#status.401"),
        "404": ("Not Found", "https://httpwg.org/specs/rfc7231.html#status.404"),
    }


    def get_property_type(property_desc, from_schemas):
        type_name = property_desc.get("type", None)
        a_pre = ""
        a_post = ""
        if type_name == "array":
            property_desc = property_desc['items']
            type_name = property_desc.get("type", None)
            a_pre = "\\["
            a_post = "\\]"
        if type_name is None:
            type_name = property_desc.get("$ref", None)
            if type_name is None:
                # print(f"WARNING - No type...")
                return ""
            type_name = type_name[type_name.rfind('/') + 1:]
            prefix = "" if from_schemas else "../schemas/"
            type_name = f"[`{type_name}`]({prefix}#{type_name.lower()})"
        return f"{a_pre}{type_name}{a_post}"


    for path, desc in rest_specs["paths"].items():
        dest_path = None
        dest_path_desc = None
        for p, d in rest_path_descs.items():
            if f"/{p}" in path:
                dest_path = p
                dest_path_desc = d
                break
        if dest_path is None:
            print(f"Path {path} has no paths bucket")
            continue

        file = rest_path_files.get(dest_path)
        if file is None:
            file = open(f"{REST_REF_DIR_PATH}/apis_{dest_path}.md", "w")
            if dest_path in enterprise_rest_paths:
                file.write(ENTERPRISE_BANNER)
            file.write(f"{dest_path_desc}\n\n")
            rest_navigation += " " * 6 + f"- Paths for {dest_path}: manuals/reference_rest/apis_{dest_path}.md\n"
            rest_path_files[dest_path] = file

        file.write(f"# `{path}`\n\n")
        for method, method_desc in desc.items():
            file.write(f"## {method.upper()}\n\n")
            file.write(f"{method_desc['description']}\n\n")
            parameters = method_desc.get("parameters")
            if parameters is not None:
                file.write(f"<h4>Parameters</h4>\n\n")
                file.write("|Name|Type|Required|Description|\n")
                file.write("|---|---|---|---|\n")
                for param in parameters:
                    param_type = "TODO"
                    if "schema" in param and len(param["schema"]) == 1:
                        param_type = param["schema"]["type"]
                    file.write(
                        f"|{param['name']}|{param_type}|{'Yes' if param['name'] else 'No'}|{param.get('description', '-')}|\n")
                file.write("\n")
            request_body = method_desc.get("requestBody")
            if request_body is not None:
                file.write(f"<div><h4 style=\"display: inline-block;\">Request body:</h4>\n")
                schema = request_body["content"]["application/json"]["schema"]["$ref"]
                schema = schema[schema.rfind('/') + 1:]
                file.write(f"<span><a href=\"../schemas/#{schema.lower()}\">{schema}</a></div>\n\n")
            responses = method_desc.get("responses")
            if responses is not None:
                file.write(f"<h4>Responses</h4>\n\n")
                for response, response_desc in responses.items():
                    file.write(f"- <b><code>{response}</code></b><br/>\n")
                    status = response_statuses[response]
                    file.write(f"    Status: [`{status[0]}`]({status[1]})\n\n")
                    description = response_desc.get("description")
                    if description is not None:
                        file.write(f"    {description}\n")
                    content = response_desc.get("content", None)
                    if content is not None:
                        schema = content["application/json"]["schema"]
                        allOf = schema.get("allOf")
                        if allOf is not None:
                            schema = allOf[0]
                        properties = schema.get("properties")
                        if properties is not None:
                            file.write("    |Name|Type|\n")
                            file.write("    |---|---|\n")
                            for property, property_desc in properties.items():
                                file.write(f"    |{property}|{get_property_type(property_desc, False)}|\n")
                        else:
                            print(f"No properties in content in response {response} in method {method} of {path}")
                    elif response != "404":
                        print(f"No content in response {response} in method {method} of {path}")
                    file.write("\n")

    for f in rest_path_files.values():
        f.close()

    file = open(f"{REST_REF_DIR_PATH}/schemas.md", "w")
    for schema, schema_desc in rest_specs["components"]["schemas"].items():
        properties = schema_desc.get("properties")
        if properties is not None:
            file.write(f"## {schema}\n\n")
            file.write("|Name|Type|Description|\n")
            file.write("|---|---|---|\n")
            for property, property_desc in properties.items():
                file.write(f"|{property}|{get_property_type(property_desc, True)}|-|\n")
            file.write("\n")
    file.close()
    rest_navigation += " " * 6 + "- Schemas: manuals/reference_rest/schemas.md\n"

    restore_top_package_location(ROOT_DIR, ROOT_PACKAGE, TOOLS_DIR)

    return rest_navigation
