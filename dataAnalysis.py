import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
print(df.groupby("level",as_index = False)["attempt"].mean())

fig = px.scatter(df.groupby("level",as_index = False)["attempt"].mean(),y = "level",x= "attempt",size = "attempt",color="attempt")
fig.show()