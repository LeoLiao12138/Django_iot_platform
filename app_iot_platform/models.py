from django.db import models

# Create your models here.
class Mqtt_message(models.Model):
    topic = models.TextField()
    payload = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.topic