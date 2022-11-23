import dash
from dash import html, Input, Output, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from functools import lru_cache


class NavbarComponent:
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
        return dbc.Navbar([
            dbc.Container([
                html.A(
                    dbc.Row([
                        # dbc.Col(
                        #     html.Img(src='/assets/img/logo_nutrire.png',
                        #              height='40px')
                        # ),
                        dbc.Col(
                            dbc.NavbarBrand(
                                "Configurar Switch", className="ms-2")
                        ),
                    ],
                        align="center",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Row([
                            dbc.Nav([
                                dcc.Location(id=self.id(
                                    'result'), refresh=True),
                                dbc.NavItem(dbc.NavLink(
                                    id=self.id('userName'))),
                                dbc.DropdownMenu([
                                    dbc.DropdownMenuItem(
                                        "Mais opções", header=True),
                                    dbc.DropdownMenuItem(
                                        "Sobre", href="nutrire.ind.br", target='_blank'),
                                    dbc.DropdownMenuItem(
                                        "Sair", id=self.id('button_logout')),
                                ],
                                    nav=True,
                                    in_navbar=True,
                                    label="Mais",
                                ),
                            ])
                            ],
                            className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
                            align="center",
                            ),
                    id=self.id("navbar-collapse"),
                    is_open=False,
                    navbar=True,
                ),
            ])
        ],
            className='mb-3',
            color="#032A3B",
            dark=True,
        )

    def events(self) -> None:
        pass
