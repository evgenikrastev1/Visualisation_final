from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.menu import make_menu_figcolor_layout
from jbi100_app.views.stackbar import Stackbar
from jbi100_app.views.rangeslider import RangeSlider
from jbi100_app.views.figcolor import FigColor

from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
from jbi100_app.data import read_data


if __name__ == '__main__':

    # read database form csv-file
    df_g = read_data()


    # Instantiate custom views
    stackbar1    = Stackbar("Stackbar", 'road type', 'day of week', df_g)

    rangeslider1 = RangeSlider("Date Range Slider", df_g)

    figcolor1    = FigColor("Scatter Plot", df_g)



    app.layout = html.Div(
        id="app-container",
        children=[
            html.H5("Visualization dashboard", style={"textAlign": "center"}),

            # tho menus for stackbar located on the same row
            html.Div(
                className="twelve columns",
                children=make_menu_layout(),
                style={"display": "inline-block"}
            ),

            # stackbar graph and below it a date range slider
            html.Div(
                className="twelve columns",
                children=[
                    stackbar1,
                    rangeslider1
                ],
                style={"display": "inline-block", "textAlign": "center"}
            ),

            # menu for figure colors graph
            html.Div(
                className="twelve columns",
                children=make_menu_figcolor_layout(),
                style={"display": "inline-block"}
            ),

            # figure colors graph
            html.Div(
                className="twelve columns",
                children=[
                    figcolor1,
                ],
                style={"display": "inline-block", "textAlign": "center"}
            ),
        ], className='row'
    )

    # Define interactions

    # interaction for stackbar graph
    @app.callback(
        Output(stackbar1.html_id, "figure"), [
        Input("select-parameter-per-val-menu", "value"),
        Input("select-parameter-color-menu", "value"),
        Input("date-range-slider", "value")
    ])
    def update_stackbar_1(param_per_val_name, param_color_name, chosen_date_range):
        return stackbar1.update(param_per_val_name, param_color_name, chosen_date_range)


    # interaction for date range slider
    @app.callback(
        Output("output-container-date-range-slider", "children"), [
        Input("date-range-slider", "value")
    ])
    def update_output(value):
        return 'Selected "{}"'.format(value)


    # interaction for figure color graph
    @app.callback(
        Output(figcolor1.html_id, "figure"), [
        Input("selection", "value"),
        Input("date-range-slider", "value")
    ])
    def update_figcolor_1(selection, chosen_date_range):
        return figcolor1.update(selection, chosen_date_range)



    app.run_server(debug=False, dev_tools_ui=False)
