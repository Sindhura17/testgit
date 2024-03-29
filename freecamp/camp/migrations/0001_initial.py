# Generated by Django 2.2.3 on 2019-11-01 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('special', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=10)),
                ('nod', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ngo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=10)),
                ('dis', models.TextField()),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='regis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camp.doctor')),
                ('evid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camp.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='org_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camp.ngo'),
        ),
    ]
