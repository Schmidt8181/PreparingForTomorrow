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
        dcc.Dropdown(id='drop_down'
        options=[
            {'label': 'All', 'value': 'Global_Index'},
            {'label': 'Oil', 'value': 'Oil_Index'},
            {'label': 'Cereal', 'value': 'Cereal_Index'},
            {'label': 'Sugar', 'value': 'Sugar_Index'},
            {'label': 'Dairy', 'value': 'Dairy_Index'},
            {'label': 'Meat', 'value': 'Meat_Index'},

            ],
            value='')]),

])
@app.callback(
    Output(component_id='graphs', component_property='children'),
    [Input(component_id='drop_down', component_property='value')]
)
def update_output_div(input_value):
    return html.Div(children=[id='graphs',
        dcc.Graph(id='current',
            figure={
                'data': [
                    {'x': After2005.Date, 'y': (callback input), 'type': 'line', 'name': 'Meat Price Index'}
                    ],
                'layout': {'title': 'Current Prices'}
                    },
            style={'width': '600', 'display': 'inline-block'}),
        dcc.Graph(id='predicted',
            figure={
                'data': [
                    {'x': , 'y': ,
                    'type': 'line', 'name': 'Predicted Prices'}
                    ],
                'layout': {'title': 'Price Forecast'}
                    },
            style={'width': '600', 'display': 'inline-block'}),
        ], style={'display': 'inline-block'})


if __name__ == '__main__':
    app.run_server(debug=True)
