import ipywidgets as widgets
from IPython.display import display


def make_multi_select_question(prompt, options, correct_indices):
    checkboxes = [widgets.Checkbox(value=False, description=opt, indent=False,
                                    layout=widgets.Layout(width="100%")) for opt in options]
    button = widgets.Button(description="Check answer", button_style="primary")
    output = widgets.Output()

    def on_click(_):
        output.clear_output()
        selected = {i for i, cb in enumerate(checkboxes) if cb.value}
        with output:
            if selected == set(correct_indices):
                print("✅ Correct!")
            else:
                print("❌ Not quite — uncheck/check some boxes and try again.")

    button.on_click(on_click)
    display(widgets.HTML(f"<b>{prompt}</b>"), *checkboxes, button, output)


def make_true_false_question(prompt, correct_answer):
    toggle = widgets.ToggleButtons(options=["True", "False"], style={"button_width": "100px"})
    button = widgets.Button(description="Check answer", button_style="primary")
    output = widgets.Output()

    def on_click(_):
        output.clear_output()
        with output:
            if (toggle.value == "True") == correct_answer:
                print("✅ Correct!")
            else:
                print("❌ Not quite — try again.")

    button.on_click(on_click)
    display(widgets.HTML(f"<b>{prompt}</b>"), toggle, button, output)


def question1():
    make_multi_select_question(
        "Select all factors that probably contributed to the accident:",
        [
            "The helicopter pilot was flying too high.",
            "The airplane pilot did not see the helicopter.",
            "The airplane pilot was too tired.",
            "The airport controller was having a non-pertinent phone call.",
        ],
        correct_indices={0, 1, 3},
    )


def question2():
    make_true_false_question(
        "If the helicopter pilot had been flying lower, the accident probably would not have "
        "happened.",
        correct_answer=False,
    )


def question3():
    make_true_false_question(
        "If the airport's manager had talked to the controller about the earlier non-pertinent "
        "phone call, the accident probably would not have happened.",
        correct_answer=True,
    )
