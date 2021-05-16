# Generated by Django 3.2 on 2021-05-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('field_name', models.CharField(help_text='Input here:', max_length=255)),
            ],
            options={
                'ordering': ['title', '-field_name'],
            },
        ),
    ]
