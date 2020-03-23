from pprint import pprint
import pyowm
from django.utils import timezone 
#from  models import TimeModel

def get_weather():
    owm = pyowm.OWM('8a61904f69fc073fe5128d1cefe42b9b')
    observation = owm.weather_at_place('Ravangla,India')
    obj = observation.get_weather()
    return obj

