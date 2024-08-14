from dataikuapi import DSSClient
from taipy.gui import Gui
import pandas as pd
import taipy.gui.builder as tgb

host = "HOST"
apiKey = "API_KEY"

c = DSSClient(host, apiKey)

metrics_table = []
nb_projects = 0
for project_keys in c.list_project_keys():
    nb_projects = nb_projects + 1
    if nb_projects == 200:
        break
    line = {}
    proj = c.get_project(project_keys)
    line["label"] = proj.get_metadata()["label"]
    for modelId in proj.list_saved_models():
        m = proj.get_saved_model(modelId["id"])
        try:
            active_Id = m.get_active_version().get("id", None)
            line["active_Id"] = active_Id
            metrics = m.get_metric_values(active_Id)
            for metric in metrics.raw["metrics"]:
                metric_type = metric["metric"]["metricType"]
                if metric_type == "AUC":
                    value = metric["lastValues"][0]["value"]
                    value = metric["lastValues"][0]["value"]

                    metrics_table.append(
                        {
                            "Project": line["label"],
                            "ModelId": modelId["id"],
                            "ActiveId": active_Id,
                            "MetricType": metric_type,
                            "Value": value,
                        }
                    )
        except Exception as e:
            print(e)
            pass

metrics_table = pd.DataFrame(metrics_table)
metrics_table["Name"] = (
    metrics_table["Project"]
    + " - "
    + metrics_table["ModelId"]
    + " - "
    + metrics_table["MetricType"]
)

metrics_table.to_csv("metrics_huge.csv", index=False)

selected_projects = list(metrics_table["Project"].unique())
selected_metrics = [list(metrics_table["MetricType"].unique())[0]]


def show_projects(metrics_table, selected_projects, selected_metrics):
    return metrics_table[
        metrics_table["Project"].isin(selected_projects)
        & metrics_table["MetricType"].isin(selected_metrics)
    ]


with tgb.Page() as page:
    tgb.text("# Dataiku **Overview**", mode="md")

    tgb.text("**Projects**", mode="md")

    tgb.selector(
        "{selected_projects}",
        lov=list(metrics_table["Project"].unique()),
        multiple=True,
        label="Projects",
        dropdown=True,
        class_name="fullwidth",
    )

    tgb.text("**Metrics**", mode="md")

    tgb.selector(
        "{selected_metrics}",
        lov=list(metrics_table["MetricType"].unique()),
        multiple=True,
        label="Metrics",
        dropdown=True,
        class_name="fullwidth",
    )

    # Taipy 4.0 required for Lambda expression.
    # Or replace by "{show_projects(metrics_table, selected_projects, selected_metrics}"
    tgb.table(
        lambda metrics_table, selected_projects, selected_metrics: show_projects(
            metrics_table, selected_projects, selected_metrics
        ),
        filter=True,
    )

    # Taipy 4.0 required for Lambda expression.
    # Or replace by "{show_projects(metrics_table, selected_projects, selected_metrics}"
    tgb.chart(
        lambda metrics_table, selected_projects, selected_metrics: show_projects(
            metrics_table, selected_projects, selected_metrics
        ),
        x="Name",
        y="Value",
        type="bar",
    )


Gui(page).run()
