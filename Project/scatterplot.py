import pandas as pd
import plotly_express as  px

df=pd.read_csv("data.csv")
fig=px.scatter(df,x="date",y="Number of caases",size="Percentage",color="Country",size_max=60)
fig.show()