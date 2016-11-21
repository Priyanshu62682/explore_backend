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

# Create your views here.

class questionList(APIView):
	def get(self,request):
		ques= question.objects.filter(id=2)
		serializer= questionSerializer(ques,many=True)
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




		
