from dash import Dash, html
import dash_bootstrap_components as dbc
from components.navbar import NavbarComponent
from components.body import BodyComponent

app = Dash(name=__name__, external_stylesheets=[
           dbc.themes.FLATLY])

app.layout = html.Div([
    NavbarComponent().layout,
    BodyComponent().layout
])


if __name__ == '__main__':
    app.run_server(debug=True)
