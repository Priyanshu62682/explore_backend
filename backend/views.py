from django.shortcuts import render
from .models import appuser,question,answer,area_of_interest,expertise_area
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import questionSerializer, answerSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import answer
from django.http import QueryDict
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

#view for the answers
class answerList(generics.CreateAPIView):
    model=answer
    queryset= answer.objects.all()
    serializer_class=answerSerializer
    def post(self, request,ans_no,answer,valid,answeredby,quw):
        ques= question.objects.get(id=2)
        #queryset=answer(ans_id=ans_no,answer_detail=answer,validity=valid,answered_by=answeredby,q_id=ques)
        serializer=answerSerializer(data=QueryDict('ans_id='+ans_no+'&answer_detail='+answer+'&validity='+valid+'&answered_by=bishnu&q_id=2',mutable=True))
        #serializer.save()
        if serializer.is_valid():			
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




		
