import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('Food_price_indices_data_jul.csv')
After2005 = df[192:]
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Thinkful DataScience Final Capstone',
        style={'text-align': 'center'}),
    html.Div(
    children='''
        In this capstone, I would like to build a dashboard as a proof of concept
        that allows a user to choose a food item from a limited drop down menu
        that will then show them the recent local prices of said food item and forecast
        if that item will be going up or down in price. Project is still pending approval.
    '''),
    html.Div(children=[
        dcc.Dropdown(
        options=[
            {'label': 'Foo', 'value': 'foo'},
            {'label': 'Bar', 'value': 'bar'},
            {'label': 'Foo2', 'value': 'foo2'}
            ],
            value='Foo')]),
    html.Div(children=[
        dcc.Graph(id='MeatSugar-graph',
            figure={
                'data': [
                    {'x': After2005.Date, 'y': After2005['Meat Price Index'], 'type': 'line', 'name': 'Meat Price Index'},
                    {'x': After2005.Date, 'y': After2005['Sugar Price Index'], 'type': 'line', 'name': 'Sugar Price Index'}
                    ],
                'layout': {'title': 'Dash Data Visualization WOO!'}
                    },
            style={'width': '600', 'display': 'inline-block'}),
        dcc.Graph(id='DairyOilsCereals-graph',
            figure={
                'data': [
                    {'x': After2005.Date, 'y': After2005['Dairy Price Index'],
                    'type': 'line', 'name': 'Dairy Price Index'},
                    {'x': After2005.Date, 'y': After2005['Oils Price Index'],
                    'type': 'line', 'name': 'Oils Price Index'},
                    {'x': After2005.Date, 'y': After2005['Cereals Price Index'],
                    'type': 'line', 'name': 'Cereals Price Index'},
                    ],
                'layout': {'title': 'Dash Data Visualization 2 WOO WOO!'}
                    },
            style={'width': '600', 'display': 'inline-block'}),
        ], style={'display': 'inline-block'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
