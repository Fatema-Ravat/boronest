# Generated by Django 5.0.6 on 2024-12-04 06:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.FileField(default='borrow/images/default_pic.png', upload_to='borrow')),
                ('description', models.TextField()),
                ('is_listed', models.BooleanField(default=True)),
                ('is_availabe', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('BK', 'Book'), ('EL', 'Electronic'), ('TY', 'Toys'), ('MISC', 'Others')], default='BK', max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField()),
                ('is_returned', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('borrowed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowing_user', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowproduct', to='borrow.product')),
            ],
        ),
    ]
