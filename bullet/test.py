import requests
import json

serverToken = 'AAAAqLDMZko:APA91bGcwgG3tBNf7cLX6rHX3EoqyUrV1qW3zo_25XubeKJuE9Vb2j5FCv2r5OEB2Q_UdLYuH1FFHczrZS96l8Jv7934g0_rppeuaEjBkm41VIupYOfDZ7xJ_cvCUPfDNfF3ph4kUKPQ'
deviceToken = 'faPQ9RrjTBKEQtdr3K03O2:APA91bH8YiktZvaQd7GwXgB8tTovPBlN7qZD8PWOx8rfsbbvVCLO8klcIAMcNoTA7K_chadJpl944Q34PK0tK0X_LeXv2gvZ2l9DEMtAcFbJyPI3eL7luqVTMCDJ_boq2xdtifIbE6AB'

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
