import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from datetime import datetime
from dateutil.relativedelta import relativedelta
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults


def load_models():
    return {
        "Sugar Price Index": ARIMAResults.load("model/SugarARIMA.pkl"),
        "Meat Price Index": ARIMAResults.load("model/MeatARIMA.pkl"),
        "Dairy Price Index": ARIMAResults.load("model/DairyARIMA.pkl"),
        "Cereals Price Index": ARIMAResults.load("model/CerealsARIMA.pkl"),
        "Oils Price Index": ARIMAResults.load("model/OilsARIMA.pkl")
    }

global model_dict
model_dict = load_models()

df = pd.read_csv('data/indexed_clean_df.csv')
df.head()


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Thinkful Data Science Final Capstone',
        style={'text-align': 'center'}),
    html.Div(
    children='''
        With this forecasting tool you will be able to predict if the price of a kind of food will go up for down and allow for appropriate planning of the near fututre.
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
            value='Meat Price Index'),
        dcc.Graph(id='graphs',
            style={'width': '600', 'display': 'inline-block'}),
        dcc.Graph(id='forecast_graph',
            style={'width': '600', 'display': 'inline-block'})
            ]),

])


@app.callback(
    Output(component_id='graphs', component_property='figure'),
    [Input(component_id='drop_down', component_property='value')]
)
def update_historical_data(drop_down):
    return {'data':[
                    {'x': df.Date, 'y': df[drop_down], 'type': 'line', 'name': drop_down},
                    ],
            'layout': go.Layout(
                xaxis={'title': "Month"},
                yaxis={'title': drop_down}
            )
            }


@app.callback(
    Output(component_id='forecast_graph', component_property='figure'),
    [Input(component_id='drop_down', component_property='value')]
)
def update_forecast_data(drop_down):
    model = model_dict[drop_down]
    forecast, stderr, conf = model.forecast(steps = 3)
    future_dates = ["2018-07-01", "2018-08-01", "2018-09-01"]
    x_dates = range(len(forecast))
    return {'data':[
                    {'x': future_dates, 'y': forecast, 'type':'line', 'name': drop_down}
    ],
            'layout': go.Layout(
                xaxis={'title': "Month"},
                yaxis={'title': drop_down}
            )}

if __name__ == '__main__':
    app.run_server(debug=True)
