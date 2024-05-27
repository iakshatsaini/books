from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from rest_framework.response import Response
from .models import bookList
import json
from django.views.decorators.csrf import csrf_exempt
from app_2.serialzers import bookListSerializers
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view

@method_decorator(csrf_exempt, name='dispatch')
class bookListAPI(View):
    def get(self, request, *args, **kwrgs):
        if request.method == 'GET':
            id = request.GET.get('id', None)
            if id is not None:
                data = bookList.objects.get(id=id)
                data = bookListSerializers(data)
                get_data = data.data
                return JsonResponse({"data":get_data, "status":200})
            else:
                data = bookList.objects.all()
                data = bookListSerializers(data, many = True)
                get_data = data.data
                return JsonResponse({"data":get_data, "status":200})
            
            
    def post(self, request, *args, **kwrgs):
        if request.method == 'POST':
            data = json.loads(request.body)
            data_serialize = bookListSerializers(data=data)
            if data_serialize.is_valid():
                data_serialize.save()
                return JsonResponse({"message":"Hello data inserted successfuly", "status":200})
            error = data_serialize.errors
            return JsonResponse({"errors":error})
        
    def put(self, request, *args, **kwrgs):
        if request.method == 'PUT':
            requestData = json.loads(request.body)
            id = requestData.get('id')
            if id is not None:
                bookData = bookList.objects.get(id=id)
                
                #  For partial update - All data not required
                # serializer = bookListSerializers(bookData, data=requestData, partial=True)
                
                #  for complete update - All data required
                serializer = bookListSerializers(bookData, data=requestData)
                if serializer.is_valid():
                    serializer.save()
                return JsonResponse({"message":"Data updated successfuly", "status":200})
            error = serializer.errors
            return JsonResponse({"errors":error})
    
    
    def delete(self, request, *args, **kwrgs):
        if request.method == 'DELETE':
            id = request.GET.get('id')
            if id is not None:
                bookData = bookList.objects.get(id=id)
                bookData.delete()
                return JsonResponse({"message":f"book successfuly deleted with the id {id} ", "status":200})
            else:
                return JsonResponse({"message":"id missing, Please check", "status":status.HTTP_404_NOT_FOUND})
    




#  Function based view
def home(request):
    return HttpResponse("This site is working and msg from app2")

@csrf_exempt
# For methods validation in function based view API
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def insertRecord(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            data_serialize = bookListSerializers(data=data)
            if data_serialize.is_valid():
                data_serialize.save()
                return Response({"message":"Hello data inserted successfuly", "status":200})
            error = data_serialize.errors
            return Response({"errors":error, "status":status.HTTP_500_INTERNAL_SERVER_ERROR}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if request.method == 'GET':
            id = request.GET.get('id', None)
            if id is not None:
                data = bookList.objects.get(id=id)
                data = bookListSerializers(data)
                get_data = data.data
                return JsonResponse({"data":get_data, "status":200})
            else:
                data = bookList.objects.all()
                data = bookListSerializers(data, many = True)
                get_data = data.data
                return JsonResponse({"data":get_data, "status":200})
            
        if request.method == 'PUT':
            requestData = json.loads(request.body)
            id = requestData.get('id')
            if id is not None:
                bookData = bookList.objects.get(id=id)
                
                #  For partial update - All data not required
                # serializer = bookListSerializers(bookData, data=requestData, partial=True)
                
                #  for complete update - All data required
                serializer = bookListSerializers(bookData, data=requestData)
                if serializer.is_valid():
                    serializer.save()
                return JsonResponse({"message":"Data updated successfuly", "status":200})
            error = serializer.errors
            return JsonResponse({"errors":error})
        
        if request.method == 'DELETE':
            id = request.GET.get('id')
            if id is not None:
                bookData = bookList.objects.get(id=id)
                bookData.delete()
                return JsonResponse({"message":f"book successfuly deleted with the id {id} ", "status":200})
            else:
                return JsonResponse({"message":"id missing, Please check", "status":status.HTTP_404_NOT_FOUND})
        
        if request.method == 'PATCH':
            return JsonResponse({"message":"Msg for patch request", "status":200})
             
    except Exception as e:
        return JsonResponse({"message":str(e), "status":status.HTTP_404_NOT_FOUND})
    