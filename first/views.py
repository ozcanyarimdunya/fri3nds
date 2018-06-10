from celery.result import AsyncResult
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from first.tasks import simple_task


# Create your views here.
def index(request):
    return render(request, 'index.html')


def start(request):
    const = 81
    taskId = simple_task.delay(const)
    data = {
        "result": "Task started",
        "taskId": taskId.id,
    }

    return JsonResponse({"data": data})


@csrf_exempt
def status(request):
    taskId = request.POST['taskId']

    if taskId is not None:
        task = AsyncResult(taskId)
        data = {
            "state": task.state,
            "result": task.result
        }
        return JsonResponse({"data": data})
    else:
        return JsonResponse({"data": "No task"})
