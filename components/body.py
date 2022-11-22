import dash
from dash import html, Input, Output, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from functools import lru_cache
from utils.add_ip import AddIP
from utils.add_vlan import AddVLAN
from utils.fiber_port import FiberPort
from utils.network_port import NetworkPort
from dash.exceptions import PreventUpdate


class BodyComponent:
    def __init__(self) -> None:
        self._id = hashlib.md5(
            str(pathlib.Path(__file__).absolute()).encode()).hexdigest()
        self.register_options = {
            'ip': AddIP(),
            'vlan': AddVLAN(),
            'fiber': FiberPort(),
            'network': NetworkPort(),
        }
        self.events()

    def id(self, name):
        return f"{name}-{self._id}"

    def load_data(self) -> None:
        pass

    @property
    def layout(self):
        self.load_data()
        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1('Datacom', style={'text-align': 'center'}),
                    html.Hr(),
                    html.H5('Configurar:'),
                    dcc.RadioItems([
                        'Adicionar IP',
                        "Adicionar VLAN's",
                        'Porta de fibra',
                        'Porta de Rede'
                    ], id=self.id('select_config')),
                ], width=2),
                dbc.Col([
                    dbc.Spinner(html.Div([
                    ], id=self.id('output_config')))
                ], width=9)
            ])
        ])

    def events(self) -> None:
        @callback(
            Output(self.id('output_config'), 'children'),
            Input(self.id('select_config'), 'value'),
            prevent_initial_call=True
        )
        def altern_configs(value):
            if value == 'Adicionar IP':
                return self.register_options['ip'].layout
            if value == "Adicionar VLAN's":
                return self.register_options['vlan'].layout
            if value == 'Porta de fibra':
                return self.register_options['fiber'].layout
            if value == 'Porta de Rede':
                return self.register_options['network'].layout
            raise PreventUpdate
