from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from api.models import Employee,Leave,LeaveLedger

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

# Serializers define the API representation.
class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('code','name', 'no_of_days')

# ViewSets define the view behavior.
class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

# Serializers define the API representation.
class ApplyLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveLedger
        fields = ('leave_code','leave_summary','from_date','to_date')

# ViewSets define the view behavior.
class ApplyLeaveViewSet(viewsets.ModelViewSet):
    queryset = LeaveLedger.objects.all()
    serializer_class = ApplyLeaveSerializer