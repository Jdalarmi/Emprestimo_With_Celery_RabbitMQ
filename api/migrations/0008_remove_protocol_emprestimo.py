# Generated by Django 5.0 on 2024-01-04 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_protocol_emprestimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocol',
            name='emprestimo',
        ),
    ]
