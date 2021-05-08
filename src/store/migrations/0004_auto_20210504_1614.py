# Generated by Django 3.1.3 on 2021-05-04 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210504_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='buying_type',
        ),
        migrations.RemoveField(
            model_name='order',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создание заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='store.product')),
            ],
        ),
    ]
