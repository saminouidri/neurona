# Generated by Django 5.0.2 on 2024-04-09 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neuronaLogs', '0002_alter_commentlogs_comment_id_alter_postlogs_admin_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogs',
            name='email',
        ),
    ]