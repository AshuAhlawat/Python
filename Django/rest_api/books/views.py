from .models import Novel
from .serializers import NovelSerializer

# from rest_framework.decorators import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser

# from rest_framework.decorators import api_view



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import generics
# from rest_framework import mixins
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated


# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    
#     serializer_class = NovelSerializer
#     queryset = Novel.objects.all()
#     lookup_field = 'username'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
 
#     def get(self, request, id = None):
 
#         if id:
#             return self.retrieve(request)
 
#         else:
#            return self.list(request)
 
#     def post(self, request):
#         return self.create(request)
 
#     def put(self, request, username=None):
#         return self.update(request, username)
 
#     def delete(self, request, username):
#         return self.destroy(request, username)

class allNovelAPIView(APIView):
    
    def get(self,request):
        
        novels = Novel.objects.all()
        serializer = NovelSerializer(novels, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        
        serializer = NovelSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class oneNovelAPIView(APIView):
    
    def get_object(self, username):
        
        try:
            return Novel.objects.get(user=username)
        except Novel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, username):
        
        novel = self.get_object(username)
        serializer = NovelSerializer(novel) 
         
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, username):
        
        novel = self.get_object(username)
        serializer = NovelSerializer(novel, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, username):
        
        novel = self.get_object(username)
        
        novel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# @csrf_exempt
# @api_view(['GET','POST'])
# def data_all(request):
    
#     if request.method == 'GET':
#         novels = Novel.objects.all()
#         serializer = NovelSerializer(novels, many=True)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = NovelSerializer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# @api_view(['GET','PUT','DELETE'])
# def data_one(request, username):
#     try:
#         novel = Novel.objects.get(user=username)
#     except Novel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = NovelSerializer(novel)  
#         return Response(serializer.data, status= status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = NovelSerializer(novel, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         novel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


