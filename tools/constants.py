import os

ROOT_PACKAGE = "taipy"
MODULE_EXTENSIONS = ".py"
PACKAGE_GROUP = [ "taipy.config", "taipy.core", "taipy.gui", "taipy.rest", "taipy.auth", "taipy.enterprise" ]

# Assuming that this script is located in <taipy-doc>/tools
TOOLS_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
ROOT_DIR = os.path.dirname(TOOLS_DIR)

GUI_DOC_PATH = ROOT_DIR + "/docs/manuals/gui/"
VISELEMENTS_SRC_PATH = ROOT_DIR + "/gui/doc"
VISELEMENTS_DIR_PATH = ROOT_DIR + "/docs/manuals/gui/viselements"
REST_REF_DIR_PATH = ROOT_DIR + "/docs/manuals/reference_rest"

ENTERPRISE_BANNER = """!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

"""

# (item_pattern, destination_package)
# or ([item_pattern...], destination_package)
FORCE_PACKAGE = [
    ("typing.*", "taipy.core"),
    ("taipy.gui.*.(Gui|State|Markdown|Page)", "taipy.gui"),
    (["taipy.core.cycle.cycle.Cycle",
      "taipy.core.data.data_node.DataNode",
      "taipy.core.common.frequency.Frequency",
      "taipy.core.job.job.Job",
      "taipy.core.pipeline.pipeline.Pipeline",
      "taipy.core.scenario.scenario.Scenario",
      "taipy.core.common.scope.Scope",
      "taipy.core.job.status.Status",
      "taipy.core.task.task.Task",
      "taipy.core.taipy.clean_all_entities",
      "taipy.core.taipy.cancel_job",
      "taipy.core.taipy.compare_scenarios",
      "taipy.core.taipy.create_pipeline",
      "taipy.core.taipy.create_scenario",
      "taipy.core.taipy.delete",
      "taipy.core.taipy.delete_job",
      "taipy.core.taipy.delete_jobs",
      "taipy.core.taipy.get",
      "taipy.core.taipy.get_cycles",
      "taipy.core.taipy.get_data_nodes",
      "taipy.core.taipy.get_jobs",
      "taipy.core.taipy.get_latest_job",
      "taipy.core.taipy.get_pipelines",
      "taipy.core.taipy.get_primary",
      "taipy.core.taipy.get_primary_scenarios",
      "taipy.core.taipy.get_scenarios",
      "taipy.core.taipy.get_tasks",
      "taipy.core.taipy.set",
      "taipy.core.taipy.set_primary",
      "taipy.core.taipy.submit",
      "taipy.core.taipy.subscribe_pipeline",
      "taipy.core.taipy.subscribe_scenario",
      "taipy.core.taipy.tag",
      "taipy.core.taipy.unsubscribe_pipeline",
      "taipy.core.taipy.unsubscribe_scenario",
      "taipy.core.taipy.untag"], "taipy.core"),
    ("taipy.core.data.*.*DataNode", "taipy.core.data"),
    ("taipy.rest.rest.Rest", "taipy.rest")
]

# Entries that should be hidden for the time being
HIDDEN_ENTRIES = ["Decimator", "get_context_id", "invoke_state_callback"]

REFERENCE_REL_PATH = "manuals/reference"
REFERENCE_DIR_PATH = ROOT_DIR + "/docs/" + REFERENCE_REL_PATH
XREFS_PATH = ROOT_DIR + "/docs/manuals/xrefs"
MKDOCS_YML_TEMPLATE_PATH = ROOT_DIR + "/mkdocs.yml_template"
MKDOCS_YML_PATH = ROOT_DIR + "/mkdocs.yml"
