# Generated by Django 4.1.13 on 2024-01-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='enrolled',
            unique_together={('subject', 'student')},
        ),
    ]