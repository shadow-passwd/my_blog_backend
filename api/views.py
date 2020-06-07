from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import UserProfile, Post, TestImage, Base64Image
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer, PostSerializer, TestImageSerializer, Base64ImageSerializer, SinglePostSerializer, MyTokenObtainPairSerializer
from rest_framework.response import Response

# Create your views here.


class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class PostView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TestImageView(ListCreateAPIView):
    queryset = TestImage.objects.all()
    serializer_class = TestImageSerializer


class Base64ImageView(ListCreateAPIView):
    queryset = Base64Image.objects.all()
    serializer_class = Base64ImageSerializer


class SinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = SinglePostSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# class TestModelImageView(APIView):
#     def get(self,request,format=None):
#         images = TestImage.objects.all()
#         serializer=TestImageModelSerializer(data=images)
#         if serializer.is_valid():
#             return Response(images,status=201)
#         return Response(serializer.errors,status=400)

#     def post(self,request,format=None):
#         serializer = TestImageModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

    #         usernames = [user.username for user in User.objects.all()]
    # return Response(usernames)
