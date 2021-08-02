import pandas as pd
import requests
from io import StringIO
import plotly.graph_objs as go
from plotly.offline import plot

url = "https://docs.google.com/spreadsheets/d/1qkTiPLBIpL05a6WS4qq1AwNmj6nPDGIAb9QzWphXx_s/export?format=csv&gid=0"
r = requests.get(url)
csv_string = r.content.decode('utf-8')
df = pd.read_csv(StringIO(csv_string))
df.to_csv('./data.csv', index=False)
starttime = '2021-07-21 20:00'

df['dttm'] = pd.to_datetime(df['Timestamp'])

df=df[df['dttm']>starttime].copy()

data1 = []
data1.append(go.Scatter({
	'x':df['dttm'],
	'y':df['SG'],
	'name':'actual',
	'mode':'markers'
}))
data1.append(go.Scatter({
	'x':df['dttm'],
	'y':df['SG'].ewm(com=5).mean(),
	'name':'rolling'
}))
plot(data1, filename='specific_gravity.html')

data2 = []
data2.append(go.Scatter({
	'x':df['dttm'],
	'y':df['Temp']
}))
plot(data2, filename='temperature.html')
