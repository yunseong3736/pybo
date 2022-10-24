from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin) :
    search_fields = ['subject']
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin) :
    search_fields = ['content']
admin.site.register(Answer, AnswerAdmin)