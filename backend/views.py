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
    def post(self, request,answer,quw,usr_id):
        ques= appuser.objects.get(id=usr_id)
        abc=ques.name
        serializer=answerSerializer(data=QueryDict('q_id='+quw+'&answer_detail='+answer+'&validity=0&answered_by='+abc+'&upvotes=0&downvotes=0',mutable=True))
        if serializer.is_valid():		
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class register(generics.CreateAPIView):
    model=appuser
    serializer_class=appuserSerializer
    def post(self, request,name,city):
        serializer=appuserSerializer(data=QueryDict('name='+name,mutable=True))
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

class questionPost(generics.CreateAPIView):
    model=question
    serializer_class=questionSerializer
    def post(self,request,usr_id,que_detail,loc):
        user=appuser.objects.get(id=usr_id)
        username=user.name
        serializer=questionSerializer(data=QueryDict('q_detail='+que_detail+'&asked_by='+username+'&status=0&location='+loc+'&upvotes=0&downvotes=0',mutable =True))
        if serializer.is_valid():
            print("okk")			
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class question_vote_upvote(generics.CreateAPIView):
    model=question
    serializer_class=questionSerializer
    def get(self,request,usr_id,que_id):
        local=question.objects.get(id=que_id)
        local.upvotes=local.upvotes+1
        local.save()
        return Response(status=status.HTTP_201_CREATED)

class question_vote_downvote(generics.CreateAPIView):
    model=question
    serializer_class=questionSerializer
    def get(self,request,usr_id,que_id):
        local=question.objects.get(id=que_id)
        local.downvotes=local.downvotes+1
        local.save()
        return Response(status=status.HTTP_201_CREATED)

class answer_vote_upvote(generics.CreateAPIView):
    model=answer
    serializer_class=answerSerializer
    def get(self,request,usr_id,que_id):
        local=answer.objects.get(id=que_id)
        local.upvotes=local.upvotes+1
        local.save()
        return Response(status=status.HTTP_201_CREATED)

class answer_vote_downvote(generics.CreateAPIView):
    model=answer
    serializer_class=answerSerializer
    def get(self,request,usr_id,que_id):
        local=answer.objects.get(id=que_id)
        local.downvotes=local.downvotes+1
        local.save()
        return Response(status=status.HTTP_201_CREATED)
      

class interested_area_register(generics.CreateAPIView):
    model=area_of_interest
    serializer_class=expertSerializer
    def post(self, request,user_id,city):
        serializer=interestSerializer(data=QueryDict('user_id='+user_id+'&city='+city,mutable=True))
        if serializer.is_valid():		
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

		
