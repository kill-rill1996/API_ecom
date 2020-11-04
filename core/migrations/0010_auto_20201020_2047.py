# Generated by Django 3.1.1 on 2020-10-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201010_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-created'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=5000)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.reviews')),
            ],
            options={
                'verbose_name': 'Отзыв о товаре',
                'verbose_name_plural': 'Отзывы о товаре',
            },
        ),
    ]
