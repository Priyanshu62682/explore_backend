"""explore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^answerpost/(?P<answer>[a-z]+)/(?P<quw>[0-9]+)/(?P<usr_id>[0-9]+)/$', views.answerPost.as_view()),
    url(r'^feed/(?P<id_input>[0-9]+)/$',views.questionList.as_view()),
    url(r'^answerlist/(?P<question_id>[0-9]+)/$',views.answerList.as_view()),
    url(r'^questionpost/(?P<usr_id>[0-9]+)/(?P<que_detail>[a-z]+)/(?P<loc>[a-z]+)/$',views.questionPost.as_view()),
    url(r'^questionlike/(?P<usr_id>[0-9]+)/(?P<que_id>[0-9]+)/$',views.question_vote_upvote.as_view()),
    url(r'^questiondislike/(?P<usr_id>[0-9]+)/(?P<que_id>[0-9]+)/$',views.question_vote_downvote.as_view()),
    url(r'^answerlike/(?P<usr_id>[0-9]+)/(?P<que_id>[0-9]+)/$',views.answer_vote_upvote.as_view()),
    url(r'^answerdislike/(?P<usr_id>[0-9]+)/(?P<que_id>[0-9]+)/$',views.answer_vote_downvote.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)
