import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('/Users/Beba/Food_price_indices_data_jul.csv')
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Holy crap I\'m making a webpage!',
        style={'text-align': 'center',
                'color': 'rgb(199,0,57)',
                'background-color': 'rgb(62,60,60)'
                }),

    html.Div(
    children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id='MeatSugar-graph',
        figure={
            'data': [
                {'x': df.Date, 'y': df['Meat Price Index'], 'type': 'line', 'name': 'Meat Price Index'},
                {'x': df.Date, 'y': df['Sugar Price Index'], 'type': 'line', 'name': 'Sugar Price Index'}
            ],
            'layout': {
                'title': 'Dash Data Visualization WOO!'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
