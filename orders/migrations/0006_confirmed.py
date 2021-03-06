# Generated by Django 3.0.6 on 2020-06-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200618_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('order_time', models.TimeField()),
                ('user', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=30)),
                ('item_category', models.CharField(max_length=30)),
                ('item_size', models.CharField(blank=True, max_length=30)),
                ('item_toppings_num', models.IntegerField(blank=True, default=0)),
                ('item_toppings_list', models.CharField(blank=True, max_length=100)),
                ('item_total_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
