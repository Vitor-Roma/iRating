# Generated by Django 4.0.4 on 2022-06-23 17:01

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=1000)),
                ('detail', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=app.models.upload_image)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=1000)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=app.models.upload_image)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('note', models.CharField(max_length=9999)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('size', models.IntegerField()),
                ('complement', models.IntegerField()),
                ('side_dish', models.IntegerField()),
                ('comment', models.CharField(max_length=9999)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('restaurant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.restaurant')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=app.models.upload_image)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
