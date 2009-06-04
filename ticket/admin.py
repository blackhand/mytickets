from django.contrib import admin
from models import Category, Event, Ticket, Auditorium, Province, Country, Artist, Zone


class ZoneInline(admin.StackedInline):
    model = Zone 


class ProvinceAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


class AuditoriumAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    inlines = [
            ZoneInline,
            ]


class TicketAdmin(admin.ModelAdmin):
    pass


class ArtistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Province, ProvinceAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Auditorium, AuditoriumAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Ticket, TicketAdmin)
