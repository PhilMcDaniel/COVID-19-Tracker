# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

# add column that is date integer
rolleddata['Date int'] = mdates.date2num(rolleddata['Date'])
rolleddata

#filter datafrom for USA & Italy
us = rolleddata[rolleddata["Country/Region"]=="US"]
italy = rolleddata[rolleddata["Country/Region"]=="Italy"]
uk = rolleddata[rolleddata["Country/Region"]=="United Kingdom"]


#get current deaths for annotation
curus = us.sort_values(by='Date',ascending = False).head(1)
curitaly = italy.sort_values(by='Date',ascending = False).head(1)
curuk = uk.sort_values(by='Date',ascending = False).head(1)


plt.plot(us['Date'],us["Cases"],label = 'US')
plt.plot(italy['Date'],italy["Cases"],label = 'Italy')
plt.plot(uk['Date'],uk["Cases"],label = 'United Kingdom')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.ticklabel_format(axis="y",style="plain")
plt.title("COVID-19 Cases Over Time")
plt.legend()
plt.annotate(curus['Cases'].values
            ,xy=(curus['Date int'],curus['Cases']),xycoords = 'data'
            ,xytext=(-10,10),textcoords='offset pixels'
            ,horizontalalignment='center', verticalalignment='top'
            ,fontsize = 'small'
            )
plt.annotate(curitaly['Cases'].values
            ,xy=(curitaly['Date int'],curitaly['Cases']),xycoords = 'data'
            ,xytext=(10,-15),textcoords='offset pixels'
            ,horizontalalignment='center', verticalalignment='top'
            ,fontsize = 'small'
            )
plt.annotate(curuk['Cases'].values
            ,xy=(curuk['Date int'],curuk['Cases']),xycoords = 'data'
            ,xytext=(-10,15),textcoords='offset pixels'
            ,horizontalalignment='center', verticalalignment='top'
            ,fontsize = 'small'
            )



#get current figure
figure = plt.gcf()

#update current figure size before saving
figure.set_size_inches(16,9)

#save figure
plt.savefig("TotalCasesOverTimeByCountry.png")

#show figure
plt.show()