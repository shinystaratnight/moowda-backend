# Generated by Django 2.2.1 on 2019-06-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_password_hash',
            field=models.CharField(blank=True, help_text='HT__RESET_PASSWORD_HASH', max_length=150, null=True, unique=True, verbose_name='VN__RESET_PASSWORD_HASH'),
        ),
    ]
