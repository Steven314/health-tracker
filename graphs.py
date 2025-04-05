from shiny import ui, module

@module.ui
def graphs_ui():
    return ui.page_fluid()


@module.server
def graphs_server(input, output, session):
    pass
