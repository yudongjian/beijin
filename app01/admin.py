from django.contrib import admin

# Register your models here.
from .models import userinfo


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(userinfo, QuestionAdmin)

