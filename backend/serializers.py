from rest_framework import serializers
from .models import appuser,area_of_interest,expertise_area,question,answer


class questionSerializer(serializers.ModelSerializer):

	class Meta:
		model= question
		fields= '__all__'

class answerSerializer(serializers.ModelSerializer):

	class Meta:
		model= answer
		fields= '__all__'