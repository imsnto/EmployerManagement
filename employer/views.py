from django.http import Http404
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employer
from .serializers import EmployerSerializer
from .permissions import IsOwnerOfEmployer

class ListCreateEmployerAPIView(APIView):
    """This class is responsible for creating a new employer and return list of the employers"""
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """This method is responsible for creating a new employer"""
        serializer = EmployerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """This method is responsible for returning the list of employers (only the current user is associated with it"""
        employers = Employer.objects.filter(user=request.user)
        serializer = EmployerSerializer(employers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployerDetailUpdateDeleteAPIView(APIView):
    """This class is responsible for getting single employer details and updating and deleting"""
    permission_classes = [IsAuthenticated, IsOwnerOfEmployer]

    def get_object(self, pk):
        """This method return a single employer record if exists. Otherwise, raise exception"""
        try:
            employer = get_object_or_404(Employer, pk=pk)
            self.check_object_permissions(self.request, employer)
            return employer
        except Employer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """This method is responsible for returning the employer details"""
        employer = self.get_object(pk)
        serializer = EmployerSerializer(employer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        """This method is responsible for updating(partial) the employer details"""
        employer = self.get_object(pk)
        serializer = EmployerSerializer(employer, data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        """This method is responsible for updating the employer details"""
        employer = self.get_object(pk)
        serializer = EmployerSerializer(employer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """This method is responsible for deleting an employer record"""
        employer = self.get_object(pk)
        employer.delete()
        return Response({
          "success": f"Employer {employer.contact_person_name} was deleted.",
            "data": EmployerSerializer(employer).data
        },status=status.HTTP_204_NO_CONTENT)

