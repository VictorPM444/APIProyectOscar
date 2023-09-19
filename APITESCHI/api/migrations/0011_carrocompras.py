# Generated by Django 3.2.4 on 2023-09-19 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_genero_material_producto_temporada'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarroCompras',
            fields=[
                ('idCarroCompras', models.AutoField(db_column='idCarroCompras', primary_key=True, serialize=False)),
                ('numeroProducto', models.IntegerField(db_column='numeroProducto')),
                ('fk_producto', models.ForeignKey(db_column='fk_producto', on_delete=django.db.models.deletion.CASCADE, to='api.producto')),
                ('fk_usuario', models.ForeignKey(db_column='fk_usuario', on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
            options={
                'db_table': 'CarroCompras',
            },
        ),
    ]
