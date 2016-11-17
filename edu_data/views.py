from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from edu_data.models import School
from edu_data.serializers import SchoolSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def schools(request, format=None):
    if request.method == 'GET':
        all_schools = School.objects.all()
        serialized = SchoolSerializer(all_schools, many=True)
        return Response(serialized.data)
