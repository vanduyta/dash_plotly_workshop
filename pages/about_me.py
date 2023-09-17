from dash import register_page
import dash_mantine_components as dmc

register_page(__name__, path="/about_me")

layout = dmc.Text("About me")
# defaultne se komponenty vykresli na celou sirku rodicovske komponenty
o_mne_text = "Prvý kontakt s programovaním som mal ešte v študentských časoch a odvtedy sa moje kódovanie stalo súčasťou môjho DNA. Mojím poslaním je prinášať riešenia prostredníctvom kódu, ktoré majú skutočný dopad na svet. Vo svojej voľnej chvíli ma nájdete buď hlboko ponoreného do nového projektu alebo hľadajúceho inšpiráciu v prírode a technológii."
layout = dmc.Grid(
    [
        dmc.Col(
            [
                dmc.Grid(
                    [
                        dmc.Col([dmc.Divider(label="Who am I?", size="sm")]),
                    ]
                ),
                dmc.Grid(
                    [
                        dmc.Col(dmc.Text(o_mne_text), sm=8),
                        dmc.Col(
                            dmc.Image(src="/assets/profile_picture_pingu.svg"),
                            sm=4,
                        ),
                    ]
                ),
            ],
            sm=4,
            offsetSm=3,
            offset=1,
            span=10,
        )
    ]
)
