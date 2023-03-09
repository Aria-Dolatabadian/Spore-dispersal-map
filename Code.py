import plotly.express as px
import pandas as pd
df = pd.read_csv("Data.csv")

fig = px.scatter_polar(df, r = "distance" , theta="direction", size = "load")
fig.update_layout(
    title = "Spore dispersal",
    font_size = 20,
    showlegend = True,
    polar = dict(
      bgcolor = "rgb(217, 209, 189)",
      angularaxis = dict(
        linewidth = 3,
        showline=True,
        linecolor='black'
      ),
      radialaxis = dict(
        side = "clockwise",
        showline = True,
        linecolor = "pink",
        linewidth = 3,
        gridcolor = "white",
        gridwidth = 3,
      )
    ),
    paper_bgcolor = "rgb(255, 255, 255)"
)
fig.show()
