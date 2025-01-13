from taipy.gui import Gui, Markdown, State, invoke_long_callback, notify
import taipy.gui.builder as tgb


def pi_approx(num_iterations: int):
    """
    Approximate Pi using the Leibniz formula.

    Args:
        num_iterations: Number of iterations to compute the approximation.

    Returns:
        A list of approximations of Pi, made at each iteration.
    """
    k, s = 3.0, 1.0
    pi_list = []
    for i in range(num_iterations):
        s = s - ((1 / k) * (-1) ** i)
        k += 2
        if (i + 1) % (int(num_iterations / 100) + 1) == 0:
            pi_list += [4 * s]

    return pi_list


def heavy_status(state: State, status, pi_list: list):
    """
    Periodically update the status of the long callback.

    Args:
        state: The state of the application.
        status: The status of the long callback.
        pi_list: The list of approximations of Pi.
    """
    state.logs = f"Approximating Pi... ({status}s)"
    if isinstance(status, bool):
        if status:
            state.logs = f"Finished! Approximation: {pi_list[-1]}"
            notify(state, "success", "Finished")
            state.pi_list = pi_list
        else:
            notify(state, "error", "An error was raised")
    else:
        state.status += 1


def approximate_pi(state: State):
    """
    When the button is clicked, start the long callback.

    Args:
        state: The state of the application.
    """
    invoke_long_callback(
        state, pi_approx, [int(state.num_iterations)], heavy_status, [], 1000
    )


if __name__ == "__main__":
    status = 0
    num_iterations = 20_000_000
    pi_list = []
    logs = "Not running"

    with tgb.Page() as page:
        tgb.text("# Approximating **Pi** using the Leibniz formula", mode="md")
        tgb.number("{num_iterations}", label="Number of iterations")
        tgb.button("Approximate Pi", on_action=approximate_pi)

        tgb.text("## Evolution of approximation", mode="md")
        tgb.chart("{pi_list}", layout="{layout}")

        tgb.html("br")

        with tgb.part("card"):
            tgb.text("## Logs", mode="md")
            tgb.text("### {logs}", mode="md")

    layout = {
        "xaxis": {"title": "Iteration (Percentage of Total Iterations)"},
        "yaxis": {"title": "Pi Approximation"},
    }

    Gui(page).run()
