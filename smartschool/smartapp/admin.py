from django.contrib import admin
from .models import Activity, Alumni


# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    pass

class AlumniAdmin(admin.ModelAdmin):
    pass


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Alumni, AlumniAdmin)

