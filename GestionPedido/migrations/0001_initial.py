# Generated by Django 2.2.17 on 2020-12-03 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paciente', '0004_auto_20201203_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pedido', 'Pedido'), ('Taller', 'Taller'), ('Finalizado', 'Finalizado')], max_length=10)),
                ('subtotal', models.FloatField()),
                ('total', models.FloatField()),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('clasificacion', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lente_distancia', models.CharField(choices=[('Lejos', 'Lejos'), ('Cerca', 'Cerca')], max_length=6)),
                ('lente_posicion', models.CharField(choices=[('Derecho', 'Derecho'), ('Izquierdo', 'Izquierdo')], max_length=10)),
                ('lente_armazon', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionPedido.Pedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionPedido.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_tipo_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionPedido.TipoPago'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
