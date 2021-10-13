import dash 
import pandas as pd
import datetime as dt 
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

import plotly 
import plotly.express as px 


df = pd.read_csv("https://raw.githubusercontent.com/Physicalpixel/Assessments/main/Assessment_2/data_bind.csv")
print(df) 

app = dash.Dash(__name__)



app.layout = html.Div([

        html.H1(""),  
        html.H1("Stocks Trend", style={'text-align': 'center', "font-family":"Arial Rounded MT Bold, monospace"}),
         dcc.Checklist(
                id='my_checklist',                      # used to identify component in callback
                options=[
                     {"label": "ABB", "value": "ABB"},
                     {"label": "Reliance", "value": "Reliance"},
                     {"label": "Infy", "value": "Infy"},
                     {"label": "ICICIBANK", "value": "ICICIBANK"}
                ],
                value=["ABB"]  
            ),
         
        dcc.Dropdown(id="slct_symb",
                 options=[
                     {"label": "ABB", "value": "ABB"},
                     {"label": "Reliance", "value": "Reliance"},
                     {"label": "Infy", "value": "Infy"},
                     {"label": "ICICIBANK", "value": "ICICIBANK"}],
                 multi=False,
                 value="ABB",
                 style={'width': "40%" , 'text-align': 'center', "font-family":"Arial Rounded MT Bold, monospace"}
                 ),

    html.Br(),

    dcc.Graph(id='graph', figure={}),
],
style={'width': '70%','padding-left':'15%', 'padding-right':'10%'}
)

@app.callback(    
     Output(component_id='graph', component_property='figure'),
    [Input(component_id='slct_symb', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))
    dff = df.copy()
    dff = dff[dff["Symbol"] == option_slctd]
    
    fig = px.line(
        data_frame=dff,
            x="Date",
            y="Close",
            template='plotly_dark',
            color_discrete_sequence=["yellow"],
            hover_data=["Date", "Open", "High", "Low", "Close"]
    )
    fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Price",
    legend_title="Trend",
    font=dict(
        family="Arial Rounded MT Bold, monospace",
        size=18,
        color="white"
    ),
    hoverlabel=dict(
        bgcolor="black",
        font_size=14,
        font_family="tahoma, monospace"
    )
)
    
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)



