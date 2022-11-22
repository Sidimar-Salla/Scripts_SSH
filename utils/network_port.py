import dash
from dash import html, Input, Output, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from functools import lru_cache


class NetworkPort:
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
                "Porta de Rede", className="ms-1")]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Input(placeholder="IP Padrão", type="text"),
                    html.Br(),
                ], width=6),
                dbc.Col([
                    dbc.Input(placeholder="IP Final", type="text"),
                ], width=6),
                html.Br(),
            ])
        ])

    def events(self) -> None:
        pass
