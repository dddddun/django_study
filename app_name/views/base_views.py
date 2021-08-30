from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


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
