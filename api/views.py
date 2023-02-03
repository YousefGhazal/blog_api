from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticlesSerializer,SingleArticleSerializer
from .mixins import AdminGetMixin,AdminCreateMixin,AdminDestroyMixin,AdminUpdateMixin

class ArticleRetrieveUpdateDestroyAPIView(AdminGetMixin,AdminDestroyMixin,AdminUpdateMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    lookup_field = 'slug'
    
    
class Article(AdminGetMixin,AdminCreateMixin,generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

    
    