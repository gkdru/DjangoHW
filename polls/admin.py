from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'question_text', 'comment')
    actions = ('stradd',)

    def stradd(self, request, queryset):
        for q in queryset:
            q.question_text = q.question_text + "$"
            q.save()
        self.message_user(request, 'Done')
    stradd.short_description = 'Добавить $ к строке'


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)