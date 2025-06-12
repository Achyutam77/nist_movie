from django.contrib import admin

from .models import Favorites, WatchHistory

admin.site.register(WatchHistory)
admin.site.register(Favorites)
