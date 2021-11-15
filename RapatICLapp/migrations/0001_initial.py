# Generated by Django 3.2.8 on 2021-11-14 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asisten',
            fields=[
                ('nim', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rapat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topik', models.CharField(max_length=50)),
                ('tanggal', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Notulensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('konten', models.TextField()),
                ('notulen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RapatICLapp.asisten')),
                ('rapat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RapatICLapp.rapat')),
            ],
        ),
        migrations.CreateModel(
            name='Absensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hadir', models.BooleanField()),
                ('asisten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asisten', to='RapatICLapp.asisten')),
                ('rapat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rapat', to='RapatICLapp.rapat')),
            ],
        ),
    ]
