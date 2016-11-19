from django.shortcuts import render
from .models import appuser,question,answer,area_of_interest,expertise_area
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import questionSerializer

# Create your views here.

class questionList(APIView):
	def get(self,request):
#		ques= question.objects.filter(asked_by=2)
		ques=[]
		c=[]
		user=appuser.objects.get(id=1)
#		for city in cities:
#			ques.append(question.objects.filter(location=city))
		cities=area_of_interest.objects.all()
		for city in cities:
			c.append(area_of_interest.objects.filter(user_id=user.id))
#		cities = appuser.objects.prefetch_related("area_of_interest").first()
#		cities.area_of_interest_set # Won't need another query
		for city in c:
			ques.append(question.objects.filter(location=city))

		serializer= questionSerializer(ques,many=True)
		return Response(serializer.data)

	def post(self):
		pass
