from django.shortcuts import render

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework import status, permissions, serializers, viewsets
from .models import RetailPoint, Visit, Employee


class RetailPointSerializer(serializers.ModelSerializer):
    employee = serializers.ReadOnlyField(source='employee.name')

    class Meta:
        model = RetailPoint
        fields = ['id', 'title', 'employee', ]


class RetailPointViewSet(viewsets.ModelViewSet):

    serializer_class = RetailPointSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, *args, **kwargs):
        return RetailPoint.objects.filter(employee__phone=self.request.query_params.get('phone'))


class VisitSerializer(serializers.ModelSerializer):
    
    retail_point = serializers.ReadOnlyField(source='retail_point.title')

    class Meta:
        model = Visit
        fields = ['retail_point', 'visit_date', 'coordinates']


class VisitViewSet(viewsets.ModelViewSet):

    serializer_class = VisitSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        retail_point = get_object_or_404(RetailPoint, id=self.request.data.get('retail'))
        coordinates = self.request.data.get('coordinates')
        serializer.save(retail_point=retail_point, coordinates=coordinates)


retail_points = RetailPointViewSet.as_view({
    'get': 'list',
})

visit = VisitViewSet.as_view({
    'post': 'create'
})