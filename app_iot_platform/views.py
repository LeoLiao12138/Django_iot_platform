from django.shortcuts import render
from .models import Mqtt_message
# Create your views here.
def index(request):
    message = Mqtt_message.objects.get(id = 1)
    context = {'topic':message.topic, 'payload':message.payload}
    return render(request, 'app_iot_platform/index.html',context)