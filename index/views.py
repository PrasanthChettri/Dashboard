from django.views import generic
from django.utils import timezone 
from .fetch_weather import get_weather 
from .models import TimeModel
import pyowm
from .fetch_mail import Gmail
import os

def get_t():
    c_time = timezone.localtime(timezone.now())
    model = TimeModel.objects.get(pk = 1)
    obj = get_weather()
    local_m = timezone.localtime(model.time)
    if c_time.hour != local_m.hour or c_time.day != local_m.day :
        print("UPDATED")
        indexes , values = list(zip(*obj.get_temperature('celsius').items()))
        model.tmp_c , model.tmp_max , model.tmp_min , _  = values
        model.humidity = obj.get_humidity()
        model.status = obj.get_status()
        model.icon_url = obj.get_weather_icon_url()

    model.time  = c_time
    model.save()
    return model
    
class main_index(generic.ListView):
    template_name = "index/index.html"
    queryset = {''}
    def __init__(self):
        self.objM = Gmail()
        print(os.getcwd())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_model'] = get_t()
        context['mails']   = self.objM.get_snipped_messages() 
        return context
