# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from books.models import Publisher,Book,Author

# Register your models here.
admin.site.register([Publisher,Book,Author])