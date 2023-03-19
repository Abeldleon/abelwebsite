# Generated by Django 4.1.7 on 2023-03-19 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habla', '0004_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'published')], default='draft', max_length=10),
        ),
    ]