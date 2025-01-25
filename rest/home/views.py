from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from home.models import Question, Vote
from home.serializers import QuestionSerializer
from django.utils.text import slugify
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class QuestionViewSet(ViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        """give list of questions./"""

        ser_data = self.serializer_class(instance=self.queryset, many=True)
        return Response({'questions_data': ser_data.data})

    def retrieve(self, request, *args, **kwargs):
        """give one of the questions./"""

        question_instance = self.queryset.get(pk=kwargs['pk'])
        ser_data = self.serializer_class(instance=question_instance, many=False)
        return Response({'question_data': ser_data.data})

    def create(self, request, *args, **kwargs):
        """create a new question with given data./"""

        ser_data = self.serializer_class(data=request.data)
        if ser_data.is_valid(raise_exception=True):
            ser_data.validated_data['user'] = request.user
            ser_data.validated_data['slug'] = slugify(ser_data.validated_data['title'][:30])
            ser_data.save()
            return Response(
                {
                    'message': 'question created successfully.',
                    'question_data': ser_data.data
                }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """update a question with given data(no field most be blank)./"""

        question_instance = self.queryset.get(pk=kwargs['pk'])
        if request.user != question_instance.user:
            return Response({'message': 'You are not allowed to edit this question.'},
                            status=status.HTTP_403_FORBIDDEN)
        ser_data = self.serializer_class(instance=question_instance, data=request.data)
        if ser_data.is_valid(raise_exception=True):
            ser_data.save()
            return Response(
                {
                    'message': 'question updated successfully.',
                    'updated_data': ser_data.data
                }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        """update a question with given data(you can fill only one of fields)./"""

        question_instance = self.queryset.get(pk=kwargs['pk'])
        if request.user != question_instance.user:
            return Response({'message': 'You are not allowed to edit this question.'},
                            status=status.HTTP_403_FORBIDDEN)
        ser_data = self.serializer_class(instance=question_instance, data=request.data, partial=True)
        if ser_data.is_valid(raise_exception=True):
            ser_data.save()
            return Response(
                {
                    'message': 'question updated successfully.',
                    'updated_data': ser_data.data,
                }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        question_instance = self.queryset.get(pk=kwargs['pk'])
        if request.user != question_instance.user:
            return Response({'message': 'You are not allowed to destroy this question.'},
                            status=status.HTTP_403_FORBIDDEN)
        question_instance.delete()
        return Response({'message': 'question deleted successfully.'}, status=status.HTTP_200_OK)


class CreateVoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, question_id):
        """like a post./"""

        question_instance = get_object_or_404(Question, id=question_id)
        like = Vote.objects.filter(user=request.user, question=question_instance)
        if like.exists():
            return Response({'message': 'you already liked this question.'}, status=status.HTTP_400_BAD_REQUEST)
        Vote.objects.create(user=request.user, question=question_instance)
        return Response({'message': 'you liked this question.'}, status=status.HTTP_200_OK)


