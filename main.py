from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open("rainforest_classifier.pkl", 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

	if request.method == 'POST':
		loc = ['Location_Adelaide', 'Location_Albany', 'Location_Albury', 'Location_AliceSprings', 'Location_BadgerysCreek', 
				'Location_Ballarat', 'Location_Bendigo', 'Location_Brisbane', 'Location_Cairns', 'Location_Canberra', 'Location_Cobar', 
				'Location_CoffsHarbour', 'Location_Dartmoor', 'Location_Darwin', 'Location_GoldCoast', 'Location_Hobart', 'Location_Katherine',
				'Location_Launceston', 'Location_Melbourne', 'Location_MelbourneAirport', 'Location_Mildura', 'Location_Moree', 'Location_MountGambier', 
				'Location_MountGinini', 'Location_Newcastle', 'Location_Nhil', 'Location_NorahHead', 'Location_NorfolkIsland', 
				'Location_Nuriootpa', 'Location_PearceRAAF',
				'Location_Penrith', 'Location_Perth', 'Location_PerthAirport', 'Location_Portland', 'Location_Richmond', 'Location_Sale', 
				'Location_SalmonGums', 'Location_Sydney', 'Location_SydneyAirport', 'Location_Townsville', 'Location_Tuggeranong', 'Location_Uluru',
				'Location_WaggaWagga', 'Location_Walpole', 'Location_Watsonia', 'Location_Williamtown', 'Location_Witchcliffe', 'Location_Wollongong',
				'Location_Woomera']

				
				
		for n in loc:
			n = 0
		Month = float(request.form['Month'])
		location =str(request.form['Location'])

		if (location == 'Adelaide'):
			Location_Adelaide = 1
		elif (location == 'Brisbane'):
			Location_Brisbane = 1
		elif (location == 'Canberra'):
			Location_Canberra = 1
		elif (location == 'Sydney'):
			Location_Sydney = 1
		elif (location == 'Perth'):
			Location_Perth = 1
		else:
			if (location == 'Melbourne'):
				Location_Melbourne = 1
				print("AAAAAAAAAAAAAA")
		print("BBBBBB")
		MinTemp=float(request.form['Minimum_temperature'])
		MaxTemp=float(request.form['Maximum_temperature'])
		Rainfall = float(request.form['Rainfall'])
		Evaporation =float(request.form['Evaporation'])
		Sunshine=float(request.form['Sunshine'])

		winddir=str(request.form['WindGustDir'])
		WindGustDir_S = 0
		WindGustDir_N = 0
		WindGustDir_E = 0
		WindGustDir_W = 0
		WindGustDir_ENE = 0
		WindGustDir_ESE = 0
		WindGustDir_NA = 0
		WindGustDir_NE = 0
		WindGustDir_NNE = 0
		WindGustDir_NNW = 0
		WindGustDir_NW = 0
		WindGustDir_SE = 0
		WindGustDir_SSE  = 0
		WindGustDir_SSW = 0
		WindGustDir_SW = 0
		WindGustDir_WNW = 0
		WindGustDir_WSW = 0
		if winddir == 'S':
			WindGustDir_S = 1
		elif winddir == 'N':
			WindGustDir_N = 1
		elif winddir == 'E':
			WindGustDir_E = 1
		elif winddir == 'W':
			WindGustDir_W = 1
		elif winddir == 'ENE':
			WindGustDir_ENE = 1
		elif winddir == 'ESE':
			WindGustDir_ESE = 1
		elif winddir =='NA':
			WindGustDir_NA = 1
		elif winddir == 'NE':
			WindGustDir_NE = 1
		elif winddir == 'NNE':
			WindGustDir_NNE = 1
		elif winddir == 'NNW':
			WindGustDir_NNW = 1
		elif winddir == 'NW':
			WindGustDir_NW = 1
		elif winddir == 'SE':
			WindGustDir_SE = 1
		elif winddir == 'SSE':
			WindGustDir_SSE = 1
		elif winddir == 'SSW':
			WindGustDir_SSW = 1
		elif winddir == 'SW':
			WindGustDir_SW = 1
		elif winddir == 'WNW':
			WindGustDir_WNW = 1
		else:
			if winddir == 'WSW':
				WindGustDir_WSW = 1
				
		windgustspeed = float(request.form['WindGustSpeed'])
		winddir9am =str(request.form['WindDir9am'])
		WindDir9am_S = 0
		WindDir9am_N = 0
		WindDir9am_E = 0
		WindDir9am_W = 0
		WindDir9am_ENE = 0
		WindDir9am_ESE = 0
		WindDir9am_NA = 0
		WindDir9am_NE = 0
		WindDir9am_NNE = 0
		WindDir9am_NNW = 0
		WindDir9am_NW = 0
		WindDir9am_SE = 0
		WindDir9am_SSE  = 0
		WindDir9am_SSW = 0
		WindDir9am_SW = 0
		WindDir9am_WNW = 0
		WindDir9am_WSW = 0
		if winddir9am == 'S':
			WindDir9am_S = 1
		elif winddir9am == 'N':
			WindDir9am_N = 1
		elif winddir9am == 'E':
			WindDir9am_E = 1
		elif winddir9am == 'W':
			WindDir9am_W = 1
		elif winddir9am == 'ENE':
			WindDir9am_ENE = 1
		elif winddir9am == 'ESE':
			WindDir9am_ESE = 1
		elif winddir9am == 'NA':
			WindDir9am_NA = 1
		elif winddir9am == 'NE':
			WindDir9am_NE = 1
		elif winddir9am == 'NNE':
			WindDir9am_NNE = 1
		elif winddir9am == 'NNW':
			WindDir9am_NNW = 1
		elif winddir9am == 'NW':
			WindDir9am_NW = 1
		elif winddir9am == 'SE':
			WindDir9am_SE = 1
		elif winddir9am == 'SSE':
			WindDir9am_SSE = 1
		elif winddir9am == 'SSW':
			WindDir9am_SSW = 1
		elif winddir9am == 'SW':
			WindDir9am_SW = 1
		elif winddir9am == 'WNW':
			WindDir9am_WNW = 1
		else:
			if winddir9am == 'WSW':
				WindDir9am_WSW = 1
		winddir3pm=str(request.form['WindDir3pm'])
		WindDir3pm_S = 0
		WindDir3pm_N = 0
		WindDir3pm_E = 0
		WindDir3pm_W = 0
		WindDir3pm_ENE = 0
		WindDir3pm_ESE = 0
		WindDir3pm_NA = 0
		WindDir3pm_NE = 0
		WindDir3pm_NNE = 0
		WindDir3pm_NNW = 0
		WindDir3pm_NW = 0
		WindDir3pm_SE = 0
		WindDir3pm_SSE  = 0
		WindDir3pm_SSW = 0
		WindDir3pm_SW = 0
		WindDir3pm_WNW = 0
		WindDir3pm_WSW = 0
		if winddir3pm == 'S':
			WindDir3pm_S = 1
		elif winddir3pm == 'N':
			WindDir3pm_N = 1
		elif winddir3pm == 'E':
			WindDir3pm_E = 1
		elif winddir3pm == 'W':
			WindDir3pm_W = 1
		elif winddir3pm == 'ENE':
			WindDir3pm_ENE = 1
		elif winddir3pm == 'ESE':
			WindDir3pm_ESE = 1
		elif winddir3pm == 'NA':
			WindDir3pm_NA = 1
		elif winddir3pm == 'NE':
			WindDir3pm_NE = 1
		elif winddir3pm == 'NNE':
			WindDir3pm_NNE = 1
		elif winddir3pm == 'NNW':
			WindDir3pm_NNW = 1
		elif winddir3pm == 'NW':
			WindDir3pm_NW = 1
		elif winddir3pm == 'SE':
			WindDir3pm_SE = 1
		elif winddir3pm == 'SSE':
			WindDir3pm_SSE = 1
		elif winddir3pm == 'SSW':
			WindDir3pm_SSW = 1
		elif winddir3pm == 'SW':
			WindDir3pm_SW = 1
		elif winddir3pm == 'WNW':
			WindDir3pm_WNW = 1
		else:
			if winddir3pm == 'WSW':
				WindDir3pm_WSW = 1
				
				
		WindSpeed9am=float(request.form['WindSpeed9am'])
		WindSpeed3pm =float(request.form['WindSpeed3pm'])
		Humidity9am=float(request.form['Humidity9am'])
		Humidity3pm=float(request.form['Humidity3pm'])
		Pressure9am = float(request.form['Pressure9am'])
		Pressure3pm =float(request.form['Pressure3pm'])
		Cloud9am=float(request.form['Cloud9am'])
		cloud3pm=float(request.form['Cloud3pm'])
		Temp9am =float(request.form['Temp9am'])
		Temp3pm=float(request.form['Temp3pm'])
		RainToday=request.form['RainToday']
		if(RainToday=='No'):
			RainToday = 0
		else:
			RainToday = 1


		prediction=model.predict(['MinTemp','MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 
									'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm', 'RainToday', 'Month', 
									'Location_Adelaide', 'Location_Albany', 'Location_Albury', 'Location_AliceSprings', 'Location_BadgerysCreek', 'Location_Ballarat',
									'Location_Bendigo', 'Location_Brisbane', 'Location_Cairns', 'Location_Canberra', 'Location_Cobar', 'Location_CoffsHarbour', 'Location_Dartmoor', 
									'Location_Darwin', 'Location_GoldCoast', 'Location_Hobart', 'Location_Katherine', 'Location_Launceston', 'Location_Melbourne', 
									'Location_MelbourneAirport', 'Location_Mildura', 'Location_Moree', 'Location_MountGambier', 'Location_MountGinini', 'Location_Newcastle', 
									'Location_Nhil', 'Location_NorahHead', 'Location_NorfolkIsland', 'Location_Nuriootpa', 'Location_PearceRAAF', 'Location_Penrith',
									'Location_Perth', 'Location_PerthAirport', 'Location_Portland', 'Location_Richmond', 'Location_Sale', 'Location_SalmonGums', 
									'Location_Sydney', 'Location_SydneyAirport', 'Location_Townsville', 'Location_Tuggeranong', 'Location_Uluru', 'Location_WaggaWagga', 
									'Location_Walpole', 'Location_Watsonia', 'Location_Williamtown', 'Location_Witchcliffe', 'Location_Wollongong', 'Location_Woomera', 
									'WindGustDir_E', 'WindGustDir_ENE', 'WindGustDir_ESE', 'WindGustDir_N', 'WindGustDir_NE', 'WindGustDir_NNE', 'WindGustDir_NNW', 
									'WindGustDir_NW', 'WindGustDir_S', 'WindGustDir_SE', 'WindGustDir_SSE', 'WindGustDir_SSW', 'WindGustDir_SW', 'WindGustDir_W',
									'WindGustDir_WNW', 'WindGustDir_WSW', 'WindDir9am_E', 'WindDir9am_ENE', 'WindDir9am_ESE', 'WindDir9am_N', 'WindDir9am_NE', 
									'WindDir9am_NNE', 'WindDir9am_NNW', 'WindDir9am_NW', 'WindDir9am_S', 'WindDir9am_SE', 'WindDir9am_SSE', 'WindDir9am_SSW',
									'WindDir9am_SW', 'WindDir9am_W', 'WindDir9am_WNW', 'WindDir9am_WSW', 'WindDir3pm_E', 'WindDir3pm_ENE', 'WindDir3pm_ESE', 
									'WindDir3pm_N', 'WindDir3pm_NE', 'WindDir3pm_NNE', 'WindDir3pm_NNW', 'WindDir3pm_NW',
										'WindDir3pm_S', 'WindDir3pm_SE', 'WindDir3pm_SSE', 'WindDir3pm_SSW',
										'WindDir3pm_SW', 'WindDir3pm_W', 'WindDir3pm_WNW', 'WindDir3pm_WSW'])
		output=prediction
		if output == 0:
			return render_template('index.html',prediction_texts="Tommorow no rain")
		else:
			return render_template('index.html',prediction_text="There are chances it can rain tommorow")
	else:
		return render_template('index.html')

if __name__=="__main__":
	app.run(debug=True)

