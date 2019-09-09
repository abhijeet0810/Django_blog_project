from django.contrib import admin

# Register your models here.
# In order to use the models, it should be registered here
from .models import Question
from .models import Tutorial

admin.site.register(Question)
admin.site.register(Tutorial)