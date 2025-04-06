from shiny import ui, module, render
from faicons import icon_svg

@module.ui
def settings_ui():
    return ui.layout_columns(
        ui.card(
            ui.card_header("Settings"),
            ui.p("Settings are currently not available."),
            full_screen = True
        ),
        ui.card(
            ui.card_header("Database"),
            ui.p(
                """
                Clearing the database will clear all the saved data.
                """
            ),
            ui.div(
                ui.input_action_button(
                    "clear_db",
                    "Clear Database",
                    icon = icon_svg("trash"),
                    class_ = "btn-outline-danger",
                    width = "75%"
                )
            ).add_style("display: flex; align-items: center; justify-content: center;"),
            class_ = "border-warning"
        )
    )

@module.server
def settings_server(input, output, session):
    pass
