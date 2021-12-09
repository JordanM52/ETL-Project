import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from pandas.core.frame import DataFrame

# Read and Described the data from the csv file
df = pd.read_csv("For-Sale-Inventory.csv")
df.describe()

# Data Cleaning
df.drop(columns=['RegionType'])

# Reorganizing the data into a new dataframe
new_df = df.groupby(['StateName']).reset_index()


new_df = new_df.sort_values(by=[''])


trace1 = go.Bar(x=new_df['Drink_Name'], y=new_df['Unit_Price'],
    name='Unit Price', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['Drink_Name'], y=new_df['Case_Price'],
    name='Case Price', marker={'color': '#9EA0A1'})

data = [trace1, trace2]

layout = go.Layout(title='Prices of the most popular drinks in the United States that are the most expensive', xaxis_title="Drink Names",
    yaxis_title="Prices of Drinks in U.S. Dollars", barmode='stack')

# Creating the graph/plot for the dataframe
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='NationalForSale.html')
