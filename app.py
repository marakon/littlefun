import datetime
import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

q = curl http://egnyte.zendesk.com/api/v2/tickets.json \
  -v -u mosinski@egnyte.com:Tr0l0l0l0!!!!!!

def serve_layout():
    return html.H1('The time is: ' + str(datetime.datetime.now()))

app.layout = serve_layout

app.layout = html.Div([
    html.H1("Support",
    style={
        'textAlign': 'center'
    }),

        html.Div([
            html.H2("dashboard",
            queue,
            style={
                'textAlign': 'right',
                'float': 'left'
            })
        ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)