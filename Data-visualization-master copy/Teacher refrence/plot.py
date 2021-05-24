import pandas as pd
import plotly.express as px

df = pd.read_csv("line_chart_csv")
fig = px.line(df,x="Year",y="Per capita income", color="Country",
                    title="per Capita")
fig.show()               