# Generated by Django 2.2.5 on 2020-01-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last name')),
                ('author_name', models.CharField(max_length=200, verbose_name='Author name')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ('author_name',),
            },
        ),
        migrations.DeleteModel(
            name='Chatting',
        ),
    ]
