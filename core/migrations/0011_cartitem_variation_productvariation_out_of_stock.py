# Generated by Django 4.2.7 on 2023-11-20 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_productattribute_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_variation', to='core.productvariation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariation',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
    ]
