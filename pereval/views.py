import django_filters
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import *
from .models import *


class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['fam', 'name', 'otc', 'email']

    # def create(self, request, *args, **kwargs):
    #     serializer = PerevalsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             {
    #                 'status': status.HTTP_200_OK,
    #                 'message': 'Успех!',
    #                 'id': serializer.data['id'],
    #             }
    #         )

    #     if status.HTTP_400_BAD_REQUEST:
    #         return Response(
    #             {
    #                 'status': status.HTTP_400_BAD_REQUEST,
    #                 'message': 'Некорректный запрос',
    #                 'id': None,
    #             }
    #         )

    #     if status.HTTP_500_INTERNAL_SERVER_ERROR:
    #         return Response(
    #             {
    #                 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
    #                 'message': 'Ошибка при выполнении операции',
    #                 'id': None,
    #             }
    #         )

class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalsViewSet(viewsets.ModelViewSet):
    queryset = Perevals.objects.all()
    serializer_class = PerevalsSerializer

    # создание перевала
    def create(self, request, *args, **kwargs):
        serializer = PerevalsSerializer(data=request.data)

        """Результаты метода: JSON"""
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data['id'],
            })
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad Request',
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка подключения к базе данных',
                'id': None,
            })
    # редактирование объекта перевала, если статус все еще new и данные о самом пользователе не меняются.
    def partial_update(self, request, *args, **kwargs):
        perevals = self.get_object()
        if perevals.status == 'new':
            serializer = PerevalsSerializer(perevals, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'state': '1',
                    'message': 'Запись успешно изменена'
                })
            else:
                return Response({
                    'state': '0',
                    'message': serializer.errors
                })
        else:
            return Response({
                'state': '0',
                'message': f"Не удалось обновить запись, так как сведения уже у модератора и имеют статус: {perevals.get_status_display()}"
            })

# список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
class EmailAPIView(generics.ListAPIView):
    serializer_class = PerevalsSerializer
    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if Perevals.objects.filter(user__email=email):
            data = PerevalsSerializer(Perevals.objects.filter(user__email=email), many=True).data
            api_status = status.HTTP_200_OK
        else:
            data = {
                'message': f'Не существует пользователя с таким email - {email}'
            }
            api_status = 404
        return JsonResponse(data, status=api_status, safe=False)