from __future__ import unicode_literals

from django.db import models

# Create your models here.
class appuser(models.Model):
	name=models.CharField(max_length=50)
	q_asked=models.IntegerField()
	q_answered=models.IntegerField()
	def __str__(self):
		return self.name

class expertise_area(models.Model):
	user_id=models.ForeignKey(appuser, on_delete=models.CASCADE)
	city=models.CharField(max_length=20)
	def __str__(self):
		return self.city

class area_of_interest(models.Model):
	user_id=models.ForeignKey(appuser, on_delete=models.CASCADE)
	city=models.CharField(max_length=20)
	def __str__(self):
		return self.city

class question(models.Model):
	q_detail=models.CharField(max_length=5000)
#	asked_by=models.ForeignKey(appuser,on_delete=models.CASCADE)
	#0 is not answered
	status=models.IntegerField()	
	location=models.CharField(max_length=20)
	asked_on=models.DateField(auto_now=True, auto_now_add=False)
	upvotes=models.IntegerField()
	downvotes=models.IntegerField()
	def __str__(self):
		t=str(self.id)
		return t

class answer(models.Model):
	q_id=models.ForeignKey(question, on_delete=models.CASCADE)
	ans_id=models.IntegerField()
	answer_detail=models.CharField(max_length=5000)
	validity=models.IntegerField()
#	answered_by=models.CharField(max_length=100)
	asked_on=models.DateField(auto_now=True, auto_now_add=False)
	upvotes=models.IntegerField()
	downvotes=models.IntegerField()
	def __str__(self):
		t=str(self.id)
		return t