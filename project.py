import random
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("/content/PhoneRatings.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Average Rating on Amazon"], show_hist=False)
fig.show()
