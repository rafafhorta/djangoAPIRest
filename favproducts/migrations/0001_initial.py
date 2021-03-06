# Generated by Django 3.1.4 on 2020-12-11 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('reviewScore', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='favproducts.client')),
                ('product', models.ManyToManyField(related_name='favproduct', to='favproducts.Product')),
            ],
            options={
                'unique_together': {('client',)},
            },
        ),
    ]
