from django.conf.urls import url
from django.views.generic.base import RedirectView
from tweets.api.views import TweetListAPIView, TweetCreateAPIView, RetweetAPIView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', RedirectView.as_view(url="/")), #/tweet/
    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'), #/api/tweet/ 
]