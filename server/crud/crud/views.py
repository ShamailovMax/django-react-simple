from crud import serialize
from crud.models import DetailsModel
from crud.serialize import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Запросы get и post
class DetailsTable(APIView):
    def get(self, request):
        detailsObj = DetailsModel.objects.all()
        dlSerializeObj = DetailsSerializer(detailsObj, many = True)
        return Response(dlSerializeObj.data)

    def post(self, request):
        serialize_obj = DetailsSerializer(data=request.data)
        if serialize_obj.is_valid():
            serialize_obj.save()
            return Response(200)
        return Response(serialize_obj.errors)


# update запрос
class DetailsUpdate(APIView):
    def post(self, request, pk):
        try:
            detail_obj = DetailsModel.objects.get(pk=pk)
        except:
            return Response('Not found in Database')

        serialize_obj = DetailsSerializer(detail_obj, data=request.data)
        if serialize_obj.is_valid():
            serialize_obj.save()
            return Response(200)
        return Response(serialize_obj.errors)


# delete запрос
class DetailsDelete(APIView):
    def post(self, request, pk):
        try:
            detail_obj = DetailsModel.objects.get(pk=pk)
        except:
            return Response('Not found in Database')
        detail_obj.delete()
        return Response(200)