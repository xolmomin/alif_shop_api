from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from apps.models import Category


@admin.register(Category)
class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20
