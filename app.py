from shiny import App, ui, reactive
from pathlib import Path
from faicons import icon_svg
import settings
import data_input
import graphs

dull_red = "#a13545"

app_ui = ui.page_navbar(
    ui.nav_control(
        ui.a(
            ui.span(icon_svg("github"), "S. L. Carter"), 
            href = "https://steven314.github.io/", 
            target = '_blank'
        )
    ),
    ui.nav_spacer(),
    ui.nav_panel(
        "Home", 
        ui.page_fillable(
            # buttons for each tab, evenly spaced on the page.
            ui.div(
                ui.input_action_button(
                    "data_input1", 
                    "Inputs", 
                    icon = icon_svg("keyboard"), 
                    class_ = "btn-primary",
                    height = "100%",
                    width = "100%",
                    style = "margin: 10px;"
                ),
                ui.input_action_button( 
                    "graph1",
                    "Graphs",
                    icon = icon_svg("chart-simple"),
                    class_ = "btn-primary",
                    height = "100%",
                    width = "100%",
                    style = "margin: 10px;"
                ),
                ui.input_action_button(
                    "settings1", 
                    "Settings", 
                    icon = icon_svg("gear"), 
                    class_ = "btn-primary",
                    height = "100%",
                    width = "100%",
                    style = "margin: 10px;"
                ),
                style = "display: flex; flex-direction: column; align-items: center; justify-content: space-between;"
            ),
            fillable_mobile = True
        ),
        icon = icon_svg("house")
    ),
    ui.nav_panel(
        "Inputs", 
        data_input.data_input_ui("data_input1"),
        icon = icon_svg("keyboard")
    ),
    ui.nav_panel(
        "Graphs", 
        graphs.graphs_ui("graph1"),
        icon = icon_svg("chart-simple")
    ),
    ui.nav_panel(
        "Settings", 
        settings.settings_ui("settings1"),
        icon = icon_svg("gear")
    ),
    ui.nav_spacer(),
    ui.nav_menu(
        "Extras",
        ui.nav_control(
            ui.a(
                ui.span(icon_svg("code"), "Source Code"), 
                href = "https://github.com/Steven314/health-tracker/", 
                target = '_blank'
            )
        ),
        # center the dark mode toggle
        ui.nav_control(
            ui.input_dark_mode(
                style = "display: flex; align-items: center; justify-content: center;"
            )
        ),
        icon = icon_svg("flask"),
        align = "right"
    ),
    ui.head_content(
        ui.tags.link(
            rel = "icon", type = "image/png", 
            sizes = "32x32", href = "hex_32.png"
        ),
        ui.tags.link(
            rel = "icon", type = "image/png",
            sizes = "16x16", href = "hex_16.png"
        )
    ),
    title = ui.div(
        ui.img(src = "hex.png", height = '64px', style = "margin-right: 10px"),
        ui.span(
            "Health Tracker", 
            style = "font-weight: bold;"
        )
    ),
    id = "main",
    theme = ui.Theme(preset = "zephyr").add_defaults(primary = dull_red),
    navbar_options = ui.navbar_options(
        class_         = "bg-primary",
        theme          = "dark",
        underline      = False,
        enable_rounded = True
    ),
    window_title = "Health Tracker"
)

def server(input, output, session):
    @reactive.effect
    def _():
        """
        Updates the selected tab on the sidebar when the corresponding button is
        clicked.
        """
        if input.data_input1():
            ui.update_navs(
                "main", 
                selected = "Inputs"
            )
        
        if input.graph1():
            ui.update_navs(
                "main",
                selected = "Graphs"
            )
        
        if input.settings1():
            ui.update_navs(
                "main",
                selected = "Settings"
            )
        
    data_input.data_input_server("data_input1")
    settings.settings_server("settings1")
    graphs.graphs_server("graph1")
    
www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets = www_dir)
