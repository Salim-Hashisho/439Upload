# Generated by Django 4.2.5 on 2023-09-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0003_alter_contact_image_alter_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
