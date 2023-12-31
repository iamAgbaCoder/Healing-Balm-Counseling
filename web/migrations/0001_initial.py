# Generated by Django 4.2 on 2023-10-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=14)),
                ('age_range', models.CharField(max_length=12)),
                ('challenge', models.CharField(max_length=15)),
                ('date_of_appointment', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'ordering': ('-date_created',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Counsellor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('specialization', models.CharField(max_length=15)),
                ('short_bio', models.CharField(help_text='Bio should be short, precise and detailed - Max 100 characters', max_length=100)),
                ('image', models.ImageField(upload_to='counsellors/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Counsellor',
                'verbose_name_plural': 'Counsellors',
                'ordering': ('-date_added',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=30)),
                ('title', models.CharField(help_text='e.g Deliverance from depression. Short and precise.', max_length=50)),
                ('testimony', models.TextField()),
                ('location', models.CharField(default='Unknown', help_text='State, Country - e.g Lagos, Nigeria', max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='logo.png', upload_to='testimonials/')),
            ],
            options={
                'verbose_name': 'Testimony',
                'verbose_name_plural': 'Testimonies',
                'ordering': ('-date_created',),
            },
        ),
    ]
