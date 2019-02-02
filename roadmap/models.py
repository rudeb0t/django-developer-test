from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class RoadmapStep(models.Model):
    """
    Data model for roadmap step objects.
    """
    name = models.CharField(max_length=100,
                            help_text=_('Roadmap step name.'))
    explanation = models.TextField(help_text=_('Explanation of how to complete'
                                               ' this step.'))

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return '{}: {}'.format(self.name, self.explanation)


class Roadmap(models.Model):
    """
    Data model for roadmap objects.
    """
    name = models.CharField(max_length=100,
                            help_text=_('Roadmap name.'))
    steps = models.ManyToManyField(RoadmapStep, related_name='roadmaps',
                                   help_text=_('Steps required to complete this'
                                               ' roadmap.'))

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Project(models.Model):
    """
    Data model for project objects.
    """
    name = models.CharField(max_length=100,
                            help_text=_('Project name.'))
    description = models.CharField(max_length=200,
                                   help_text=_('One line project description.'))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              help_text=_('Project owner.'))
    roadmap = models.ForeignKey(Roadmap, related_name='projects',
                                help_text=_('Project roadmap.'))

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
