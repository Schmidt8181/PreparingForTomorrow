import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pystan
import pyflux as pf

url = 'https://raw.githubusercontent.com/Schmidt8181/ThinkfulCapstone/master/data/Food_price_indices_data_jul.csv'
df = pd.read_csv(url)
indexed_df = clean_food_data.set_index(['Date'])
train = indexed_df.loc['1990':'2016']
test = indexed_df.loc['2017':'2018']
After2005 = df[192:].copy()
After2005['Date'] =pd.to_datetime(After2005['Date'])
After2005['Year'] = After2005['Date'].dt.year

#After2005.head()


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
        dcc.Graph(id='forecast_graph',
            style={'width': '600', 'display': 'inline-block'})
            ]),
    #html.Div(children=[
        #dcc.Slider(
            #id='year_slider',
            #min=After2005['Year'].min(),
            #max=After2005['Year'].max(),
            #value=After2005['Year'].min(),
            #step=None,
            #marks={str(year): str(year) for year in After2005['Year'].unique()}),



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
    [Input(component_id='drop_down', component_property='value')]
)
def update_output_div2(drop_down):
    temp_df = pd.DataFrame()
    #temp_df['ds'] = After2005.Date
    #temp_df['y'] = After2005[drop_down]
    model = pf.ARIMA(data=temp_df, target=drop_down, ar=1, integ=1, ma=12, family=pf.Normal())
    fitted = model.fit("M-H")
    #future = m.make_future_dataframe(periods=60, freq="M")
    forecast = fitted.predict(h=12)
    return {'data':[
                    {'x': forecast.date, 'y': forecast.drop_down, 'type':'line', 'name': drop_down}
    ],
            'layout': go.Layout(
                xaxis={'title': "Month"},
                yaxis={'title': drop_down}
            )}

if __name__ == '__main__':
    app.run_server(debug=True)
