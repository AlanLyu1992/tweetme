from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

User = get_user_model()
class UserDetailView(DetailView):
	template_name = 'accounts/user_detail.html'
	queryset = User.objects.all()

	def get_object(self):
		return get_object_or_404(User, username__iexact=self.kwargs.get("username"))


class UserFollow(View):
	def get(self, username):
		return redirect
