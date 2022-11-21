import dash
from dash import html, Input, Output, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from functools import lru_cache
from components.button_config import ButtonComponent


class AddIP:
    def __init__(self) -> None:
        self._id = hashlib.md5(
            str(pathlib.Path(__file__).absolute()).encode()).hexdigest()
        self.events()

    def id(self, name):
        return f"{name}-{self._id}"

    def load_data(self) -> None:
        pass

    @property
    def layout(self):
        self.load_data()
        return dbc.Container([
            html.H4(["Configurar", dbc.Badge(
                "IP", className="ms-1")]),
            html.Br(),
            dbc.Row([
                    html.Div([
                        dbc.Label("IP Padrão"),
                        dbc.Input(
                            id=self.id('ip_default'), placeholder="IP Padrão", type="text",
                            value="192.168.0.25"),
                        dbc.FormText(
                            "Geralmente o IP padrão dos switch's Datacom é  192.168.0.25"),
                    ]),
                    html.Hr(),
                    dbc.Col([
                        html.Div([
                            dbc.Label("IP à configurar"),
                            dbc.Input(
                                id=self.id('ip_config'), placeholder="IP Padrão", type="text"),
                            dbc.FormText(
                                "Formato xxx.xxx.xxx.xxx"),
                            html.Br(),
                        ]),
                        html.Div([
                            dbc.Label("Máscara de Sub-Rede"),
                            dbc.Input(
                                id=self.id('ip_config'), placeholder="IP Padrão", type="text"),
                            dbc.FormText(
                                "Formato xxx.xxx.xxx.xxx"),
                            html.Br(),
                        ]),
                    ], width=6),
                    dbc.Col([
                        html.Div([
                            dbc.Label("Gateway"),
                            dbc.Input(
                                id=self.id('ip_config'), placeholder="IP Padrão", type="text"),
                            dbc.FormText(
                                "Formato xxx.xxx.xxx.xxx"),
                        ]),
                    ], width=6),
                    html.Br(),
                    ButtonComponent().layout
                    ]),
        ])

    def events(self) -> None:
        pass
        # dbc.Alert("Configurado com sucesso!",
        #           color="success", duration=5000)
