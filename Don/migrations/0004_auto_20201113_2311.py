# Generated by Django 3.1.2 on 2020-11-13 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Statistique', '0001_initial'),
        ('Don', '0003_auto_20201113_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistique',
            name='gouvernorat_FK',
        ),
        migrations.AlterField(
            model_name='hopital',
            name='gouvernorat_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Statistique.gouvernorat'),
        ),
        migrations.DeleteModel(
            name='Gouvernorat',
        ),
        migrations.DeleteModel(
            name='Statistique',
        ),
    ]
