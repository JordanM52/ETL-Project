import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from pandas.core.frame import DataFrame

#Parsing the data from the csv file
df = pd.read_csv("ZillowHomeValues.csv")

# Reorganizing the data into a new dataframe
df = df.groupby(by=['StateName'])

df=df.sort_values(by='2021-01-31', ascending = False)

# Preparing data
data = [go.Bar(x=df['StateName'], y=df['2021-01-31'])]

# Preparing layout
layout = go.Layout(title='Most Popular States to Sell a Property', xaxis_title="States",
                   yaxis_title="Properties For Sale")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='NationalForSale.html')
 