from django.contrib import admin
from .models import Choice, Question


class ChoiseInkine(admin.TabularInline):
    model = Choice
    extra = 3
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information',  {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiseInkine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)