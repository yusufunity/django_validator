# Generated by Django 4.1 on 2022-08-27 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Kategoriya nomi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-create_at'], 'verbose_name': 'Yanglik', 'verbose_name_plural': 'Yangiliklar'},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, verbose_name='Kontent'),
        ),
        migrations.AlterField(
            model_name='news',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tuzilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publikabad'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='img/%Y/%m/%d/', verbose_name='rasm'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Ozgargan vaqti'),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Kategoriya nomi'),
        ),
    ]
