from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car, Mark
from .serializers import CarSerializer

# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


class CarAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        return Response({'cars': CarSerializer(cars, many=True).data})

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'car': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        print(f'pk={pk}')
        if not pk:
            return Response({'error': 'Метод PUT не определен!!!'})
        try:
            instance = Car.objects.get(pk=pk)
            print(f'instance={instance}')
        except:
            return Response({'error': 'Запсиь не найдена'})

        serializer = CarSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'car': serializer.data})
