# Generated by Django 4.2.7 on 2023-12-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=230)),
                ('imgs', models.ImageField(upload_to='pics')),
                ('description', models.TextField()),
            ],
        ),
    ]