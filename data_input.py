from shiny import ui, render, module, reactive
import datetime
from faicons import icon_svg

@module.ui
def data_input_ui():
    submit_button = ui.div(
        ui.input_action_button(
            "submit", 
            "Submit",
            icon = icon_svg("check"),
            class_ = "btn-primary"
        ).add_style("margin: 10px;") 
    ).add_style("display: flex; align-items: center; justify-content: center;")

    input_accord = ui.accordion(
        ui.accordion_panel(
            "Date",
            ui.div(
                ui.input_date(
                    "date", 
                    "Date", 
                    value = datetime.date.today(), 
                    format = "DD, MM d, yyyy"
                ),
                ui.input_action_button(
                    "today", 
                    "Today",
                    icon = icon_svg("calendar"),
                    class_ = "btn-primary"
                ).add_style("margin: 5px;"),
                style = "display: flex; align-items: center; justify-content: center;"
            )
        ),
        ui.accordion_panel(
            "Diet",
            ui.input_slider(
                "caffeine",
                "Caffeine (mg)",
                min = 0,
                max = 500,
                value = 140,
                step = 5,
                width = "100%"
            ),
            ui.input_slider(
                "weight",
                "Weight (lbs)",
                min = 0,
                max = 225,
                value = 134,
                step = 0.5,
                width = "100%"
            )
        ),
        ui.accordion_panel(
            "Exercise",
            ui.input_switch("running", "Running"),
            ui.input_switch("weight_lifting", "Weight Lifting"),
        ),
        ui.accordion_panel(
            "Garmin",
            ui.card(
                ui.input_slider(
                    "stress",
                    "Stress",
                    min = 0,
                    max = 100,
                    value = 25,
                    step = 1,
                    width = "100%"
                ),
            ),
            ui.card(
                ui.card_header("Sleep"),
                ui.input_slider(
                    "sleep_rhr",
                    "Resting Heart Rate (bpm)",
                    min = 40,
                    max = 100,
                    value = 55,
                    step = 1,
                    width = "100%"
                ),
                ui.input_slider(
                    "sleep_duration",
                    "Duration (hours)",
                    min = 0,
                    max = 12,
                    value = 8,
                    step = 0.25,
                    width = "100%"
                ),
                ui.input_slider(
                    "sleep_battery",
                    "Body Battery Increase",
                    min = 0,
                    max = 100,
                    value = 65,
                    step = 1,
                    width = "100%"
                )
            )
        ),
        multiple = False
    )

    return ui.page_fluid(
        input_accord,
        submit_button,
    )

@module.server
def data_input_server(input, output, session):
    @reactive.effect
    def _():
        if input.today(): 
            ui.update_date(
                "date", 
                value = datetime.date.today()
            )
