from flask import Flask , request , render_template
import requests
app = Flask(__name__)

class class_weather():
    def __init__ (self ,city_name ,temperature ,pressure ,humidity ,windspeed ,description):
        self.name = city_name
        self.temp = temperature
        self.press = pressure
        self.hum = humidity
        self.wind = windspeed
        self.des = description

def k_into_c(temp_in_k):
    temp_in_c=temp_in_k - 273.15
    return temp_in_c
        
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    zipcode1 = request.form['zipcode']
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode1+',pl&appid=1617e3120079a59e6460661b46b2a98f')
    #response = requests.get('http://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22')
    json_text = response.json()

    list_of_description = json_text['weather']
    jason_of_description = list_of_description[0]
    describ = jason_of_description['description']
    
    wz = class_weather(json_text['name'],json_text['main']['temp'],json_text['main']['pressure'],json_text['main']['humidity'],json_text['wind']['speed'],describ)

    wz.temp=k_into_c(wz.temp)
    wz.temp=str(wz.temp)
    wz.press=str(wz.press)
    wz.hum=str(wz.hum)
    wz.wind=str(wz.wind)


    return render_template('weather.html' , city=wz.name , description=wz.des , temperature=wz.temp , pressure=wz.press , humidity=wz.hum , wind=wz.wind)
    
if __name__ == "__main__":
    app.run()
