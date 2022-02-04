import plotly.express as px
import pathlib
import pandas as pd
from datetime import datetime


def read_data():
    # Read data

    THIS_FILE_PATH = pathlib.Path(__file__).parent

    DATASETS_PATH = THIS_FILE_PATH.joinpath("../datasets").resolve()

    # read data form csv-file
    df = pd.read_csv(DATASETS_PATH.joinpath('accidents.csv'), low_memory=False)
    return df



# Any further data preprocessing can go her
def get_range_data(df, chosen_date_range):

    # get unique list of dates from dataframe in string format
    dates_list_unique_str = df["date"].unique().tolist()

    # convert date form string to datetime format
    dates_list_unique = []
    for i in range(len(dates_list_unique_str)):
        date_i = datetime.strptime(dates_list_unique_str[i], "%d/%m/%Y")
        # put to unique list of dates in datetime format
        dates_list_unique.append(date_i)

    # sort unique list of dates in datetime format
    dates_list = sorted(dates_list_unique)

    # range slider gives min_date index = 1
    if chosen_date_range[0] <= 0:
        chosen_date_range[0] = 1
        print("min_date index is out of range: " + chosen_date_range[0], ". Use 1 instead.")
    # d1 - start date
    d1 = dates_list[chosen_date_range[0]-1]

    # range slider gives max_date index = 365
    if chosen_date_range[1] > len(dates_list):
        chosen_date_range[1] = len(dates_list)
        print("max_date index is out of range: " + chosen_date_range[1], ". Use ", len(dates_list), " instead.")
    # d1 - end date
    d2 = dates_list[chosen_date_range[1]-1]

    # get data in the required date interval only
    df_date = df.copy()
    df_date = df_date[(pd.to_datetime(df_date['date']) >= d1) & (pd.to_datetime(df_date['date']) <= d2)]
    if df_date.empty:
        print("There are no data to be visualized from ", d1, " to ", d2)

    return df_date
