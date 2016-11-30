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
#    url(r'^answerpost/(?P<ans_no>[0-9]+)/(?P<answer>[a-z]{5})/(?P<valid>[0-9]{1})/(?P<answeredby>[a-z]{5})/(?P<quw>[0-9]{1})/$', views.answerPost.as_view()),
    #url(r'^answer/', views.answerList.as_view()),
    #for questions--> /feed/<user-id>/    (questions related to areas of that user expert+intersted)
    url(r'^feed/(?P<id_input>[0-9]+)/$',views.questionList.as_view()),
    #for answers--> /answers/<question-id>/
    url(r'^answerslist/(?P<question_id>[0-9]+)/$',views.answerList.as_view()),
    #for answer feed page(experts answers in that)
    url(r'^answer_feed/(?P<id_input>[0-9]+)/$',views.question_answer_page.as_view()),
    #register new user
    url(r'^register/(?P<name>[a-zA-Z0-9|\w|\W]+)/(?P<city>[a-zA-Z0-9|\w|\W]+)/$',views.register.as_view()),
    #update area of expertise
    url(r'^expertise-area-register/(?P<user_id>[0-9]+)/(?P<city>[a-zA-Z0-9|\w|\W]+)/$',views.expertise_area_register.as_view()),
    #update area of interest
    url(r'^interested-area-register/(?P<user_id>[0-9]+)/(?P<city>[a-zA-Z0-9|\w|\W]+)/$',views.interested_area_register.as_view()),
    url(r'^answerpost/(?P<answer>[a-zA-Z0-9|\w|\W]+)/(?P<quw>[0-9]+)/(?P<usr_id>[0-9]+)/$', views.answerPost.as_view()),
#    url(r'^feed/(?P<id_input>[0-9]+)/$',views.questionList.as_view()),
#    url(r'^answerlist/(?P<question_id>[0-9]+)/$',views.answerList.as_view()),
    url(r'^questionpost/(?P<usr_id>[0-9]+)/(?P<que_detail>[a-zA-Z0-9|\w|\W]+)/(?P<loc>[a-zA-Z0-9|\w|\W]+)/$',views.questionPost.as_view()),
    url(r'^questionlike/(?P<usr_id>[0-9]+)/(?P<que_id>[0-9]+)/$',views.question_vote_upvote.as_view()),
    url(r'^questiondislike/(?P<usr_id>[0-9]+)/(?P<que_id>[0-9]+)/$',views.question_vote_downvote.as_view()),
    url(r'^answerlike/(?P<usr_id>[0-9]+)/(?P<que_id>[0-9]+)/$',views.answer_vote_upvote.as_view()),
    url(r'^answerdislike/(?P<usr_id>[0-9]+)/(?P<que_id>[0-9]+)/$',views.answer_vote_downvote.as_view()),
    #add city
    url(r'^addcity/(?P<user_id>[0-9]+)/(?P<expert_in>[a-zA-Z0-9|\w|\W]+)/(?P<interested_in>[a-zA-Z0-9|\w|\W]+)/$',views.add_city.as_view()),
    #notify url
    url(r'^notify_ques/(?P<user_id>[0-9]+)/$',views.notify_ques.as_view())

]

#urlpatterns = format_suffix_patterns(urlpatterns)
