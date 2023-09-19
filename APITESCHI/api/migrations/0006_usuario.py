# Generated by Django 3.2.4 on 2023-09-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('nombreUsuario', models.TextField(db_column='nombreUsuario', max_length=50)),
                ('apellidoPaterno', models.TextField(db_column='apellidoPaterno', max_length=50)),
                ('apellidoMaterno', models.TextField(db_column='apellidoMaterno', max_length=50)),
                ('password', models.TextField(db_column='password', max_length=25)),
                ('correoElectronico', models.EmailField(db_column='correoElectronico', max_length=254)),
                ('numeroTelefonico', models.IntegerField(db_column='numeroTelefonico')),
            ],
        ),
    ]
