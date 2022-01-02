import pandas as pd
import plotly.express as px

data=pd.read_csv("c103/data.csv")
fig=px.scatter(data,x="date",y="cases",color="country",symbol="country")
fig.show()