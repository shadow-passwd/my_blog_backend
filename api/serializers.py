from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import UserProfile, Post, TestImage, Base64Image


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestImage
        fields = '__all__'


class Base64ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base64Image

        fields = '__all__'


class SinglePostSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data.pop('refresh', None)  # remove refresh from the payload
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['user'] = self.user.username
        data['userid'] = self.user.id
        return data


# class TestImageModelSerializer(serializers.ModelSerializer):
#     image=Base64ImageField()
#     class meta:
#         model=TestImage
#         fields= '__all__'
#     def create(self, validated_data):
#         image=validated_data.pop('image')
#         user=validated_data.pop('user')
#         return TestImage.objects.create(user=user,image=image)
