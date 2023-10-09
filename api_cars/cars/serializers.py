from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('__all__')

# class CarSerializer(serializers.Serializer):
#     mark = serializers.CharField(max_length=100)
#     model = serializers.CharField(max_length=100)
#     body = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     year = serializers.IntegerField()
#     time_create = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         mark = validated_data.get('mark')
#         validated_data['mark'] = Mark.objects.filter(name=mark)[0]
#         return Car.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         mark = validated_data.get('mark', instance.mark)
#         instance.mark = Mark.objects.filter(name=mark)[0]
#         instance.model = validated_data.get('model', instance.model)
#         instance.body = validated_data.get('body', instance.body)
#         instance.description = validated_data.get(
#             'description',
#             instance.description)
#         instance.year = validated_data.get('year', instance.year)
#         instance.time_create = validated_data.get(
#             'time_create',
#             instance.time_create)
#         instance.save()
#         return instance
