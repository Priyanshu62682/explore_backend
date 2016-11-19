from rest_framework import serializers
from .models import appuser,area_of_interest,expertise_area,question,answer


class questionSerializer(serializers.ModelSerializer):

	class Meta:
		model= question
		fields= '__all__'