# Generated by Django 5.0.1 on 2024-02-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mob', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin', models.IntegerField(null=True)),
                ('datecreated', models.DateTimeField(null=True)),
            ],
        ),
    ]