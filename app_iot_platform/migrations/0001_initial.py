# Generated by Django 3.2.13 on 2022-05-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mqtt_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField()),
                ('payload', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
