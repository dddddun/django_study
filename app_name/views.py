from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer, Comment
from django.core.paginator import Paginator
from .forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
