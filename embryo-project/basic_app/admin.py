from django.contrib import admin
from basic_app.models import ResourcePerson,MemberInfo,Event,Expenses
from django.conf.urls import url
from django.contrib import admin

# Register your models here.
admin.site.register(ResourcePerson)
admin.site.register(Event)
admin.site.register(MemberInfo)

admin.site.register(Expenses)

admin.site.site_header = 'BPHC Embryo Portal'
admin.site.site_title = 'Embryo Tech Team'
admin.site.index_title = 'Embryo Portal'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
