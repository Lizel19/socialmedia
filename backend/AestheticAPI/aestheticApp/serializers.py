from rest_framework.serializers import ModelSerializer
from .models import User, Outfit
from rest_framework import serializers


class OutfitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Outfit
        fields = ['title', 'cover']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
      
   class PostingSerializer(ModelSerializer):
    class Meta:
        model = Posting
        fields = ['user_id', 'content', 'image', 'created_at']

class OutfitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Outfit
        fields = ['user_id', 'content', 'image', 'date_created']
