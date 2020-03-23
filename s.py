from pprint import pprint
import pyowm
owm = pyowm.OWM('8a61904f69fc073fe5128d1cefe42b9b')
observation = owm.weather_at_place('Ravangla,India')
print(observation.get_weather().)
