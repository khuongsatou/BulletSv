from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from .tasks import sleepy, send_email_task
from django.http import HttpResponse
from home.notify import handle_notification

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'pages/login.html')




def index(request):
    # handle_notification()
    sleepy.delay(12)
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')


