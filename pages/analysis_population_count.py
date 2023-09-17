from utils import priprava_dat
from dash import register_page, dcc, callback, Input, Output
import dash_mantine_components as dmc
from plotly.express import bar

register_page(__name__, path="/analysis_population_count")

df = priprava_dat()
# print(df[["uzemi_txt", "vzdelani_txt", "hodnota"]])

layout = dmc.Stack(
    [
        dmc.Select(
            id="area_selection",
            value="Česká republika",
            label="Choose area",
            data=[
                {"value": option, "label": option}
                for option in df["uzemi_txt"].drop_duplicates().sort_values()
            ],
        ),
        dcc.Graph(id="education_graph"),
    ]
)


@callback(
    Output(component_id="education_graph", component_property="figure"),
    Input(component_id="area_selection", component_property="value"),
)
def parse_data(area):
    w_df = df.copy()
    w_df = w_df[w_df["uzemi_txt"] == area]
    w_df = w_df.groupby(by=["vzdelani_txt"])["hodnota"].sum().reset_index()

    fig = bar(w_df, x="vzdelani_txt", y="hodnota")
    return fig
