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
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Project name.', max_length=100)),
                ('description', models.CharField(help_text='One line project description.', max_length=200)),
                ('owner', models.ForeignKey(help_text='Project owner.', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Roadmap name.', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RoadmapStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Roadmap step name.', max_length=100)),
                ('explanation', models.TextField(help_text='Explanation of how to complete this step.')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='roadmap',
            name='steps',
            field=models.ManyToManyField(help_text='Steps required to complete this roadmap.', related_name='roadmaps', to='roadmap.RoadmapStep'),
        ),
        migrations.AddField(
            model_name='project',
            name='roadmap',
            field=models.ForeignKey(related_name='projects', to='roadmap.Roadmap', help_text='Project roadmap.'),
        ),
    ]
