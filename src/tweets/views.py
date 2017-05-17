from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.forms.utils import ErrorList
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Tweet
from django.urls import reverse_lazy
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.

from .forms import TweetModelForm

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	# queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	# success_url = reverse_lazy("tweet:detail")
	login_url = '/admin/'
	# fields = ['user','content']

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin, UpdateView):
	form_class = TweetModelForm
	success_url = '/tweet/'
	template_name = 'tweets/update_view.html'
	queryset = Tweet.objects.all()

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet 
	success_url = reverse_lazy("tweet:list")
	template_name = 'tweets/delete_confirm.html'


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
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query)	|
				Q(user__username__icontains=query)
				) 
		return qs

	def get_context_data(self,*args,**kwargs):
		context = super(TweetListView, self).get_context_data(*args,**kwargs)
		return context

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