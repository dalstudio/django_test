from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)