import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Whitehat/DataScience/P103/Copy+of+data+-+data.csv")

#fig = px.scatter(df, x = 'Population', y = 'Per capita')
fig = px.scatter(df, x = 'date', y = 'cases', size = 'cases', color = 'country')
fig.show()