from rest_framework import serializers
from .models import User, Tasks

#O serializer é chamado para pegar um elemento e transformar em json.
#Quando chamamos esse método pedimos que ele retorne tudo do objeto graças ao método "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  #Isso aqui quer dizer que a nossa API vai devolver todos os campos

class TasksSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Tasks
        fields = "__all__"