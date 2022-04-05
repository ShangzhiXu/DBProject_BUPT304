from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Competition)
admin.site.register(English)
admin.site.register(Practice)
admin.site.register(Major)
admin.site.register(Application)
admin.site.register(Agent)
admin.site.register(Teacher)
admin.site.register(Program)