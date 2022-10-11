from django.contrib.auth.models import User
from rest_framework import serializers, validators
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )
        return user


class RegisterDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ('address','mobile','department')

class RegisterPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ('address','mobile')

class RegisterNurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nurse
        fields = ('address','mobile')

class RegisterReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Receptionist
        fields = ('address','mobile')

class AddPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ('address','mobile','status')