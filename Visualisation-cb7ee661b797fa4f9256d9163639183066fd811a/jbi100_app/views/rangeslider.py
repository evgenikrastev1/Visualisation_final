from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd


class RangeSlider(html.Div):
    def __init__(self, name, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        df_date = self.df[["date"]]

        date_group = df_date.groupby(["date"])

        # days_num -> get the the number of days between them
        days_num = len(date_group)

        # date_min -> get the smallest date
        date_min = df_date["date"].min()

        # date_max -> get the biggest date
        date_max = df_date["date"].max()

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.RangeSlider(
                    id="date-range-slider",
                    min=1,
                    max=days_num,
                    value=[121, 182], # [1, days_num],
                    step=1,
                    allowCross=False,
                    included=True,
                    marks={
                        1:   '1/01/2019', #date_min
                        32:  '1/02/2019',
                        60:  '1/03/2019',
                        91:  '1/04/2019',
                        121: '1/05/2019',
                        152: '1/06/2019',
                        182: '1/07/2019',
                        213: '1/08/2019',
                        244: '1/09/2019',
                        274: '1/10/2019',
                        305: '1/11/2019',
                        335: '1/12/2019',
                        days_num: date_max # 365: '31-12-2019'
                    },
                )
            ],
        )


    def update(self):
        return None
