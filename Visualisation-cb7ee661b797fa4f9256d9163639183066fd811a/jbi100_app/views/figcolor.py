from jbi100_app.main import app

from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json
from itertools import chain
from plotly import graph_objects as go

from ..config import parameter_figcolor_select_list
from jbi100_app.data import get_range_data


class FigColor(html.Div):
    def __init__(self, name, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = "speed_limit"
        self.feature_y = "number_of_vehicles"
        self.color = "number_of_casualties"
        self.facet_col = "day_of_week"

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],
        )


    # chosen_date_range - provides two index values in a list (about start date and end date) from 1 to 365 including
    def update(self, selection, chosen_date_range):
        #clear the file from NaN values
        df = self.df.dropna()
        df1 = get_range_data(df, chosen_date_range)
        #df1 = df1.head(200000)

        # Instantiate custom views

        if selection == parameter_figcolor_select_list[0]:
            print("'One animated scatter' is chosen")

            fig_scatter = px.scatter(
         		df1, x="number_of_casualties", y="number_of_vehicles", animation_frame="day_of_week",
         		animation_group="accident_index", size="road_type", color="speed_limit",
         		hover_name="accident_reference",
         		range_x=[0, 15], range_y=[0, 25],
    			title="Relation between the number of vehicles, causalities and speed limit in every day of the week")
            self.fig = fig_scatter

        elif selection == parameter_figcolor_select_list[1]:
            print("'Scatter for every week day' is chosen")

            #Create multi scatter plot that is part of animation plot
            #Code taken from plotply
            fig_scatter_group = px.scatter(
                df1, x="speed_limit", y="number_of_vehicles", color="number_of_casualties", facet_col="day_of_week",
    			labels={
    				"speed_limit": "Speed limit",
    				"number_of_vehicles": "Number of vehicles",
    				"number_of_casualties": "Number of causalities",
    				"day_of_week": "Day of the week"
    			},
    			title="Relation between the number of vehicles, causalities and speed limit in every day of the week",
    			facet_col_wrap=4)

            #Create lines to show any correlation
            reference_line = go.Scatter(x=[1, 6],
            							y=[1, 10],
            							mode="lines",
            							line=go.scatter.Line(color="gray"),
            							showlegend=False, )
            #Add the lines to the charts
            fig_scatter_group.add_trace(reference_line, row=1, col=1)
            fig_scatter_group.add_trace(reference_line, row=1, col=3)
            self.fig = fig_scatter_group

        else:
            print("Scatter is not chosen")
            self.fig = None


        #Animation plot
        #Part of the code is from https://plotly.com/python/animations/
        animations = {
        	'One animated scatter': px.scatter(
         		df1, x="number_of_casualties", y="number_of_vehicles", animation_frame="day_of_week",
         		animation_group="accident_index", size="road_type", color="speed_limit",
         		hover_name="accident_reference",
         		range_x=[0, 15], range_y=[0, 25],
    			title="Relation between the number of vehicles, causalities and speed limit in every day of the week"),
        	'Scatter for every week day': self.fig,
        }

        return self.fig
