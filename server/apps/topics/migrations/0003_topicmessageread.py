# Generated by Django 2.2.1 on 2019-06-05 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0002_auto_20190605_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicMessageRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(help_text='HT__MESSAGE', on_delete=django.db.models.deletion.CASCADE, related_name='topic_messages_read', to='topics.TopicMessage', verbose_name='VN__MESSAGE')),
                ('topic', models.ForeignKey(help_text='HT__TOPIC', on_delete=django.db.models.deletion.CASCADE, related_name='topic_messages_read', to='topics.Topic', verbose_name='VN__TOPIC')),
                ('user', models.ForeignKey(help_text='HT__USER', on_delete=django.db.models.deletion.CASCADE, related_name='topic_messages_read', to=settings.AUTH_USER_MODEL, verbose_name='VN__USER')),
            ],
            options={
                'verbose_name': 'VN__TOPIC_MESSAGE_READ',
                'verbose_name_plural': 'VN__TOPIC_MESSAGES_READ',
                'ordering': ('-created_at',),
            },
        ),
    ]
