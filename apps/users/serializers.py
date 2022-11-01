from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    top_seller = serializers.BooleanField(source="profile.top_seller")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name","full_name","gender","phone_number","profile_photo","country","city","top_seller"]

        def get_first_name(self,obj):
            return obj.first_name.title()

        def get_last_name(self,obj):
            return obj.last_name.title()
# a two representation field serializer method, we are add the admin field if he is an admin
        def to_representation(self,instance):
            representation = super(UserSerializer,self).to_representation
            (instance)
            if instance.is_superuser:
                representation["admin"] = True

            return representation
#  here we are sub classing
class CreateUserSerializer(UserCreateSerializer):
    # here we are then accessing the serializer's meta we are sub classing from
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id","username","email","first_name","last_name","password"]

