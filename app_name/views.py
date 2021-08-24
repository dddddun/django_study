from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# from .models import Answer
from .models import Question
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("안녕하세요~~~~~~ 이거슨~~~~~ 테스트페이지 이지롱")


# 질문 목록 보기
def index(request):
    # 질문 목록 데이터 (생성일 역순(-)으로 정렬)
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # render함수 = 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
    return render(request, 'app_name/question_list.html', context)

# 질문글 자세히 보기
def detail(request, question_id):
    # 질문 내용 데이터
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'app_name/question_detail.html', context)

# 질문에 대한 답변 생성하기 1
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 답변 생성 후 질문 상세 화면을 다시 보여주기 위한 redirect함수 사용
    return redirect('app_name:detail', question_id=question_id)

# 질문에 대한 답변 생성하기 2 (Answer 모델을 import해서 직접 사용하는 방법)
# def answer_create(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
#     answer.save()
#     return redirect('app_name:detail', question_id=question.id)
