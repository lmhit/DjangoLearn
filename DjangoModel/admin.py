# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  DjangoModel.models import Test
from DjangoModel.models import Contact
from DjangoModel.models import Tag


# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name','email')


class  TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    # list_display = ('name','email')  # list
    search_fields = ('name',)
    inlines = [TagInline]

    fieldsets = (
       ['Main',{
           'fields':('name','email')
       }],

        ['Advance',{
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]

    )



# Register your models here.
admin.site.register([Test,Tag])
admin.site.register(Contact,ContactAdmin)