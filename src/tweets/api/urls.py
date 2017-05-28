from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (
	TweetListAPIView, 
	TweetCreateAPIView, 
	RetweetAPIView,
	LikeToggleAPIView,
	TweetDetailAPIView
	)

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', RedirectView.as_view(url="/")), #/tweet/
    url(r'^$', TweetListAPIView.as_view(), name='list'), #/api/tweet/ 
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), #/api/tweet/create
    url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'),   #/tweet/1/like
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),	# /tweet/1/retweet
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),   #/tweet/1/like
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),	# /tweet/1/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),	# /tweet/1/update
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),	# /tweet/1/delete

]