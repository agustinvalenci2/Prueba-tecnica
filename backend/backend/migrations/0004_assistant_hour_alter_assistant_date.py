# Generated by Django 4.1.13 on 2024-01-25 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_enrolled_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistant',
            name='hour',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.hours'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assistant',
            name='date',
            field=models.DateField(),
        ),
    ]