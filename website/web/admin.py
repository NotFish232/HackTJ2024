from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Alert)
admin.site.register(InformationReport)
admin.site.register(FacialDetectionResult)