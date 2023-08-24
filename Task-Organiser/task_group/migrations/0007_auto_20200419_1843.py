# Generated by Django 2.1.5 on 2020-04-19 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_group', '0006_remove_task_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='Catagories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Task', to='task_group.Catagories'),
        ),
    ]
