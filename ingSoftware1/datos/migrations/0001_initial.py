# Generated by Django 3.0.9 on 2021-01-10 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=300)),
                ('usuario', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=350)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('calorias_totales', models.FloatField()),
                ('macronutrientes', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='')),
                ('direccion_envio', models.CharField(max_length=500)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dolares_por_kilometros', models.FloatField()),
                ('valor_comida', models.FloatField()),
                ('direccion_fija', models.CharField(max_length=500)),
                ('no_comidas_por_semana', models.IntegerField(default=0)),
                ('no_de_comida_por_dia', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pago', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.FloatField()),
                ('nombre_impuesto', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_propietario', models.CharField(max_length=200)),
                ('tipo_tarjeta', models.CharField(max_length=200)),
                ('fecha_caducidad', models.DateField()),
                ('direccion_facturacion', models.CharField(max_length=350)),
                ('cvv', models.IntegerField(default=0)),
                ('numero_tarjeta', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSuscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=350)),
                ('duracion', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('cantidad_comidas', models.IntegerField(default=0)),
                ('comidas_gratis', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=200)),
                ('id_tipo_suscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.TipoSuscripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('peso_inicio', models.FloatField()),
                ('peso_meta', models.FloatField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emitido', models.DateTimeField(verbose_name='Fecha de emisión')),
                ('estado', models.IntegerField(default=0)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('id_forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.FormaDePago')),
                ('id_iva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Iva')),
                ('id_suscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Suscripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Dias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Calendario')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emitido', models.DateTimeField(verbose_name='Fecha de emisión')),
                ('hora_entrega', models.TimeField()),
                ('estado_pedido', models.IntegerField(default=0)),
                ('id_comida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Comidas')),
                ('id_dias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Dias')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_dias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_entrega', models.DateTimeField(verbose_name='Hora de entrega')),
                ('id_comida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Comidas')),
                ('id_dias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Dias')),
            ],
        ),
        migrations.AddField(
            model_name='comidas',
            name='id_vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Vendedor'),
        ),
        migrations.CreateModel(
            name='ClienteSuscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comidas_consumidas', models.IntegerField(default=0)),
                ('fecha_inicio', models.DateField()),
                ('fecha_de_caducidad', models.DateField()),
                ('fecha_facturacion', models.DateField()),
                ('comidas_disponibles', models.IntegerField(default=0)),
                ('comidas_gratis_disponibles', models.IntegerField(default=0)),
                ('comidas_gratis_consumidas', models.IntegerField(default=0)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Cliente')),
                ('id_suscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Suscripcion')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_tarjeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Tarjeta'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='nombre_perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Perfil'),
        ),
        migrations.AddField(
            model_name='calendario',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Cliente'),
        ),
    ]