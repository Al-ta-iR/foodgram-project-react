from djoser.views import UserViewSet
from rest_framework import viewsets

from .serializers import CustomUserSerializer, IngredientSerializer, TagSerializer
from recipes.models import Ingredient, Tag


class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
