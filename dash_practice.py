import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pystan
from fbprophet import Prophet

url = 'https://raw.githubusercontent.com/Schmidt8181/ThinkfulCapstone/master/data/Food_price_indices_data_jul.csv'
df = pd.read_csv(url)

After2005 = df[192:]
After2005['Date'] =pd.to_datetime(After2005['Date'])



app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Thinkful DataScience Final Capstone',
        style={'text-align': 'center'}),
    html.Div(
    children='''
        In this capstone, I would like to build a dashboard as a proof of concept
        that allows a user to choose a food item from a limited drop down menu
        that will then show them the recent local prices of said food item and forecast
        if that item will be going up or down in price.
    '''),
    html.Div(children=[
        dcc.Dropdown(id='drop_down',
        options=[
            {'label': 'Food Price Index', 'value': 'Food Price Index'},
            {'label': 'Oils Price Index', 'value': 'Oils Price Index'},
            {'label': 'Cereals Price Index', 'value': 'Cereals Price Index'},
            {'label': 'Sugar Price Index', 'value': 'Sugar Price Index'},
            {'label': 'Dairy Prince Index', 'value': 'Dairy Price Index'},
            {'label': 'Meat Price Index', 'value': 'Meat Price Index'},
            ],
            value='Food Price Index'),
         dcc.Graph(id='graphs',
            style={'width': '600', 'display': 'inline-block'}),
         dcc.Graph(id='forcast_graph',
            style={'width': '600', 'display': 'inline-block'}),
         dcc.Slider(
            id='year_slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            step=None,
            marks={str(year): str(year) for year in df['year'].unique()}
    )
])
])
])

@app.callback(
    Output(component_id='graphs', component_property='figure'),
    [Input(component_id='drop_down', component_property='value')]
)
def update_output_div(drop_down):
    return {'data':[
                    {'x': After2005.Date, 'y': After2005[drop_down], 'type': 'line', 'name': drop_down},
                    ],
            'layout': go.Layout(
                xaxis={'title': "Month"},
                yaxis={'title': drop_down}
            )
            }
@app.callback(
    Output(component_id='forecast_graph', component_property='figure'),
    [Input(component_id='year_slider', component_property='value')]
)
def update_output_div2(year-slider):
    return #{put forecast stuff in here}

if __name__ == '__main__':
    app.run_server(debug=True)
