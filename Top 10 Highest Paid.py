from numpy import dtype
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from pandas.core.frame import DataFrame

# Parsing the data from the csv file
df = pd.read_csv('nba_2016_2017_100.csv', header=0,)
# Deleting empty spaces
df = df.rename(columns=lambda x: x.strip())
# Sorting by salary, descending
df = df.sort_values(by= "SALARY_MILLIONS", ascending = False)

df = df.head(10)


# Preparing data
data = [go.Bar(x=df['PLAYER_NAME'], y=df['SALARY_MILLIONS'])]

# Preparing layout
layout = go.Layout(title='Top 10 Highest Paid Players (2016-2017)', xaxis_title="Player", yaxis_title="Salary (Millions)")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Top 10 Highest Paid Players.html')