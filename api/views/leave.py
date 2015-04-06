from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from api.models import Leave

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
class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('code','name', 'no_of_days')

# ViewSets define the view behavior.
class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer