from django.contrib import admin

from bug.models import Developer, ProjectManager, Administrator
# Register your models here.


admin.site.register(Administrator)
admin.site.register(Developer)
admin.site.register(ProjectManager)