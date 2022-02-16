# Generated by Django 4.0.2 on 2022-02-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_description', models.TextField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_qty',
            field=models.IntegerField(),
        ),
    ]
