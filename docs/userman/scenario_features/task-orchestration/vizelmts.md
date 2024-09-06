Taipy provides some visual elements dedicated useful for Task orchestration. These elements are the
*scenario selector*, the *scenario viewer*, and the *job selector*.

# Scenario Selector
The *scenario selector* control (`scenario_selector`) is designed to create and select scenarios
easily. It provides users with the ability to switch between them seamlessly.

The default usage is really simple. It does not require any specific configuration to display
the selectable scenarios. The following image shows the default behavior of the
*scenario selector* control when three scenarios exist.

<figure class="tp-center">
<img src="../img/vizelmts/scenario-selector-default-behavior.png" class="visible-dark"/>
<img src="../img/vizelmts/scenario-selector-default-behavior.png" class="visible-light"/>
<figcaption>The list of selectable scenarios</figcaption>
</figure>

When the "Add scenario" button is pressed, a form is displayed to create a new scenario with the
desired settings, in particular the `ScenarioConfig^` used to instantiate the new scenario.
The following image shows the form to create a new scenario.

<figure class="tp-center">
<img src="../img/vizelmts/scenario-selector-default-behavior-create.png" class="visible-dark"/>
<img src="../img/vizelmts/scenario-selector-default-behavior-create.png" class="visible-light"/>
<figcaption>The list of selectable data nodes</figcaption>
</figure>

Thanks to its rich configurability, you can greatly customize the display of the scenario
selector, for example, adding a search bar, adding a filter or a sort capability, grouping
the scenarios by cycle, etc. For more details, see the
[scenario selector](../../../refmans/gui/viselements/corelements/scenario_selector.md) page.

# Scenario Viewer
The *scenario viewer* control (`scenario`) displays a scenario's information and lets
end-users interact with it.

The default usage is really simple. It does not require any specific configuration to display
a selected scenario.

<figure class="tp-center">
<img src="../img/vizelmts/scenario-viewer-default-behavior.png" class="visible-dark"/>
<img src="../img/vizelmts/scenario-viewer-default-behavior.png" class="visible-light"/>
<figcaption>The selected scenario</figcaption>
</figure>

All the information about the scenario is displayed and various buttons are available to
interact with the scenario. In particular, the end-user can submit the scenario for execution,
using the top right button "Submit". The scenario's sequences are also displayed, and the
end-user can create, delete or submit them. Most of the fields and interactions are customizable.

For more details, see the [scenario viewer](../../../refmans/gui/viselements/corelements/scenario.md) page.

# Job selector
The *job selector* control (`job_selector`) displays the list of jobs submitted to a Taipy
application. It lists all the jobs with other related information, in particular the job status,
and provides users with the ability to select a job.

As usual, the default usage is really simple. It does not require any specific configuration to get
the following display.

<figure class="tp-center">
<img src="../img/vizelmts/job-selector-default-behavior.png" class="visible-dark"/>
<img src="../img/vizelmts/job-selector-default-behavior.png" class="visible-light"/>
<figcaption>The job list</figcaption>
</figure>

Thanks to its rich configurability, you can customize the columns to display in job selector.
For more details, see the [job selector](../../../refmans/gui/viselements/corelements/job_selector.md) page.

# Task orchestration interface

Once your execution graph is modeled as data nodes and tasks, it becomes easy to get a user
interface to manage and monitor your submissions. The combination of the *scenario selector*,
the *scenario viewer*, and the *job selector* controls provides a user-friendly interface
covering the whole task orchestration functionalities.

!!! example "Combining visual elements"

    === "Task orchestration interface"
        The following image shows an example of how to combine the *scenario selector*,
        the *scenario viewer*, and the *job selector* controls. On the top, the *scenario selector*
        displays all the scenarios that can be selected. Below, the *scenario viewer* displays
        the selected scenario. Finally, the *job selector* displays the list of jobs created and
        submitted through the submission of scenarios and sequences in the *scenario viewer*.

        <figure class="tp-center">
        <img src="../img/vizelmts/task-orchestration-vizelements.png" class="visible-dark" width="70%"/>
        <img src="../img/vizelmts/task-orchestration-vizelements.png" class="visible-light" width="70%"/>
        <figcaption>Task orchestration interface</figcaption>
        </figure>

    === "Corresponding code"
        The following code shows a complete example of how to combine the visual elements.
        It consists of creating a dumb function named "identity" and used to create a scenario
        configuration. A user interface is created with the three controls thanks to the GUI service.

        ```python linenums="1"
        {%
        include-markdown "./code-example/vizelemts/task-orchestration-vizelements-default-behavior.py"
        comments=false
        %}
        ```
