from dash import Dash, html, Input, Output, callback, State, page_container
import dash_mantine_components as dmc
from utils import navigacny_panel

app = Dash(__name__, use_pages=True)

links = {
    "about_me": {"label": "About me"},
    "projects": {"label": "Projects"},
    "contacts": {"label": "Contacts"},
    "experience": {"label": "Experience"},
    "analysis_population_count": {"label": "Analysis"},
}

app.layout = dmc.MantineProvider(
    [
        navigacny_panel(odkazy=links, logo="tabler:square-rounded-letter-d"),
        html.Div(page_container, style={"margin-top": "40px"}),
    ],
    id="theme_provider",
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
)


@callback(
    Output(component_id="theme_provider", component_property="theme"),
    Input(component_id="tlacidlo-zmena-temy", component_property="n_clicks"),
    State(component_id="theme_provider", component_property="theme"),
    config_prevent_initial_callbacks=True,
)
def change_theme(n_clicks, theme):
    return (
        {"colorScheme": "dark"}
        if theme["colorScheme"] == "light"
        else {"colorScheme": "light"}
    )


if __name__ == "__main__":
    app.run(debug=True)
