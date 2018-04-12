# Generated by Django 2.0.3 on 2018-04-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180409_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete='CASCADE', to='shop.Product')),
            ],
        ),
    ]
