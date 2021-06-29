from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from website.models import Blog
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

class ProjectList(APIView):
    pass

class BlogList(APIView):
    permission_classes =  (IsAuthenticatedOrReadOnly)

    def get(self, request, *args, **kwargs):
        articles = Blog.objects.all()

    def post(self, request, *args, **kwargs):
        #serializer = serializers.BlogSerializer()
        pass

