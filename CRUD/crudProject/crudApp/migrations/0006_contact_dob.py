# Generated by Django 4.2.5 on 2023-09-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0005_alter_contact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='dob',
            field=models.DateField(auto_now=True),
        ),
    ]