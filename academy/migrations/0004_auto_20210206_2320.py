# Generated by Django 3.1.6 on 2021-02-06 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_auto_20210206_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.student'),
        ),
    ]