# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import City ,Issues ,Customer ,Lawyer
# Register your models here.
admin.site.register(City)
admin.site.register(Issues)
admin.site.register(Customer)
admin.site.register(Lawyer)
