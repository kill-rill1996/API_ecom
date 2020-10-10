# Generated by Django 3.1.1 on 2020-10-10 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20201001_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adding_date', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(to='core.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Избранный товар',
                'verbose_name_plural': 'Избранные товары',
            },
        ),
    ]