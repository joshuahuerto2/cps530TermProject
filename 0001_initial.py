# Generated by Django 2.2.7 on 2019-11-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(help_text='This field is required', max_length=100)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
