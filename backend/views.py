from django.shortcuts import render
from .models import appuser,question,answer,area_of_interest,expertise_area,who_asked_what,who_answered_what,q_like,a_like,q_dislike,a_dislike
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from .serializers import questionSerializer,answerSerializer,appuserSerializer,expertSerializer,interestSerializer,w_asked_wSerializer,q_likeSerializer,a_likeSerializer,q_dislikeSerializer,a_dislikeSerializer
from django.db.models import Max


# Create your views here.

class questionList(APIView):
	def get(self,request,id_input):
#		ques= question.objects.filter(asked_by=2)
		cities=area_of_interest.objects.select_related('user_id').filter(user_id=id_input)
		for city in cities:
			q=question.objects.filter(location=city.city).order_by('-id')
			if q:
				serializer= questionSerializer(q,many=True)

		cities=expertise_area.objects.select_related('user_id').filter(user_id=id_input)
		
		for city in cities:
			q=question.objects.filter(location=city.city).order_by('-id')
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
			q=question.objects.filter(location=city.city).order_by('-id')
			if q:
				serializer= questionSerializer(q,many=True)
		
#		ques= question.objects.filter(location="Roorkee")
		
		return Response(serializer.data)

	def post(self):
		pass


class answerList(APIView):
	def get(self,request,question_id):
		ans=answer.objects.select_related('q_id').filter(q_id=question_id).order_by('-upvotes')
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
        get_ques=question.objects.get(id=quw)
        get_ques.status=1
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
        if request.method =='POST':
            user=appuser.objects.get(id=usr_id)
            username=user.name
            serializer=questionSerializer(data=QueryDict('q_detail='+que_detail+'&asked_by='+username+'&status=0&location='+loc+'&upvotes=0&downvotes=0',mutable =True))
            if serializer.is_valid():			
                serializer.save()
            idbc="null"
            print(serializer.data)
            print(serializer.data['id'])
            idbc=serializer.data['id']
            bcidbc=str(idbc)
            print(bcidbc)
            next_serializer=w_asked_wSerializer(data=QueryDict('user_id='+usr_id+'&q_asked='+bcidbc,mutable =True))
            if next_serializer.is_valid():
                next_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class question_vote_upvote(generics.CreateAPIView):
    model=question
    serializer_class=q_likeSerializer
    def get(self,request,usr_id,que_id):
        local=question.objects.get(id=que_id)
        try :
            abc=q_like.objects.filter(q_id=que_id)
        except q_like.DoesNotExist:
            abc=None
        flag=0
        for x in abc:
           if x.user_id==usr_id:
               flag=1
        print(flag)
        if flag==0:
            print("okk")
            local.upvotes=local.upvotes+1
            local.save()
            next_serializer=q_likeSerializer(data=QueryDict('user_id='+usr_id+'&q_id='+que_id,mutable =True))
            if next_serializer.is_valid():
                next_serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
class question_vote_downvote(generics.CreateAPIView):
    model=question
    serializer_class=q_dislikeSerializer
    def get(self,request,usr_id,que_id):
        local=question.objects.get(id=que_id)
        try :
            abc=q_dislike.objects.filter(q_id=que_id)
        except q_dislike.DoesNotExist:
            abc=None
        flag=0
        for x in abc:
           if x.user_id==usr_id:
               flag=1
        print(flag)
        if flag==0:
            print("okk")
            local.downvotes=local.downvotes+1
            local.save()
            next_serializer=q_dislikeSerializer(data=QueryDict('user_id='+usr_id+'&q_id='+que_id,mutable =True))
            if next_serializer.is_valid():
                next_serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

class answer_vote_upvote(generics.CreateAPIView):
    model=answer
    serializer_class=a_likeSerializer
    def get(self,request,usr_id,que_id):
        local=answer.objects.get(id=que_id)
        try :
            abc=a_like.objects.filter(a_id=que_id)
        except a_like.DoesNotExist:
            abc=None
        flag=0
        for x in abc:
           if x.user_id==usr_id:
               flag=1
        print(flag)
        if flag==0:
            print("okk")
            local.upvotes=local.upvotes+1
            local.save()
            next_serializer=a_likeSerializer(data=QueryDict('user_id='+usr_id+'&a_id='+que_id,mutable =True))
            if next_serializer.is_valid():
                next_serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_201_CREATED)

class answer_vote_downvote(generics.CreateAPIView):
    model=answer
    serializer_class=a_dislikeSerializer
    def get(self,request,usr_id,que_id):
        local=answer.objects.get(id=que_id)
        try :
            abc=a_dislike.objects.filter(a_id=que_id)
        except a_dislike.DoesNotExist:
            abc=None
        flag=0
        for x in abc:
           if x.user_id==usr_id:
               flag=1
        print(flag)
        if flag==0:
            print("okk")
            local.downvotes=local.downvotes+1
            local.save()
            next_serializer=q_dislikeSerializer(data=QueryDict('user_id='+usr_id+'&a_id='+que_id,mutable =True))
            if next_serializer.is_valid():
                next_serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_201_CREATED)
      

class interested_area_register(generics.CreateAPIView):
    model=area_of_interest
    serializer_class=expertSerializer
    def post(self, request,user_id,city):
        serializer=interestSerializer(data=QueryDict('user_id='+user_id+'&city='+city,mutable=True))
        if serializer.is_valid():		
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class add_city(generics.CreateAPIView):
    model=area_of_interest
    serializer_class=expertSerializer
    def post(self, request,user_id,expert_in,interested_in):
        flag=0;
        if(interested_in=="null"):
            serializer=interestSerializer(data=QueryDict('user_id='+user_id+'&city='+expert_in,mutable=True))
            flag=1;
            print("in 1");
        elif(expert_in=="null"):
            serializer=expertSerializer(data=QueryDict('user_id='+user_id+'&city='+interested_in,mutable=True))
            flag=1;
            print("in 2");
        else:
            serializer=interestSerializer(data=QueryDict('user_id='+user_id+'&city='+expert_in,mutable=True))
            if serializer.is_valid():       
                serializer.save()
            serializer=expertSerializer(data=QueryDict('user_id='+user_id+'&city='+interested_in,mutable=True))
            if serializer.is_valid():       
                serializer.save()
                print("in 3");
        if(flag==1):
            if serializer.is_valid():       
                serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            
class notify_ques(APIView):
    def get(self,request,user_id):
#        question_rec=question.objects.get(id=ques_id)
#        question_rec.status=2;
        ques=question.objects.raw('SELECT * FROM backend_question INNER JOIN backend_who_asked_what ON backend_question.id=backend_who_asked_what.q_asked WHERE backend_who_asked_what.user_id=9 AND backend_question.status=0 ')
        for q in ques:
            q.status=1
        serializer= questionSerializer(ques,many=True)
        return Response(serializer.data)
