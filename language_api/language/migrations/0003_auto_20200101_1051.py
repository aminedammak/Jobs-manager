# Generated by Django 3.0.1 on 2020-01-01 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0002_paradigm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='paradigm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='language.Paradigm'),
        ),
    ]
