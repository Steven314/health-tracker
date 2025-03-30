from shiny import App, ui
from pathlib import Path
from faicons import icon_svg

app_ui = ui.page_navbar(
    ui.nav_control(
        ui.a(
            ui.span(icon_svg("github"), "S. L. Carter"), 
            href = "https://steven314.github.io/", 
            target = '_blank'
        )
    ),
    ui.nav_panel(title = "Home"),
    ui.head_content(
        ui.tags.link(
            rel="icon", type="image/png", sizes="32x32", href="hex_32.png"
        ),
        ui.tags.link(
            rel="icon", type="image/png", sizes="16x16", href="hex_16.png"
        )
    ),
    title = ui.div(
        ui.img(src = "hex.png", height = '64px', style = "margin-right: 10px"),
        ui.span("Health Tracker", style = "text-transform: uppercase; font-weight: bold;")
    ),
    theme = ui.Theme(preset = "pulse"),
    navbar_options = ui.navbar_options(
        class_         = "bg-primary",
        theme          = "dark",
        bg             = "#a13545",
        underline      = False,
        enable_rounded = True
    ),
    window_title = "Health Tracker"
)

def server(input, output, session):
    pass

www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets = www_dir)
