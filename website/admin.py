from django.contrib import admin

from .models import Brewery, Style, Beer, Event, Session 


class BreweryAdmin(admin.ModelAdmin):
    pass


class StyleAdmin(admin.ModelAdmin):
    pass


class BeerAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class SessionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brewery, BreweryAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Beer, BeerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Session, SessionAdmin)
