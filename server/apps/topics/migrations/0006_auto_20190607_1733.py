# Generated by Django 2.2.1 on 2019-06-07 14:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0005_auto_20190605_1707'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='topicmessageread',
            unique_together={('topic', 'user')},
        ),
    ]