from django.contrib import admin
from .models import Fart


class FartAdmin(admin.ModelAdmin):

    list_per_page = 50
    list_display = ('category',
                    'topic',
                    'project',
                    )

    # block/playlist list_filter will only show up when there are >= 2 choices available
    list_filter = ['category',
                   'topic',
                   'project',]

admin.site.register(Fart, FartAdmin)
