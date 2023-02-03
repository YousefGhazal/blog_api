from rest_framework import serializers
from .models import Article


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        
        

class SingleArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title','body',"description","published"]