from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from api.models import Employee

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Serializers define the API representation.
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('url','employee_code', 'qualification', 'name', 'msys_email', 'designation')

# ViewSets define the view behavior.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer