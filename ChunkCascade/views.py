from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json


def homepage(request):
    return render(
        request,
        "base.html",
    )


@csrf_exempt
@require_POST
def start_timer(request):
    data = json.loads(request.body.decode("utf-8"))
    return JsonResponse({"status": "ok", "request_data": data})
