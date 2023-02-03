from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .views import ArticleRetrieveUpdateDestroyAPIView,Article
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

schema_view = get_schema_view(
    openapi.Info(title="ecommerce API", default_version="v1"),
    public=True,
)
app_name = 'api'

urlpatterns = [
    path("docs/",schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    
    path("token/", TokenObtainPairView.as_view(), name="login"),
    
    path('articles/<slug>',ArticleRetrieveUpdateDestroyAPIView.as_view()),
    
    path('articles',Article.as_view())
    
]