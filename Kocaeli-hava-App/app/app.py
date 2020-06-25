# -*- coding: utf-8 -*-
import requests
import calendar
from datetime import datetime
from collections import defaultdict
import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_daq as daq
from statsmodels.tsa.arima_model import ARIMAResults
import pickle

app = dash.Dash()

def Hesapla_PM10(Pm10):
    hki = ""
    if (Pm10>=0 and Pm10<=50):
     hki= 'İyi'
    if (Pm10>=51 and Pm10<=100):
     hki= 'Orta'
    if (Pm10>=101 and Pm10<=260):
     hki= 'Hassas'
    if (Pm10>=261 and Pm10<=400):
     hki= 'Sağlıksız'
    if (Pm10>=401 and Pm10<=520):
     hki= 'Kötü'
    if (Pm10>521):
     hki= 'Tehlikeli'
    return hki


import pandas as pd
import matplotlib.pyplot as plt
import statsmodels as sm

plt.style.use('seaborn')

plt.rcParams['figure.figsize'] = [8,6]

veri = pd.read_csv(r"C:\Users\hlltk\PycharmProjects\guncel\Kocaeli_Orj.csv")
veri.head()
PM10 = veri['Kocaeli-PM10']
Tarih = veri['Tarih']
PM10 = pd.DataFrame(PM10)

veri_PM10 = PM10.join(veri['Tarih'],how='inner')
veri_PM10
veri_PM10["Tarih"] = pd.to_datetime(veri_PM10["Tarih"])

veri_PM10.set_index("Tarih", inplace = True)
import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
# 0 ile 2 arasında herhangi bir değer almak için p, d ve q parametrelerini tanımlayın
p = d = q = range(0, 2)

# Tüm farklı p, q ve q üçlülerini oluşturun
pdq = list(itertools.product(p, d, q))

# Mevsimsel p, q ve q üçüzlerinin tüm farklı kombinasyonlarını oluşturun
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

