from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from . import user_business


@csrf_exempt
def signup(request):
    if not request.method == 'POST':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        data = json.loads(request.body)
        message, status = user_business.handle_signup(data=data)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)


@csrf_exempt
def update_profile(request, id):
    if not request.method == 'PATCH':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        data = json.loads(request.body)
        message, status = user_business.handle_update(data=data, id=id)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)


@csrf_exempt
def get_user_profile_by_id(request, id):
    if not request.method == 'GET':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        message, status = user_business.handle_get_user(id=id)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)


@csrf_exempt
def get_user_profile_by_username(request, username):
    if not request.method == 'GET':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        message, status = user_business.handle_get_user(username=username)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)


@csrf_exempt
def delete_user(request, id):
    if not request.method == 'DELETE':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        message, status = user_business.handle_delete(id)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)
