# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#url for raw data
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'


#read csv into dataframe
data = pd.read_csv(url)
#df = pd.DataFrame(data=data)

#country = df['Country/Region']
#print(country)

#filter datafrom for USA & Italy
us = data[data["Country/Region"]=="US"]
italy = data[data["Country/Region"]=="Italy"]

#move columns to rows using melt
pvtus = pd.melt(us,id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'],var_name = 'Date',value_name = 'Deaths')
pvtitaly = pd.melt(italy,id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'],var_name = 'Date',value_name = 'Deaths')
#pvtus

#convert date column to date datatype
pvtus["Date"] = pd.to_datetime(pvtus["Date"])
pvtitaly["Date"] = pd.to_datetime(pvtitaly["Date"])



#get just the dates
datesus = pvtus['Date']
datesitaly = pvtitaly['Date']

#get just the values
valus = pvtus['Deaths']
valitaly = pvtitaly['Deaths']

plt.plot(datesus.values,valus.values,label = 'US Deaths')
plt.plot(datesitaly.values,valitaly.values,label = 'Italy Deaths')
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.ticklabel_format(axis="y",style="plain")

plt.legend()
plt.show()