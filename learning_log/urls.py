from django.conf.urls import include, url
from django.contrib import admin
import mkeditor

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'', include('learning_logs.urls', namespace='learning_logs')), 
    url(r'^comment/', include('comment.urls', namespace='comments')), 
    url(r'mdeditor/', include('mdeditor.urls')),
]
