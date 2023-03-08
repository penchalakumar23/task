from rest_framework import serializers
from .models import User

class Userserializer(serializers.ModelSerializer):
    # password=serializers.CharField(max_length=8,write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","name","Email","password","confirm_password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # def __str__(self):
    #     return self.name
    def create(self, validated_data,**kwargs):
        user=User.objects.create(
            Email=validated_data['Email'],
            password=validated_data['password']
        )
        return user