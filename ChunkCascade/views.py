from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Comment
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm


@login_required
def homepage(request):
    questions = Question.objects.all()
    return render(request, "ChunkCascade/homepage.html",
                  {"questions": questions})


@login_required
def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    return render(request, 'ChunkCascade/question_detail.html', {
        "question": question,
        "pk": pk,
    })


@csrf_exempt
@require_POST
def start_timer(request):
    data = json.loads(request.body.decode("utf-8"))
    return JsonResponse({"status": "ok", "request_data": data})


@login_required
def profile_page(request):
    return render(request, 'ChunkCascade/profile_page.html')


@login_required
def question_new(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.question_owner = request.user
            question.save()
            return redirect('question-detail', pk=question.pk)
    else:
        form = QuestionForm()

    return render(request, 'ChunkCascade/question_new.html', {"form": form})
