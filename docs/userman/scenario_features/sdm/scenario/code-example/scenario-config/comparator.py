from taipy import Config


def compare_kpis(*data_to_compare):
    return max(*data_to_compare)


kpi_cfg = Config.configure_data_node("KPI")
scenario_cfg = Config.configure_scenario("scenario",
                                         additional_data_node_configs=[kpi_cfg],
                                         comparators={kpi_cfg.id: compare_kpis})
