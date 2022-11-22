import dash
from dash import html, Input, Output, State, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from functools import lru_cache
from dash.exceptions import PreventUpdate
from data.options_commands import addlistcommands, CommandsProps


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
                    html.Div([
                        dbc.Label("IP"),
                        dbc.Input(
                            id=self.id('ip_config'), placeholder="IP Padrão", type="text"),
                        dbc.FormText(
                            "Formato xxx.xxx.xxx.xxx"),
                        html.Br(),
                    ]),
                    dbc.Col([
                        html.Div([
                            dbc.Label("Máscara de Sub-Rede"),
                            dbc.Input(
                                id=self.id('netmask'), placeholder="IP Padrão", type="text"),
                            dbc.FormText(
                                "Formato xxx.xxx.xxx.xxx"),
                            html.Br(),
                        ]),
                    ], width=6),
                    dbc.Col([
                        html.Div([
                            dbc.Label("Gateway"),
                            dbc.Input(
                                id=self.id('gateway'), placeholder="IP Padrão", type="text"),
                            dbc.FormText(
                                "Formato xxx.xxx.xxx.xxx"),
                        ]),
                    ], width=6),
                    html.Br(),
                    dbc.Button(
                        'Configurar', id=self.id('trigger-configure'), n_clicks=0, color="primary", className="me-1")
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
                State(self.id('ip_default'), 'value'),
                State(self.id('ip_config'), 'value'),
                State(self.id('gateway'), 'value'),
                State(self.id('netmask'), 'value'),
            ],
            prevent_initial_call=True
        )
        def create_list_commands(n_clicks, ip_default, final_ip, gateway, netmask):
            if n_clicks is None:
                raise PreventUpdate()
            else:
                commands = addlistcommands(CommandsProps(
                    ip_config=final_ip,
                    gateway=gateway,
                    netmask=netmask,
                ))
                print(commands)
                return dbc.Alert("Parabéns, concluido com erro.", color="success", duration=5000)
