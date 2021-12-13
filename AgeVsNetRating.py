from numpy import dtype
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from pandas.core.frame import DataFrame

# Parsing the data from the csv file
df = pd.read_csv('nba_2016_2017_100.csv', header=0,)
# Deleting empty spaces
df = df.rename(columns=lambda x: x.strip())

df = df.sort_values(by= "AGE", ascending = False)

# Preparing data
data =[ 
       go.Scatter(x=df['AGE'],
               y=df['NET_RATING'],
               text=df['PLAYER_NAME'],
                mode = 'markers',
                marker_size= 25)
                ]

# Preparing layout
layout = go.Layout(title='Player Age vs Net Rating (2016 - 2017)', xaxis_title="Player Age",
                   yaxis_title="Player Rating", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='AgeVersusNetRating.html')