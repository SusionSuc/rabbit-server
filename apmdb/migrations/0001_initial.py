# Generated by Django 3.0 on 2019-12-12 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppPageSpeedInfo',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('time', models.IntegerField(default=0)),
                ('createStartTime', models.IntegerField(default=0)),
                ('createEndTime', models.IntegerField(default=0)),
                ('inflateFinishTime', models.IntegerField(default=0)),
                ('fullDrawFinishTime', models.IntegerField(default=0)),
                ('resumeEndTime', models.IntegerField(default=0)),
                ('pageName', models.CharField(max_length=100)),
                ('apiRequestCostStr', models.CharField(max_length=200)),
            ],
        ),
    ]
