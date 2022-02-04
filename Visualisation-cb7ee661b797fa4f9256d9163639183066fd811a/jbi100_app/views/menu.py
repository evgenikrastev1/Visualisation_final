from dash import dcc, html
from ..config import parameter_per_val_menu_list
from ..config import parameter_color_menu_list
from ..config import parameter_figcolor_select_list


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card"
    )


# two menus for stackbar graph located on the same row
def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[

            html.Div([
                html.Div(
                    id="left-column",
                    className="four columns",
                    children=[
                        html.Label("Parameter per value", style={"textAlign": "center"}),
                        dcc.Dropdown(
                            id="select-parameter-per-val-menu",
                            options=[{"label": i, "value": i} for i in parameter_per_val_menu_list],
                            value=parameter_per_val_menu_list[13],
                            clearable=False,
                        ),
                    ], style={'display': 'inline-block'}
                ),

                html.Br(),

                html.Div(
                    id="right-column",
                    className="four columns",
                    children=[
                        html.Label("Parameter color", style={"textAlign": "center"}),
                        dcc.Dropdown(
                            id="select-parameter-color-menu",
                            options=[{"label": i, "value": i} for i in parameter_color_menu_list],
                            value=parameter_color_menu_list[2],
                            clearable=False,
                        ),
                    ], style={'display': 'inline-block'}
                ),
            ]),

        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]


# menu for figure colors graph
def make_menu_figcolor_layout():
    return html.Div(
        id="middle-control-card",
        children=[
            html.Div(
                id="middle-column",
                className='four columns',
                children=[
                    html.Div([
                            html.Label("Select scatter plot option", style={"textAlign": "center"}),
            				# two scatter plots in different ways
            				dcc.Dropdown(
                				id="selection",
                				options=[{"label": i, "value": i} for i in parameter_figcolor_select_list],
                				value=parameter_figcolor_select_list[0],
                                clearable=False,
            				),
            			]
                    ),
                ], style={"textAlign": "float-left"}
            )
        ]
    )


# menu for matrix graph
def make_menu_matrix_layout():
    return html.Div(
        id="control-card-matrix"
    )
