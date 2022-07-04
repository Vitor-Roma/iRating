from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'This email already exists'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'This username already exists'})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(many=False, read_only=True)
    restaurant_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    product_id = serializers.UUIDField(write_only=True)
    profile = ProfileSerializer(many=False, read_only=True)
    profile_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = models.Rating
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    product_id = serializers.UUIDField(write_only=True)
    profile = ProfileSerializer(many=False, read_only=True)
    profile_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = models.Wishlist
        fields = '__all__'
