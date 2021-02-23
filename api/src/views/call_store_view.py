from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time as t
from api.src.containers.store import store
import json
from api.models import Note
import os
from django.conf import settings


@csrf_exempt
def get_data_store_pagination(request):
    data = {'error': False}
    context = {"error": True, "message": "Sai tham số"}
    t_1 = t.time()
    if request.method == 'POST':
        try:
            try:
                # get params is body
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                data['search'] = body['search']
                data['limit'] = body['limit']
                data['page'] = body['page']
                data['user_id'] = body['user_id']
                data['order_by'] = body['order_by']
            except:
                return JsonResponse(context, status=200)
            # Get URL
            # Get Info From data
            ax = store(data, context, t_1)
            if ax['error']:
                return JsonResponse(context, status=200)

            # # Result
            context['data'] = data
            context['error'] = False
            context['message'] = "Success"
            return JsonResponse(context, status=200)

        except NameError:
            return JsonResponse(context, status=200)
    else:
        return JsonResponse({'error': True, 'message': 'GET'}, status=200)


@csrf_exempt
def get_data_store_detail(request):
    data = {'error': False}
    context = {"error": True, "message": "Sai tham số"}
    if request.method == 'POST':
        try:
            try:
                # get params is body
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                data['id'] = body['id']
            except:
                return JsonResponse(context, status=200)
            # Get URL
            try:
                s = Note.objects.get(pk=data['id'])
            except Note.DoesNotExist:
                context['message'] = "key không tồn tại"
                return JsonResponse(context, status=200)

            data['url'] = s.url
            data['name'] = s.name
            context['data'] = data
            context['error'] = False
            context['message'] = "Success"
            return JsonResponse(context, status=200)

        except NameError:
            return JsonResponse(context, status=200)
    else:
        return JsonResponse({"error": False, "message": "API NOT REQUEST METHOD GET"}, status=200)


@csrf_exempt
def get_data_store_update(request):
    data = {'error': False}
    context = {"error": True, "message": "Sai tham số"}
    if request.method == 'POST':
        try:
            try:
                # get params is body
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                data['id'] = body['id']
                data['name'] = body['name']
            except:
                return JsonResponse(context, status=200)
            # Get URL

            url_folder = settings.MEDIA_ROOT + "/capture/"
            url_new = "/media/capture/"

            try:
                s = Note.objects.get(pk=data['id'])

                # Get code random to date
                date_random = s.url.split('/')[-1].split('_')[0] + "_"

                # Rename image
                os.rename(url_folder + date_random + s.name, url_folder + date_random + data['name'])

                # Change url code
                s.url = url_new + date_random + data['name']
                s.name = data['name']
                s.save()
            except Note.DoesNotExist:
                context['message'] = "ID không tồn tại"
                return JsonResponse(context, status=200)

            context['data'] = data
            context['error'] = False
            context['message'] = "Success"
            return JsonResponse(context, status=200)

        except NameError:
            return JsonResponse(context, status=200)
    else:
        return JsonResponse({"error": False, "message": "API NOT REQUEST METHOD GET"}, status=200)



@csrf_exempt
def get_data_store_delete(request):
    data = {'error': False}
    context = {"error": True, "message": "Sai tham số"}
    t_1 = t.time()
    if request.method == 'POST':
        try:
            try:
                # get params is body
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                data['id'] = body['id']
            except:
                return JsonResponse(context, status=200)
            # Get URL


            try:
                s = Note.objects.get(pk=data['id'])
                s.status = False
                s.save()
            except Note.DoesNotExist:
                context['message'] = "ID không tồn tại"
                return JsonResponse(context, status=200)

            context['data'] = data
            context['error'] = False
            context['message'] = "Success"
            return JsonResponse(context, status=200)

        except NameError:
            return JsonResponse(context, status=200)
    else:
        return JsonResponse({"error": False, "message": "API NOT REQUEST METHOD GET"}, status=200)




