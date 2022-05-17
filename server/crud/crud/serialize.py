from rest_framework import serializers
from crud.models import DetailsModel


# класс, отвечающий за сериализацию данных
class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsModel
        fields = '__all__'    # выборка из всех полей