from statsmodels.tsa.arima_model import ARMA
mod = sm.tsa.statespace.SARIMAX(veri_PM10,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()
#results.save('model.pkl')

print(results.summary())
results.plot_diagnostics(figsize=(15, 12))

from statsmodels.tsa.arima_model import ARIMAResults

loaded = ARIMAResults.load('model.pkl')
print(loaded.params)

predictions = loaded.predict(start='2018-01-01', end='2021-01-01')
print(predictions['2020-06-12'])
now_pred = predictions[pd.datetime.now (). strftime ("%Y-%m-%d")]

#function from plotly example useful for parsing pandas dataframe into dash table.
def make_weather_table( dtf):

    table =[0,html.Tr([
						html.Th(['Day']),html.Th(['Description']),html.Th(['Humidyty']),html.Th(['Temperature']),html.Th(['Wind'])
					])]
    for index, row in dtf.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append( html.Td([ row[i] ]) )
        table.append( html.Tr( html_row ) )

    return table
#openweather api call returns pandas dataframe 
def api_call(input_value="Kocaeli-tr"):
	city = 'Kocaeli'#input_value.replace(" ", "").split(" ")[0]''
	state = 'tr'
	lang='tr'
	key = '005577d079032a62849e242e311dd878' #put api key here
	r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q={},{}&appid={}&lang={}".format(city,state,key,lang))
	data = r.json()

	day = [calendar.day_name[(datetime.strptime(data["list"][i]['dt_txt'].split(" ")[0],'%Y-%M-%d')).weekday()] for i in range(3,36,8)]
	description = [data["list"][i]["weather"][0]['description'] for i in range(3,36,8)]
	temp = [round(data["list"][i]['main']['temp'] * (9/5) - 459.67) for i in range(3,36,8)]
	wind_speed = [data["list"][i]['wind']['speed'] for i in range(3,36,8)]
	humidity = [data["list"][i]['main']['humidity'] for i in range(3,36,8)]
	df = pd.DataFrame(data={'Day':day,'Description':description,'Temperature':temp,'Humidity':humidity,'Wind':wind_speed})
	
	return df

# UI layout 
app.layout = html.Div([

#header
	html.Div([
		html.H1('Kocaeli Hava Parametre Değerleri', style={'font-family': 'Dosis','font-size': '4.0rem','textAlign': 'center'})
	    ]),

#input 
    html.Div([
    	html.P(""),
    	html.Div([dcc.Input(id='Kocaeli',  placeholder="ex Ames,usa", value="Kocaeli", type = "text")
    		])
    	]),   

#output
	html.Div([
    	html.Div(id='742865')

    	]),

	# html.Br(),

	html.Div([

		html.H1('Kocaeli Günlük PM10 Parametre Değerleri', style={'font-family': 'Dosis','font-size': '2.0rem','textAlign': 'left'}),
		daq.Gauge(
			color={
				"gradient": False,
				"ranges": {"green": [0, 50], "yellow": [51, 100], "red": [101, 150]}},

			value=round(now_pred),
			label=Hesapla_PM10(now_pred),
			max=150,
			min=0,

		),

		])#,

	# html.Div([
	# html.Table(make_weather_table(api_call()))
	# ])
    

], className='container')

@app.callback(
	Output(component_id='742865', component_property='children'),
	[Input(component_id='Kocaeli', component_property='value')]
)

#function to update the app
def update_weather(input_value):
	icons =  {"snow":"https://ssl.gstatic.com/onebox/weather/64/snow.png","cloud":"https://ssl.gstatic.com/onebox/weather/64/cloudy.png",
				"rain":"https://ssl.gstatic.com/onebox/weather/64/rain.png","sunny":"https://ssl.gstatic.com/onebox/weather/64/sunny.png",
				"fog":"https://ssl.gstatic.com/onebox/weather/64/fog.png"}
	#app.get_asset_url(r"C:\Users\hlltk\OneDrive\Masaüstü\uzaktanegitim\güncel konulae\resim\ulusalhki.PNG"),
	df = api_call(input_value)

	temp_icon = ["https://www.google.com/search?q=hava+kalitesi+PM10+icon&tbm=isch&ved=2ahUKEwjrsazx5f_pAhWE0oUKHXCFB3wQ2-cCegQIABAA&oq=hava+kalitesi+PM10+icon&gs_lcp=CgNpbWcQA1DAQFi8R2DeSWgAcAB4AIABvwOIAYgKkgEJMC4xLjEuMC4ymAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img&ei=Qk3lXuuIO4SllwTwip7gBw&bih=784&biw=1707#imgrc=TN114ltQ-UKaLM"]
	for key, value in icons.items():
		if key in df.Description[0]:
					temp_icon = icons[key]
	
	input_value = input_value 

	app.layout = html.Div([

		html.H3(input_value,style={"color":'#878787'}),
			html.P(df.Day[0],style={'fontSize':'20px'}),
			html.P(df.Description[0],style={'fontSize':'18px'}),

			html.Div(style={'height': '64px','display':'inline','position': 'relative','width': '64px','margin-top':'-9px'},children = [
						html.Img(src=temp_icon[0]),
						html.P("{}F".format(df.Temperature[0]),style={'fontSize':'36px','display':'inline'})
						]),

		    html.Div(style={"float": "right", 'fontSize': '20px'}, children=[
				html.P("Nem : {}%".format(df.Humidity[0])),
				html.P("Rüzgar : {} mph".format(df.Wind[0])),
			]),



			html.Div(children=[
			dcc.Graph(
		        id='weather_graph',
		         figure=go.Figure(
			        data=[
			            go.Scatter(x=list(df.Day), y=list(df.Temperature), mode='lines+markers',name="temperature"),
			            go.Scatter(x=list(df.Day), y=list(df.Humidity), mode='lines+markers',name='Humidity'),
			            go.Scatter(x=list(df.Day), y=list(df.Wind), mode='lines+markers',name='wind')
			        ],
			        layout=go.Layout(
			            title='Beş Günlük Hava Durumu Tahmini {}'.format(input_value),
			            showlegend=True,
			            margin=go.Margin(l=20, r=0, t=40, b=20)
			        
		        	)
		        ))

		        ]),

			html.Div([
				html.Br(),
				html.Hr(),
				html.P(" {} Hava Bilgileri".format(input_value), style={"textAlign":"center"}),
				html.Table(
					),
				html.Table(
					make_weather_table(df)
				)

				])


		])
	fig = go.Figure(go.Indicator(
		mode="gauge+number+delta",
		value=420,
		domain={'x': [0, 1], 'y': [0, 1]},
		title={'text': "Speed", 'font': {'size': 24}},
		delta={'reference': 400, 'increasing': {'color': "RebeccaPurple"}},
		gauge={
			'axis': {'range': [None, 500], 'tickwidth': 1, 'tickcolor': "darkblue"},
			'bar': {'color': "darkblue"},
			'bgcolor': "white",
			'borderwidth': 2,
			'bordercolor': "gray",
			'steps': [
				{'range': [0, 250], 'color': 'cyan'},
				{'range': [250, 400], 'color': 'royalblue'}],
			'threshold': {
				'line': {'color': "red", 'width': 4},
				'thickness': 0.75,
				'value': 490}}))

	fig.update_layout(paper_bgcolor="lavender", font={'color': "darkblue", 'family': "Arial"})



	return(app.layout)

# external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
#                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
#                 "//fonts.googleapis.com/css?family=Dosis:Medium",
#                 "https://cdn.rawgit.com/plotly/dash-app-stylesheets/0e463810ed36927caf20372b6411690692f94819/dash-drug-discovery-demo-stylesheet.css"]
#
#
# for css in external_css:
#     app.css.append_css({"external_url": css})

if __name__ == '__main__':
	app.run_server(port=8080,debug=True)