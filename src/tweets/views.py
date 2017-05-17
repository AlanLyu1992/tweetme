from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.shortcuts import render, get_object_or_404
from django.forms.utils import ErrorList
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.

from .forms import TweetModelForm

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	# queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	success_url = '/tweet/create/'
	login_url = '/admin/'
	# fields = ['user','content']

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin, UpdateView):
	form_class = TweetModelForm
	success_url = '/tweet/'
	template_name = 'tweets/update_view.html'
	queryset = Tweet.objects.all()



class TweetDetailView(DetailView):
	# template_name = "tweets/detail_view.html"
	queryset = Tweet.objects.all()

	# def get_object(self):
	# 	print(self.kwargs)
	# 	pk = self.kwargs.get("pk")
	# 	return Tweet.objects.get(id=pk)

class TweetListView(ListView):
	# template_name = "tweets/list_view.html"
	queryset = Tweet.objects.all()

# def tweet_detail_view(request, id=1):
# 	obj = Tweet.objects.get(id=id) 
# 	print (obj)
# 	context = {
# 		"object": obj
# 	}
# 	return render(request,"tweets/detail_view.html",context)

# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	print (queryset)
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request,"tweets/list_view.html",context)