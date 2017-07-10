from django.conf.urls import url
from .import views
urlpatterns = [
    # ex:/
    url(r'^$', views.index, name='index'),
    # ex:/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex:/5/result
    url(r'^(?P<question_id>[0-9]+)/results/$', views.result, name='results'),
    # ex:/5/votes
    url(r'^(?P<question_id>[0-9]+)/$/vote/$', views.vote, name='vote'),
]