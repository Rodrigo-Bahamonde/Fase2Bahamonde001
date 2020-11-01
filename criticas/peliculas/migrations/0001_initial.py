# Generated by Django 2.2.3 on 2020-11-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioDolittle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('comentario', models.TextField(max_length=1000)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioEndgame',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('comentario', models.TextField(max_length=1000)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioGuerra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('comentario', models.TextField(max_length=1000)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioJoker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('comentario', models.TextField(max_length=1000)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
    ]
