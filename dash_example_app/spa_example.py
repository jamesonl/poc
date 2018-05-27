import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event
from nltk.corpus import stopwords
import nltk
from nltk import word_tokenize
import plotly.plotly as py
import plotly.graph_objs as go


# global environment variables
plot_bool = False # if False, then don't show a plot
english_stop = set(stopwords.words('english'))

# This is the statement that I will test
# "This is a test of the various stopwords and non-stopwords included within this statement"

# instantiate the instance of the app
app = dash.Dash()

# this denotes the structure of the application in 3 sections:
#   - my html Output
#   - callback area to trigger functions
#   - functions to run off of information

# represents the structure of the entire application
app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div'),
    html.Div(id='my-div2'),
    html.Div(id='my-div3'),
    dcc.Graph(
        id='graph'
        # style={'height': '60vh'}
    )
])


# section for coding the output that will be returned to each of the above
# layout breakouts
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

@app.callback(
    Output(component_id='my-div2', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'Your string is "{}" characters long...'.format(len(input_value))


@app.callback(
    Output(component_id='my-div3', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    word_count = word_tokenize(input_value)
    non_stop = len([y for y in word_count if y not in english_stop])
    stop_words = len([x for x in word_count if x in english_stop])
    return 'Words: ' + str(len(word_count)) + '; Stop:' + str(stop_words) + '; Non-Stop":' + str(non_stop)

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    word_count = word_tokenize(input_value)
    non_stop = len([y for y in word_count if y not in english_stop])
    stop_words = len([x for x in word_count if x in english_stop])

    data = [go.Bar(
            x=['Stop', 'Non-Stop', 'Words'],
            y=[stop_words, non_stop, len(word_count)]
    )]

    return {'data': data}


if __name__ == '__main__':
    app.run_server()
