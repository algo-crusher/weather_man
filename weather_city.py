from flask import Flask, render_template, request
import html_geo_weather_function
import os

app = Flask(__name__)

@app.route("/")





def city_weather():
	name = request.values.get("name")
	city = request.values.get("city")
	forecast = None
	if city:

		forecast = html_geo_weather_function.get_weather(city)
		
	return render_template('city_weather.html',
                           name=name, city=city, forecast=forecast)
	
#app.route("/about")

#def about():
#	return render_template('about.html')

# name(orange) is the assignment inside 
# the templates, name(white), is the variable 
# already assigned



if __name__ == "__main__":
	port = int(os.environ.get("PORT",5000))
	app.run()(host="1.1.1.1", port=port)
