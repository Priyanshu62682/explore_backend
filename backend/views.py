from django.shortcuts import render
from .models import appuser,question,answer,area_of_interest,expertise_area
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import questionSerializer,answerSerializer

# Create your views here.

class questionList(APIView):
	def get(self,request,id_input):
#		ques= question.objects.filter(asked_by=2)
		cities=area_of_interest.objects.select_related('user_id').filter(user_id=id_input)
		for city in cities:
			q=question.objects.filter(location=city.city)
			if q:
				serializer= questionSerializer(q,many=True)

		cities=expertise_area.objects.select_related('user_id').filter(user_id=id_input)
		
		for city in cities:
			q=question.objects.filter(location=city.city)
			if q:
				serializer= questionSerializer(q,many=True)
		
#		ques= question.objects.filter(location="Roorkee")
		
		return Response(serializer.data)

	def post(self):
		pass


class answerList(APIView):
	def get(self,request,question_id):
		ans=answer.objects.select_related('q_id').filter(q_id=question_id)
		serializer= answerSerializer(ans,many=True)
		return Response(serializer.data)

	def post(self):
		pass
