from django.contrib import admin
from .models import Question


# 관리자 화면에서 제목(subject)로 질문 검색하기
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
