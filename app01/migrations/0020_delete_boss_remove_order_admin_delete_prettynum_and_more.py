# Generated by Django 5.0 on 2023-12-23 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0019_remove_department_title_department_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Boss',
        ),
        migrations.RemoveField(
            model_name='order',
            name='admin',
        ),
        migrations.DeleteModel(
            name='PrettyNum',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]