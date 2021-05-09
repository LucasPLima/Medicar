from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'email', 'password']
        extra_kwargs ={
            'password':{'write_only': 'password'}
        }
    
    def validate(self,data):
        def validate_email(data):
            try:
                user = User.objects.get(email=data['email'])
                raise serializers.ValidationError({'email':'A user with that email already exists!'})
            except User.DoesNotExist:
                pass

        validate_email(data)
        return data

    def save(self,):
        new_user = User(username=self.validated_data['username'], 
                        email=self.validated_data['email'],
                        )
        new_user.set_password(self.validated_data['password'])
        new_user.save()
        return new_user