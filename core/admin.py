from django.contrib import admin

from core.models import Riddle


@admin.register(Riddle)
class RiddleAdmin(admin.ModelAdmin):
    pass
