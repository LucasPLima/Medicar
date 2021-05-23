from rest_framework import serializers
from .models import User
from rest_framework import exceptions
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['first_name', 'last_name','username', 'email', 'password']
        extra_kwargs ={
            'password':{'write_only': 'password'}
        }
    
    def validate(self,data):
        def validate_email(data):
            try:
                user = User.objects.get(email=data['email'])
                raise serializers.ValidationError({'email':'Email já cadastrado!'})
            except User.DoesNotExist:
                pass

        validate_email(data)
        return data

    def save(self,):
        new_user = User(username=self.validated_data['username'], 
                        email=self.validated_data['email'],
                        first_name=self.validated_data['first_name'],
                        last_name=self.validated_data['last_name'],
                        )
        new_user.set_password(self.validated_data['password'])
        new_user.save()
        return new_user