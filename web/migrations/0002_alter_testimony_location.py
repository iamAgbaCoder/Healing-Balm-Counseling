# Generated by Django 4.2 on 2023-10-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='location',
            field=models.CharField(default='Unknown', help_text='State, Country - e.g Lagos, Nigeria', max_length=20),
        ),
    ]
