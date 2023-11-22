from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NavItemsSerializer, AdvantageTileSerializer
from .models import NavItems, AdvantageTileItems

class NavItemsViews(APIView):
    def get(self, request, id=None):
        if id:
            item = NavItems.objects.get(id=id)
            serializer = NavItemsSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = NavItems.objects.all().order_by("nav_id")
        serializer = NavItemsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
class AdvantageTileItemsViews(APIView):
    def get(self, request, id=None):
        if id:
            item = AdvantageTileItems.objects.get(id=id)
            serializer = AdvantageTileSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = AdvantageTileItems.objects.all()
        serializer = AdvantageTileSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)