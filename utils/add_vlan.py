import dash
from dash import html, Input, Output, State, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from functools import lru_cache
from dash.exceptions import PreventUpdate
from data.options_commands import addlistcommands, CommandsProps


class AddVLAN:
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
                "VLAN's", className="ms-1")]),
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
                    dbc.Label("VLAN para Gerenciamento"),
                    dbc.Input(
                        id=self.id('mngt_vlan'), placeholder="1 to 4093", type="text"),
                    dbc.FormText(
                        "Informe a VLAN que irá ser usado para gerenciamento do equipamento."),
                ]),
                dbc.Col([
                    html.Div([
                        dbc.Label("Vlan"),
                        dbc.Input(
                            id=self.id('list_vlan'), placeholder="1 to 4093", type="text"),
                        dbc.FormText(
                            "Número da Vlan que será adicionado. Ex.: 100, 120, 130"),
                    ]),
                ], width=6),
                dbc.Col([
                    html.Div([
                        dbc.Label("Nome"),
                        dbc.Input(
                            id=self.id('name_vlan'), placeholder="Nome", type="text"),
                        dbc.FormText(
                            "Nome que será vinculado a vlan. Obs.: Nomear na mesma ordem dos números."),
                    ]),
                ], width=6),
                html.Br(),
                dbc.Button("Configurar", color="primary",
                           className="me-1", id=self.id('trigger-configure'), n_clicks=0),
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
                State(self.id('ip_equipamento'), 'value'),
                State(self.id('mngt_vlan'), 'value'),
                State(self.id('list_vlan'), 'value'),
                State(self.id('name_vlan'), 'value'),
            ],
            prevent_initial_call=True
        )
        def create_list_commands(n_clicks, ip_default, mngt_vlan, list_vlan, list_name):
            if n_clicks is None:
                raise PreventUpdate()
            else:
                commands = addlistcommands(
                    CommandsProps(
                        mngt_vlan=mngt_vlan,
                        vlan=list_vlan,
                        vlan_nomes=list_name,
                    )
                )
                print(commands)
                return dbc.Alert("Parabéns, concluido com erro.", color="success", duration=5000)
