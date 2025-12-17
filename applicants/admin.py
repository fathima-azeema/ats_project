from django.contrib import admin
from .models import Applicant


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'position', 'status', 'created_at')
    list_filter = ('status', 'position', 'created_at')
    search_fields = ('name', 'email', 'phone', 'position')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Application Details', {
            'fields': ('position', 'resume_url', 'resume_file', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
