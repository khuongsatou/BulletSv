# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time as t
# from api.src.containers.store import store
import json
import requests
from ce.task import add


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'pages/login.html')


class RunTask(View):
    def get(self, request):
        return render(request, 'pages/login.html')


def handle_notification():
    result = add.delay(2,4)
    print(str(result))
    return result



@csrf_exempt
def get_notify(request):
    data = {'error': False}
    context = {"error": True, "message": "Sai tham số"}
    t_1 = t.time()
    if request.method == 'POST':
        try:
            try:
                # get params is body
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
            except:
                return JsonResponse(context, status=200)
            # Get URL
            # Get Info From datasourc

            data = handle_notification()
            print(data)
            # # Result
            # context['data'] = data
            context['error'] = False
            context['message'] = "Success"
            return JsonResponse(context, status=200)

        except NameError:
            return JsonResponse(context, status=200)
    else:
        return JsonResponse({'error': True, 'message': 'GET'}, status=200)
