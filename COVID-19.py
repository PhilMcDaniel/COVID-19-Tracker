# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

import pandas as pd
import matplotlib.pyplot as plt

#read csv into dataframe
data = pd.read_csv(r'C:\Users\mcdan\Documents\GitHub\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv')

#filter datafrom for USA
usd = data[data["Country/Region"]=="US"]
usd

