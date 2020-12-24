# Generated by Django 3.1.4 on 2020-12-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Simple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('number', models.IntegerField(null=True)),
                ('url', models.URLField(default='www.abc.com')),
            ],
        ),
    ]
