from django.shortcuts import render
from .models import Mqtt_message
# Create your views here.
def index(request):
    messages = Mqtt_message.objects.all()
    context = {'messages':messages}
    return render(request, 'app_iot_platform/index.html',context)