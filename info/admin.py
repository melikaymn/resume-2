from django.contrib import admin

# Register your models here.
from  . import models

admin.site.register(models.professional_skills)
admin.site.register(models.education)
admin.site.register(models.skills)
admin.site.register(models.personal_info)
admin.site.register(models.skills_2)