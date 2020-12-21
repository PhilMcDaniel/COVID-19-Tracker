# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#url for raw data
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'


#read csv into dataframe
data = pd.read_csv(url)
# data

#move columns to rows using melt
data = pd.melt(data,id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'],var_name = 'Date',value_name = 'Deaths')

#convert data type
data["Date"] = pd.to_datetime(data["Date"])

#filter out data where the province/state != NaN. These rows are from colonies and not the main country
data = data[~((data["Country/Region"]=="United Kingdom") & (data["Province/State"].notna()))]
# data

#roll data up to 1 row per Country/Region. Some countries have the data split by province
rolleddata = data.groupby(['Country/Region','Lat','Long','Date'],as_index=False).sum('Deaths')
# rolleddata

#filter datafrom for USA & Italy
us = rolleddata[rolleddata["Country/Region"]=="US"]
italy = rolleddata[rolleddata["Country/Region"]=="Italy"]
uk = rolleddata[rolleddata["Country/Region"]=="United Kingdom"]

plt.plot(us['Date'],us["Deaths"],label = 'US')
plt.plot(italy['Date'],italy["Deaths"],label = 'Italy')
plt.plot(uk['Date'],uk["Deaths"],label = 'United Kingdom')
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.ticklabel_format(axis="y",style="plain")
plt.title("COVID-19 Deaths Over Time")
plt.legend()
plt.show()