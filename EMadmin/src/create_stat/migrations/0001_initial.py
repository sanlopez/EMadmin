# Generated by Django 2.2 on 2020-07-20 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('create_proj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberMovies', models.IntegerField(default=-1)),
                ('numberFractionsPerMovie', models.IntegerField(default=-1)),
                ('averageResolution', models.FloatField(default=-1)),
                ('averageAstigmatism', models.FloatField(default=-1)),
                ('resolutionData', models.TextField()),
                ('defocusData', models.TextField()),
                ('astigmaticData', models.TextField()),
                ('gainData', models.TextField()),
                ('alignmentShiftX', models.TextField()),
                ('alignmentShiftY', models.TextField()),
                ('acquisition', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='create_proj.Acquisition')),
            ],
        ),
    ]
