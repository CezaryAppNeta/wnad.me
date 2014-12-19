# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True)),
                ('ingredients', models.TextField(help_text='One indigrent per line', verbose_name='Indigrents')),
                ('preparation', models.TextField(verbose_name='Preparation')),
                ('time_for_preparation', models.IntegerField(help_text='Zeit in Minuten angeben', null=True, verbose_name='Preparation time', blank=True)),
                ('number_of_portions', models.PositiveIntegerField(verbose_name='Number of portions')),
                ('difficulty', models.SmallIntegerField(default=2, verbose_name='Difficulty', choices=[(1, 'easy'), (2, 'normal'), (3, 'hard')])),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_updated', models.DateTimeField(editable=False)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='recipes.Category', verbose_name='Categories')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
            },
            bases=(models.Model,),
        ),
    ]
