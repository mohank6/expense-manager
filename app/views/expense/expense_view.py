from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from . import expense_business


@csrf_exempt
def get_expense_by_id(request, id):
    if not request.method == 'GET':
        return JsonResponse({'message': 'Method not allowed'}, 400)
    try:
        message, status = expense_business.handle_get_expense(id)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, 500)


@csrf_exempt
def get_expenses_by_user(request, id):
    if not request.method == 'GET':
        return JsonResponse({'message': 'Method not allowed'}, 400)
    try:
        message, status = expense_business.handle_get_expenses_by_user(id)
        return JsonResponse(message, status=status, safe=False)
    except:
        return JsonResponse({'message': 'Server Error'}, 500)


@csrf_exempt
def get_total_amount_spent_by_user(request, id):
    if not request.method == 'GET':
        return JsonResponse({'message': 'Method not allowed'}, 400)
    try:
        message, status = expense_business.handle_get_total_amount_spent_by_user(id)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, 500)


@csrf_exempt
def create_expense(request):
    if not request.method == 'POST':
        return JsonResponse({'message': 'Method not allowed'}, 400)
    try:
        data = json.loads(request.body)
        message, status = expense_business.handle_create_expense(data)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, 500)


@csrf_exempt
def update_expense(request, id):
    if not request.method == 'PATCH':
        return JsonResponse({'message': 'Method not allowed'}, 400)
    try:
        data = json.loads(request.body)
        message, status = expense_business.handle_update_expense(data, id)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, 500)


@csrf_exempt
def delete_expense(request, id):
    if not request.method == 'DELETE':
        return JsonResponse({'message': 'Method not allowed'}, 400)
    try:
        message, status = expense_business.handle_delete_expense(id)
        return JsonResponse(message, status=status)
    except:
        return JsonResponse({'message': 'Server Error'}, 500)
