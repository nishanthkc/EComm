# Generated by Django 3.2.5 on 2022-04-27 16:40

from django.db import migrations, models
import django.db.models.deletion
import exp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=exp.models.get_file_path)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=exp.models.get_file_path)),
                ('product_desciption', models.TextField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('product_status', models.BooleanField(default=False, help_text='0=default, 1=hidden')),
                ('product_trending', models.BooleanField(default=False, help_text='0=default, 1=trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp.category')),
            ],
        ),
    ]
