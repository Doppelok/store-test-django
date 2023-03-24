# Generated by Django 4.1.6 on 2023-03-13 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseAttrValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='IPProductAttr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='multi_store.caseattrvalue')),
            ],
        ),
        migrations.CreateModel(
            name='IRAttrValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='LensAttrValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('information', models.TextField()),
                ('image', models.FileField(upload_to='products_images')),
                ('price', models.FloatField()),
                ('in_stock', models.PositiveIntegerField(default=0)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multi_store.ipproductattr')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResolutionAttrValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multi_store.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsSubGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multi_store.productscategories')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='product_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multi_store.productssubgroup'),
        ),
        migrations.AddField(
            model_name='ipproductattr',
            name='ir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ir', to='multi_store.irattrvalue'),
        ),
        migrations.AddField(
            model_name='ipproductattr',
            name='lens',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lens', to='multi_store.lensattrvalue'),
        ),
        migrations.AddField(
            model_name='ipproductattr',
            name='product_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multi_store.productssubgroup'),
        ),
        migrations.AddField(
            model_name='ipproductattr',
            name='resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resolution', to='multi_store.resolutionattrvalue'),
        ),
    ]
