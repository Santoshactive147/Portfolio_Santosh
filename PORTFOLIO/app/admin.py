from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('title', 'description', 'image', 'link') # Add any other fields if needed

    # Make 'description' field expandable in list view
    list_filter = ('title',)  # Optional: To filter by title, you can add other fields too
    search_fields = ('title', 'description',)  # Enable search functionality in admin

    # Add fieldsets to display fields in detail view
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'link')
        }),
    )
    
 

    # Optional: Make fields editable directly in the list view
    list_editable = ('link',)  # You can specify editable fields directly in the list view

# Register the model with the custom admin class
admin.site.register(Project, ProjectAdmin)





from django.contrib import admin
from .models import QueryMessages

@admin.register(QueryMessages)
class QueryMessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')
    search_fields = ('name', 'email', 'message')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
