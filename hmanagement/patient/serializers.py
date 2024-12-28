from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password"
        ]
    
    def save(self):
        username = self.validated_data["username"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        password2 = self.validated_data["confirm_password"]

        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]

        if password != password2:
            raise serializers.ValidationError({
                "error": "Password doesn\'t match"
            })
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                "error": "Email already exists"
            })
        account = User(username=username, email=email, first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.save()
        return account