# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read csv into dataframe
data = pd.read_csv(r'C:\Users\phil_\OneDrive\Documents\GitHub\COVID-19-DATA\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv')

#filter datafrom for USA & Italy
us = data[data["Country/Region"]=="US"]
italy = data[data["Country/Region"]=="Italy"]

#move columns to rows using melt
pvtus = pd.melt(us,id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'],var_name = 'Date',value_name = 'Cases')
pvtitaly = pd.melt(italy,id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'],var_name = 'Date',value_name = 'Cases')
#pvtus

#convert date column to date datatype
pvtus["Date"] = pd.to_datetime(pvtus["Date"])
pvtitaly["Date"] = pd.to_datetime(pvtitaly["Date"])



#get just the dates
datesus = pvtus['Date']
datesitaly = pvtitaly['Date']

#get just the values
valus = pvtus['Cases']
valitaly = pvtitaly['Cases']

plt.plot(datesus.values,valus.values,label = 'US Cases')
plt.plot(datesitaly.values,valitaly.values,label = 'Italy Cases')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.ticklabel_format(axis="y",style="plain")

plt.legend()
plt.show()

