# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'

data = pd.read_csv(url)
#data
# drop columns so melt() works
data = data.drop(columns = ['UID','iso2','iso3','code3','FIPS','Admin2','Province_State','Lat','Long_','Combined_Key'])
# data

# need to get this to work correctly
data = pd.melt(data,id_vars = ['Country_Region'],var_name = 'Date',value_name = 'Cases')
# data
#convert data type
data["Date"] = pd.to_datetime(data["Date"])

# roll data up to 1 row per day for all of US
rolleddata = data.groupby(['Country_Region','Date'],as_index=False).sum('Cases')
#rolleddata

# add new column that does subtraction from previous row to get deltas
rolleddata['New Cases'] = rolleddata.Cases.diff()
#rolleddata

plt.bar(rolleddata['Date'],rolleddata['New Cases'],align='center')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.ticklabel_format(axis="y",style="plain")
plt.title("Daily New Cases - US")
plt.show()