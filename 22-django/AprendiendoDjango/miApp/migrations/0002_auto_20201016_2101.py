# Generated by Django 3.1.2 on 2020-10-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=275),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
