# Generated by Django 5.0.1 on 2024-05-21 07:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_myproteindetails_product_price_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproteindetails',
            name='product_Category',
            field=models.CharField(choices=[('Optimum Nutrition Protein Supplement', 'Optimum Nutrition Protein Supplement'), ('Nutrition Protein Supplement', 'Nutrition Protein Supplement ')], max_length=100),
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('totalprice', models.FloatField(default=0)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.myproteindetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]