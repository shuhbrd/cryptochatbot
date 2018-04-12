# Generated by Django 2.0.3 on 2018-04-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_login', models.CharField(max_length=10)),
                ('customer_email', models.CharField(max_length=30)),
                ('customer_password', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
    ]
