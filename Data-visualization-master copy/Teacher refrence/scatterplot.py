import pandas as pd
import plotly.express as px

df = pd.read_csv("data.cvs")
fig = px.scatter(df, x="population", y="Per capita",
                size="Percentage",color="Country",
                size_max = 60)

fig.show()                 
