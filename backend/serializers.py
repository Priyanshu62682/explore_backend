from rest_framework import serializers
from .models import appuser,area_of_interest,expertise_area,question,answer,who_asked_what,who_answered_what


class questionSerializer(serializers.ModelSerializer):

	class Meta:
		model= question
		fields= '__all__'

class answerSerializer(serializers.ModelSerializer):

	class Meta:
		model= answer
		fields= '__all__'

class appuserSerializer(serializers.ModelSerializer):

	class Meta:
		model= appuser
		fields= '__all__'

class expertSerializer(serializers.ModelSerializer):

	class Meta:
		model= expertise_area
		fields= '__all__'

class interestSerializer(serializers.ModelSerializer):

	class Meta:
		model= area_of_interest
		fields= '__all__'

class w_asked_wSerializer(serializers.ModelSerializer):
	class Meta:
		model=who_asked_what
		fields='__all__'