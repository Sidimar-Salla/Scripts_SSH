import dash
from dash import html, Input, Output, State, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from functools import lru_cache
from dash.exceptions import PreventUpdate
from data.options_commands import addlistcommands, CommandsProps


class FiberPort:
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
                "Porta de fibra", className="ms-1")]),
            html.Br(),
            dbc.Row([
                html.Div([
                    dbc.Label("IP"),
                    dbc.Input(
                        id=self.id('ip_equipamento'), placeholder="xxx.xxx.xxx.xxx", type="text"),
                    dbc.FormText(
                        "Informe o IP que o equipamento está configurado. Ex.: 192.168.0.1"),
                ]),
                html.Hr(),
                html.Div([
                    dbc.Label("Porta"),
                    dbc.Input(
                        id=self.id('port_fibre'), placeholder="Port", type="number"),
                    dbc.FormText(
                        "Informe qual porta a fibra foi conectada."),
                ]),
                dbc.Button("Configurar", color="primary",
                           className="me-1", id=self.id('trigger-configure'), n_clicks=0)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Spinner(html.Div([], id=self.id('result'))),
            ])
        ])

    def events(self) -> None:
        @callback(
            Output(self.id('result'), 'children'),
            Input(self.id('trigger-configure'), 'n_clicks'),
            [
                State(self.id('port_fibre'), 'value'),
            ],
            prevent_initial_call=True
        )
        def create_list_commands(n_clicks, port_fibre):
            if n_clicks is None:
                raise PreventUpdate()
            else:
                commands = addlistcommands(
                    CommandsProps(
                        fibre_port=port_fibre,
                    )
                )
                print(commands)
                return dbc.Alert("Parabéns, concluido com erro.", color="success", duration=5000)
