import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('Food_price_indices_data_jul.csv')
After2005 = df[192:]
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='WOW I\'m making a webpage!',
        style={'text-align': 'center',
                'color': 'rgb(199,0,57)',
                'background-color': 'rgb(62,60,60)'
                }),

    html.Div(
    children='''
        Dash: A web application framework for Python.
    '''),
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
