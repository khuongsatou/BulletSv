from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time as t
# from api.src.containers.store import store
import json
import requests


def handle_notification():
    serverToken = 'AAAAqLDMZko:APA91bGcwgG3tBNf7cLX6rHX3EoqyUrV1qW3zo_25XubeKJuE9Vb2j5FCv2r5OEB2Q_UdLYuH1FFHczrZS96l8Jv7934g0_rppeuaEjBkm41VIupYOfDZ7xJ_cvCUPfDNfF3ph4kUKPQ'


    deviceToken = 'eQETgg_XRz6gVXuL2_j9m0:APA91bHWdWa-9_2W35R1FDdvTecOqTQ8_DjGLAb7SWusTwxFrlm1OPWNeBfJd5WC_P5NOnqLZoEQCNcvG5g3hyj0411TMc5Hhpg3l0NlxkBSMChD0NH583TTKnXWXw0Dq18tNfei5OyS'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
    }

    body = {
        'notification': {'title': 'Sending push form python script',
                         'body': 'New Message'
                         },
        'to':
            deviceToken,
        'priority': 'high',
        #   'data': dataPayLoad,
    }
    response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())
    return response.json()



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
            # Get Info From data
            # ax = store(data, context, t_1)
            # if ax['error']:
            #     return JsonResponse(context, status=200)

            data = handle_notification()
            # # Result
            context['data'] = data
            context['error'] = False
            context['message'] = "Success"
            return JsonResponse(context, status=200)

        except NameError:
            return JsonResponse(context, status=200)
    else:
        return JsonResponse({'error': True, 'message': 'GET'}, status=200)

