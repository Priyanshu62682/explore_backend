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
    url(r'^questions/',views.questionList.as_view()),
    url(r'^answer/(?P<ans_no>[0-9]{1})/(?P<answer>[a-z]{5})/(?P<valid>[0-9]{1})/(?P<answeredby>[a-z]{5})/(?P<quw>[0-9]{1})/$', views.answerList.as_view()),
    #url(r'^answer/', views.answerList.as_view()),
    #for questions--> /feed/<user-id>/    (questions related to areas of that user expert+intersted)
    url(r'^feed/(?P<id_input>[0-9]+)/$',views.questionList.as_view()),
    #for answers--> /answers/<question-id>/
    url(r'^answers/(?P<question_id>[0-9]+)/$',views.answerList.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)
