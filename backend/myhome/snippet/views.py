
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


from snippet.models import Snippet
from snippet.serializers import SnippetSerializer, SnippetSerializer2


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer2(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer2(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer2(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
    

# ---------------------------------------------------------------------------------------------------------------------------------------------
# Using DRF API views
# request, Response, status. are all part of rest_framework

# REST framework provides two wrappers you can use to write API views.
# The @api_view decorator for working with function based views.
# The APIView class for working with class-based views.

# ----------Using @api_view decorator--------
@api_view(['GET', 'POST'])
def snippet_list2(request, format=None): # format=None is used to specify the format of the response like JSON or HTML.
    
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer2(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SnippetSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail2(request, pk, format=None): # format=None is used to specify the format of the response like JSON or HTML.
    
    try:
        snippet = Snippet.objects.get(pk=pk)

    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SnippetSerializer2(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = SnippetSerializer2(serializer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# --------------using APIView -------------------------------


class SnippetList(APIView):
    
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer2(snippets, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SnippetSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404 # we raise Http404 as we dont want to return Response(status=status.HTTP_404_NOT_FOUND) from this method.
        
    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer2(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer2(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(snippet.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

       
# Bitch we will now use mixins 😈
# mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView,

from rest_framework import mixins
from rest_framework import generics

class SnippetListV2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer2

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    # Thats all bitch.


class SnippetDetailV2(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer2

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    # Thats all bitch.


# Lets trim that pussy little more. 🍑
class SnippetListV3(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer2

class SnippetDetailV3(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer2


# Bitchhhhh thatsss allll......woohoooooooo...............