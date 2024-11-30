from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

def listtweet(request):
    all_tweets = models.Tweet.objects.all().order_by('-created_at')
    tweet_dict = {"tweets" : all_tweets}
    

    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        user = request.user
        models.Tweet.objects.create(nickname=nickname, message=message, user=user)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')

class SignUpView(FormView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("tweetapp:listtweet")

    def form_valid(self, form):
        User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        return super().form_valid(form)