# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#url for raw data
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

#read csv into dataframe
data = pd.read_csv(url)
# data

#move columns to rows using melt
data = pd.melt(data,id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'],var_name = 'Date',value_name = 'Cases')

#convert data type
data["Date"] = pd.to_datetime(data["Date"])

#filter out data where the province/state != NaN. These rows are from colonies and not the main country
data = data[~((data["Country/Region"]=="United Kingdom") & (data["Province/State"].notna()))]
# data

#roll data up to 1 row per Country/Region. Some countries have the data split by province
rolleddata = data.groupby(['Country/Region','Lat','Long','Date'],as_index=False).sum('Cases')
# rolleddata

#filter datafrom for USA & Italy
us = rolleddata[rolleddata["Country/Region"]=="US"]
italy = rolleddata[rolleddata["Country/Region"]=="Italy"]
uk = rolleddata[rolleddata["Country/Region"]=="United Kingdom"]


#get just the dates
datesus = us['Date']
datesitaly = italy['Date']
datesuk = uk['Date']

#get just the values
valus = us["Cases"]
valitaly = italy["Cases"]
valuk = uk["Cases"]


plt.plot(datesus.values,valus.values,label = 'US')
plt.plot(datesitaly.values,valitaly.values,label = 'Italy')
plt.plot(datesuk.values,valuk.values,label = 'United Kingdom')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.ticklabel_format(axis="y",style="plain")
plt.title("COVID-19 Cases Over Time")
plt.legend()
plt.show()

