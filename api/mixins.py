from .models import Article
from rest_framework.response import Response


class AdminGetMixin:
    def get_queryset(self):
        queryset = Article.objects
        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            return queryset.all()

        return queryset.filter(status="PB")


class AdminCreateMixin:
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            return super().post(request, *args, **kwargs)
        return Response(
            {"error": "you must be authenticated and admin to do this post"}
        )


class AdminUpdateMixin:
    def update(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            return super().update(request, *args, **kwargs)
        return Response(
            {"error": "you must be authenticated and admin to do this update"}
        )


class AdminDestroyMixin:
    def destroy(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        return Response(
            {"error": "you must be authenticated and admin to do this delete"}
        )


class AdminPutMixin:
    def put(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            return super().put(request, *args, **kwargs)
        return Response(
            {"error": "you must be authenticated and admin to do this update"}
        )
        