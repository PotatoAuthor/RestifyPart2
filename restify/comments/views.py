from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import CommentsSerializer
from .models import Comments


class CommentsCreateAPIView(CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=serializer.context.get('request').user)


class CommentsListAPIView(ListAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
