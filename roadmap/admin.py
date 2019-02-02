from django.contrib import admin
from roadmap.models import Project, Roadmap, RoadmapStep


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'roadmap', 'owner')


class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('name', 'steps_count')

    def steps_count(self, obj):
        return obj.steps.count()
    steps_count.short_description = 'Number of Steps'


class RoadmapStepAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Roadmap, RoadmapAdmin)
admin.site.register(RoadmapStep, RoadmapStepAdmin)
