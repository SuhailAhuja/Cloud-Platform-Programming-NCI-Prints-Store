# Generated by Django 3.2.2 on 2022-04-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0003_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='Complaint',
            name='Address',
            field=models.TextField(max_length=4000, null=True),
        ),
    ]
