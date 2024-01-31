from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question
from .serializers import PersonSerializer, QuestionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class Home(APIView):
    authentication_classes = [IsAuthenticated,]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    def post(self, request):
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestionSerializer(
            instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(data={'message': 'question deleted'}, status=status.HTTP_200_OK)
