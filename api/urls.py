from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'images/$', views.ImageList.as_view()),
    url(r'images/(?P<pk>[0-9a-zA-Z-]*)$', views.ImageDetail.as_view(), name='image-detail'),

    url(r'tags/$', views.TagList.as_view()),
    url(r'tags/(?P<pk>[0-9a-zA-Z-]*)$', views.TagDetail.as_view(), name='tag-detail'),
]

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)

