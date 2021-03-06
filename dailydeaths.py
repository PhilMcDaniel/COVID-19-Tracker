# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'

       
data = pd.read_csv(url)
#data
# drop columns so melt() works
data = data.drop(columns = ['Population','UID','iso2','iso3','code3','FIPS','Admin2','Province_State','Lat','Long_','Combined_Key'])
#data

#turn date rows into columns =
data = pd.melt(data,id_vars = ['Country_Region'],var_name = 'Date',value_name = 'Deaths')
#data

#convert data type
data["Date"] = pd.to_datetime(data["Date"])

# roll data up to 1 row per day for all of US
rolleddata = data.groupby(['Country_Region','Date'],as_index=False).sum('Deaths')
#rolleddata

# add new column that does subtraction from previous row to get deltas
rolleddata['New Deaths'] = rolleddata.Deaths.diff()
#rolleddata

#add column for rolling average
rolleddata['Roll'] = rolleddata['New Deaths'].rolling(window = 7).mean()


# add column that is date integer
rolleddata['Date int'] = mdates.date2num(rolleddata['Date'])

#top 10 days with new Deaths. will be used to annotate later
topdeaths = rolleddata.sort_values(by='New Deaths',ascending = False).head(3)
#convert to int to get rid of .0 from float
topdeaths['New Deaths'] = topdeaths['New Deaths'].astype(np.int64)
#topdeaths.dtypes

#get max date for annotation
maxdate = rolleddata.sort_values(by='Date',ascending = False).head(1)
maxdate = maxdate['Date']
#maxdate


# get important dates for annotation
thanksgiving = rolleddata[rolleddata['Date'] =='2020-11-26']
nationalemergency = rolleddata[rolleddata['Date'] =='2020-03-13']
firstvaccination = rolleddata[rolleddata['Date'] =='2020-12-14']
memorialday = rolleddata[rolleddata['Date'] =='2020-05-25']
laborday = rolleddata[rolleddata['Date'] =='2020-09-07']

plt.bar(rolleddata['Date'],rolleddata['New Deaths'],align='center')
plt.plot(rolleddata['Date'],rolleddata['Roll'],color='orange',label = '7 Day Rolling Average')
plt.legend(loc = 'upper left')
plt.xlabel('Date')
plt.ylabel('New Deaths')
plt.ticklabel_format(axis="y",style="plain")
plt.title("Daily New Deaths - US")
# https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/annotation_demo.html
plt.annotate('Thanksgiving'
            ,xy=(thanksgiving['Date int'],0),xycoords = 'data'
            ,xytext=(0,-40),textcoords='offset pixels'
            ,arrowprops=dict(facecolor='black', shrink=0.05,width = 1,headwidth = 8)
            ,horizontalalignment='center', verticalalignment='top'
            )
plt.annotate('National Emergency Declared'
            ,xy=(nationalemergency['Date int'],0),xycoords = 'data'
            ,xytext=(0,-40),textcoords='offset pixels'
            ,arrowprops=dict(facecolor='black', shrink=0.05,width = 1,headwidth = 8)
            ,horizontalalignment='center', verticalalignment='top'
            )
plt.annotate('First US Vaccination'
            ,xy=(firstvaccination['Date int'],0),xycoords = 'data'
            ,xytext=(0,-60),textcoords='offset pixels'
            ,arrowprops=dict(facecolor='black', shrink=0.05,width = 1,headwidth = 8)
            ,horizontalalignment='center', verticalalignment='top'
            )
plt.annotate('Memorial Day'
            ,xy=(memorialday['Date int'],0),xycoords = 'data'
            ,xytext=(0,-40),textcoords='offset pixels'
            ,arrowprops=dict(facecolor='black', shrink=0.05,width = 1,headwidth = 8)
            ,horizontalalignment='center', verticalalignment='top'
            )
plt.annotate('Labor Day'
            ,xy=(laborday['Date int'],0),xycoords = 'data'
            ,xytext=(0,-40),textcoords='offset pixels'
            ,arrowprops=dict(facecolor='black', shrink=0.05,width = 1,headwidth = 8)
            ,horizontalalignment='center', verticalalignment='top'
            )

#annotate the top daily case days using loop
for index, row in topdeaths.iterrows():
    newdeaths = row['New Deaths']
    newcasedateint = row['Date int']
    date = row['Date']
    plt.annotate(f"{newdeaths}"
                ,xy=(newcasedateint,newdeaths),xycoords = 'data'
                ,xytext=(newcasedateint,newdeaths+100),textcoords='data'
                ,horizontalalignment='center', verticalalignment='top'
                ,fontsize = 'small'
                )

#add annotation in top middle for date of latest data
plt.annotate(f"Latest data is from: {maxdate.dt.strftime('%Y-%m-%d').values}"
            ,xy=(.5,1),xycoords = 'axes fraction'
            ,xytext=(-10,-10),textcoords='offset pixels'
            ,horizontalalignment='center', verticalalignment='top'
            ,fontsize = 'small'
            )

#get current figure
figure = plt.gcf()

#update current figure size before saving
figure.set_size_inches(16,9)

#save figure
plt.savefig("USDailyDeaths.png")

#show figure
plt.show()
