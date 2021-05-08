from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'email', 'password']
        extra_kwargs ={
            'password':{'write_only': 'password'}
        }
    
    def save(self,):
        new_user = User(username=self.validated_data['username'], 
                        email=self.validated_data['email'],
                        )
        new_user.set_password(self.validated_data['password'])
        new_user.save()
        return new_user