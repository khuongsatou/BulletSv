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