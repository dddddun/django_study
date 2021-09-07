from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question


# 질문 목록 보기
def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent') # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 조회
    # question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리 (페이지당 10개씩 보여주기)
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'app_name/question_list.html', context)

# 질문글 자세히 보기
def detail(request, question_id):
    # 질문 내용 데이터
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'app_name/question_detail.html', context)
