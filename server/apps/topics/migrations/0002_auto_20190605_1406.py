# Generated by Django 2.2.1 on 2019-06-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicmessage',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='HT__IMAGE', null=True, related_name='topic_messages', to='topics.Image', verbose_name='VN__IMAGE'),
        ),
    ]
