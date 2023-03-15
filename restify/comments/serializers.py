from rest_framework.serializers import ModelSerializer
from .models import Comments


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'author',
            'content',
            'address_type',
            'address_id'
        ]


class CommentsSerializerCreate(ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'content',
            'address_type',
            'address_id'
        ]
