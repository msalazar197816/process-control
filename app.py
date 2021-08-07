import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
author="miguel salazar"
app=dash.Dash(__name__)

app.layout=html.Div([
    html.H1('Process Control'),
    html.H2(f'By:{author}')
])



app.run_server(debug=True)