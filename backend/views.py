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
from .serializers import questionSerializer,answerSerializer,appuserSerializer,expertSerializer,interestSerializer

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

#API for all questions of expertise(Answer page)
class question_answer_page(APIView):
	def get(self,request,id_input):
#		ques= question.objects.filter(asked_by=2)
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

class answerPost(generics.CreateAPIView):
    model=answer
    queryset= answer.objects.all()
    serializer_class=answerSerializer
    def post(self, request,ans_no,answer,valid,answeredby,quw):
        ques= question.objects.get(id=1)
        #queryset=answer(ans_id=ans_no,answer_detail=answer,validity=valid,answered_by=answeredby,q_id=ques)
        abc="bishnu"
        bb="9"
        cc="9"
        serializer=answerSerializer(data=QueryDict('ans_id='+ans_no+'&answer_detail='+answer+'&validity='+valid+'&answered_by='+abc+'&q_id=1&upvotes='+bb+'&downvotes='+cc,mutable=True))
        #serializer.save()
        print("here")
        if serializer.is_valid():
            print("okk")			
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class register(generics.CreateAPIView):
    model=appuser
    serializer_class=appuserSerializer
    def post(self, request,name,q_asked,q_answered):
        serializer=appuserSerializer(data=QueryDict('name='+name+'&q_asked='+q_asked+'&q_answered='+q_answered,mutable=True))
        if serializer.is_valid():		
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class expertise_area_register(generics.CreateAPIView):
    model=expertise_area
    serializer_class=expertSerializer
    def post(self, request,user_id,city):
        serializer=expertSerializer(data=QueryDict('user_id='+user_id+'&city='+city,mutable=True))
        if serializer.is_valid():		
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class interested_area_register(generics.CreateAPIView):
    model=area_of_interest
    serializer_class=expertSerializer
    def post(self, request,user_id,city):
        serializer=interestSerializer(data=QueryDict('user_id='+user_id+'&city='+city,mutable=True))
        if serializer.is_valid():		
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

		
