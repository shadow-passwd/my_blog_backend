from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, UserProfileDetailView, PostView, TestImageView, Base64ImageView, SinglePostView, MyTokenObtainPairView

urlpatterns = [
    # gets all user profiles and create a new profile
    path("accounts/allprofiles",
         UserProfileListCreateView.as_view(), name="allprofiles"),
    # retrieves profile details of the currently logged in user
    path("accounts/profile/<int:pk>",
         UserProfileDetailView.as_view(), name="profile"),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain'),


    path('post/<int:pk>', SinglePostView.as_view(), name='singel_post'),
    path("post/", PostView.as_view(), name="post"),
    # path('test/',TestImageView.as_view(),name='test'),
    path('test/', TestImageView.as_view(), name='test'),
    path('get/', Base64ImageView.as_view(), name='test'),


]
