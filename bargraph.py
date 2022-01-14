import pandas as panda
import plotly_express as plot

data=panda.read_csv("data.csv")

bars=plot.bar(data,x="Country",y="InternetUsers",color="Population",title="Countries Capital Income")

bars.show()
