# Generated by Django 2.0.13 on 2019-04-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_add_login_method_to_choicefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login_backend',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
