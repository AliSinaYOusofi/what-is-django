from django.contrib import admin

from .models import Questions
from .models import Choice
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

# admin.site.register(Questions)
admin.site.register(Choice) 
admin.site.register(Questions, QuestionAdmin)