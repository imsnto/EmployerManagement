from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employer
from .serializers import EmployerSerializer


class ListCreateEmployerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = EmployerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        employers = Employer.objects.all()
        serializer = EmployerSerializer(employers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployerDetailUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Employer.objects.get(pk=pk)
        except Employer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employer = self.get_object(pk)
        serializer = EmployerSerializer(employer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        employer = self.get_object(pk)
        serializer = EmployerSerializer(employer, data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        employer = self.get_object(pk)
        serializer = EmployerSerializer(employer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employer = self.get_object(pk)
        employer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

