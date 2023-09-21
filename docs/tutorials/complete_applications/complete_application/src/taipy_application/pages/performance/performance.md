<|part|render={len(comparison_scenario)>0}|

<|Table|expanded=False|expandable|
<|{comparison_scenario}|table|>
|>

<|{selected_metric}|selector|lov={metric_selector}|dropdown|>

<|{comparison_scenario}|chart|type=bar|x=Scenario Name|y[1]=RMSE baseline|y[2]=RMSE ML|render={selected_metric=="RMSE"}|>

<|{comparison_scenario}|chart|type=bar|x=Scenario Name|y[1]=MAE baseline|y[2]=MAE ML|render={selected_metric=="MAE"}|>
|>


<center><|Compare primarys|button|on_action=compare|></center>