# Create your scenario:

<|layout|columns=3 1 1 1 1|
<|{scenario}|scenario_selector|>

**Prediction date** <br/>
<|{day}|date|active={scenario}|not with_time|>

**Max capacity** <br/>
<|{max_capacity}|number|active={scenario}|>

**Number of predictions** <br/>
<|{n_predictions}|number|active={scenario}|>

<br/> <|Save|button|on_action=save|active={scenario}|>
|>
 
<|{scenario}|scenario|on_submission_change=submission_change|>

<|{predictions_dataset}|chart|x=Date|y[1]=Historical values|type[1]=bar|y[2]=Predicted values ML|y[3]=Predicted values Baseline|>