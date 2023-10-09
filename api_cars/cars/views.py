# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminOrReadOnly

from .models import Car
from .serializers import CarSerializer


class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CarAPIUpdate(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIDestroy(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

#     @action(methods=['get'], detail=False)
#     def lexus(self, request):
#         querry = Car.objects.filter(mark__name='Lexus')
#         serializer = self.get_serializer(querry, many=True)
#         return Response(serializer.data)


# class CarAPIView(APIView):
#     def get(self, request):
#         cars = Car.objects.all()
#         return Response({'cars': CarSerializer(cars, many=True).data})

#     def post(self, request):
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'car': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         print(f'pk={pk}')
#         if not pk:
#             return Response({'error': 'Метод PUT не определен!!!'})
#         try:
#             instance = Car.objects.get(pk=pk)
#             print(f'instance={instance}')
#         except:
#             return Response({'error': 'Запсиь не найдена'})

#         serializer = CarSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'car': serializer.data})
