from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_date', 'subject']
    search_fields = ['subject', 'content']

admin.site.register(Question, QuestionAdmin) # Question 모델 등록
# Question 모델에 세부 기능을 추가할 수 있는 QuestionAdmin 생성
# 제목 검색을 위해 search_fields 속성에 'subject' 추가

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_date', 'question_id', 'content']

admin.site.register(Answer, AnswerAdmin)

