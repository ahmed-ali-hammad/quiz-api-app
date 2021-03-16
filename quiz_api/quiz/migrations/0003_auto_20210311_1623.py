# Generated by Django 3.1.7 on 2021-03-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210311_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active Status'),
        ),
        migrations.AddField(
            model_name='questions',
            name='level',
            field=models.IntegerField(choices=[(0, 'Fundamental'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')], default=0, verbose_name='Level'),
        ),
        migrations.AddField(
            model_name='questions',
            name='technique',
            field=models.IntegerField(choices=[(0, 'Multiple Choice')], default=0, verbose_name='Question Type'),
        ),
        migrations.AddField(
            model_name='questions',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='quizes',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='answers',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='quizes',
            name='title',
            field=models.CharField(default='New Quiz', max_length=225, verbose_name='Quiz Title'),
        ),
    ]
