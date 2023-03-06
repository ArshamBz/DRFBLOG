from rest_framework import serializers
from .models import *


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'create_at')
