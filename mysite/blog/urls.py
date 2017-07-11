from django.conf.urls import url
from .import views

# URL 配置文件的命名空间
app_name = 'blog'
urlpatterns = [
    # ex:/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex:/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex:/5/result
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex:/5/votes
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]