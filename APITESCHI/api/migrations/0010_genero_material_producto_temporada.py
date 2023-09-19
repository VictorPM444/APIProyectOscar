# Generated by Django 3.2.4 on 2023-09-19 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('nombreGenero', models.TextField(db_column='nombreGenero', max_length=20)),
            ],
            options={
                'db_table': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('idMaterial', models.AutoField(db_column='idMaterial', primary_key=True, serialize=False)),
                ('nombreMaterial', models.TextField(db_column='nombreMaterial', max_length=30)),
            ],
            options={
                'db_table': 'Materiales',
            },
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('idTemporada', models.AutoField(db_column='idTemporada', primary_key=True, serialize=False)),
                ('nombreTemporada', models.TextField(db_column='nombreTemporada', max_length=30)),
            ],
            options={
                'db_table': 'Temporadas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombreProducto', models.TextField(db_column='nombreProducto', max_length=50)),
                ('descripcionProducto', models.TextField(db_column='descripcionProducto', max_length=100)),
                ('precioProducto', models.FloatField(db_column='precioProducto')),
                ('imagenProducto', models.ImageField(db_column='imagenProducto', upload_to='')),
                ('disponibilidadStock', models.IntegerField(db_column='disponibilidadStock')),
                ('fk_categoria', models.ForeignKey(db_column='fk_categoria', on_delete=django.db.models.deletion.CASCADE, to='api.categoria')),
                ('fk_color', models.ForeignKey(db_column='fk_color', on_delete=django.db.models.deletion.CASCADE, to='api.color')),
                ('fk_genero', models.ForeignKey(db_column='fk_genero', on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
                ('fk_marca', models.ForeignKey(db_column='fk_marca', on_delete=django.db.models.deletion.CASCADE, to='api.marca')),
                ('fk_material', models.ForeignKey(db_column='fk_material', on_delete=django.db.models.deletion.CASCADE, to='api.material')),
                ('fk_talla', models.ForeignKey(db_column='fk_talla', on_delete=django.db.models.deletion.CASCADE, to='api.talla')),
                ('fk_temporada', models.ForeignKey(db_column='fk_temporada', on_delete=django.db.models.deletion.CASCADE, to='api.temporada')),
            ],
        ),
    ]