from django.conf.urls import url

from . import views

app_name = 'comment'
urlpatterns = [
    url(r'^comment_a/$', views.comment_view, name='comment_a'),

    url(r'^make_comment/(?P<comment_id>\d+)/$', views.add_comment_c,
        name='comment_c'),

]