from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from django.core.paginator import Paginator


# 질문 목록 보기
def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리 (페이지당 10개씩 보여주기)
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
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
