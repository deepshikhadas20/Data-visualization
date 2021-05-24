import pandas as pd
import plotly.express as px

df = pd.read_csv("data.cvs")
fig = px.bar(df, x="Country",y="InternetUser")
fig.show() 