# Generated by Django 3.2.4 on 2023-09-19 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.AutoField(db_column='idPedido', primary_key=True, serialize=False)),
                ('fechaPedido', models.DateField(db_column='fechaPedido')),
                ('direccionEnvio', models.TextField(db_column='direccionEnvio', max_length=200)),
                ('estadoPedido', models.TextField(db_column='estadoPedido', max_length=20)),
                ('totalPedido', models.FloatField(db_column='totalPedido')),
                ('metodoPago', models.TextField(db_column='metodoPago', max_length=20)),
                ('fk_usuario', models.ForeignKey(db_column='fk_usuario', on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
            options={
                'db_table': 'Pedidos',
            },
        ),
    ]
