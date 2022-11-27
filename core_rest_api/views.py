from django.shortcuts import render
from .models import *
from rest_framework import viewsets, serializers, permissions
from .serializer import *
from .permissions import *
from rest_framework.authentication import TokenAuthentication


class NewsApi(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        for item in data.data:
            categ = NewsCategory.objects.get(pk=item['category'])
            print(categ.name)

        return data
    def create(self, request, *args, **kwargs):
        if request.user.username != 'admin':
            raise serializers.ValidationError("Вы не админ!")
        data = super().create(request, *args, **kwargs)
        if data.data['user'] == request.user.pk:
            raise serializers.ValidationError("Название слишко корокое")
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs)
        print(request.user.username)
        print(data.data['titel'])
        return data

class NewsCategoryApi(viewsets.ModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("Метод удаления не доступен!")


# def index(request):
#     context = {
#         'title':"Главная страница",
#         "content":News.objects.all()
#     }


#     return render(request, "core_rest_api/index.html", context)
# Create your views here.
