from django.db import models
from django.contrib.auth.models import User
from django.db.models import FilePathField

from django_base64field.fields import Base64Field

import base64
from django.core.files.base import ContentFile


def get_location(instance, filename):
    location = 'account/'+str(instance.user)+'/'+str(filename)
    return location


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    profile_pic_base64 = models.TextField(blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Users Profile'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    genre = models.CharField(max_length=254)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'


def get_image_filename(instance, filename):
    print('---------------'+str(filename))
    image_save_location = "post_images/" + \
        str(instance.user.id)+"/"+str(filename)
    print(str(image_save_location))
    return image_save_location


class TestImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=get_image_filename)


def decode_base64_image(data, filename):
    decoded_file = base64.b64decode(data)
    return ContentFile(decoded_file, filename)


class Base64Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    filename = models.CharField(max_length=254)
    base64data = models.TextField()
    title = models.CharField(max_length=254)
    genre = models.CharField(max_length=254)
    description = models.TextField()

    def save(self, *args, **kwargs):
        print("------------------------")
        images_base64data = self.base64data[0:len(
            self.base64data)-1].split(':')
        filenames = self.filename[0:len(self.filename)-1].split(':')
        post = Post(user=self.user, title=self.title,
                    genre=self.genre, description=self.description)
        post.save()
        for i in range(len(images_base64data)):
            testimage = TestImage(user=self.user, image=decode_base64_image(
                images_base64data[i], str(post.id)+"/"+filenames[i]))
            testimage.save()
            # testimage=TestImage(user=self.user,image=decode_base64_image(self.base64data,self.filename))
            # testimage.save()

        print("---------------------------------")
