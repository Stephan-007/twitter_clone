from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import Twitt
from .forms import Tweetform
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.


def index(request):
    # If the method is TWEET
    if request.method == 'POST':
        form = Tweetform(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # If Yes, save
            form.save()
            # Redirect to Home page
            return HttpResponseRedirect('/')
        else:
            # If No, shows error
            return HttpResponseRedirect(form.error.as_json())

    # Get 10 tweets
    tweets = Twitt.objects.all()[:10]
    return render(request, 'tweets.html',
                  {'tweets': tweets})


def delete(request, tweet_id):
    # find the tweet_id
    tweet = Twitt.objects.get(id=tweet_id)
    tweet.delete()
    return HttpResponseRedirect('/')


# def edit(request, tweet_id):
#     tweet = Twitt.objects.get(id=tweet_id)
#     if request.method == 'GET':
#         tweet = Twitt.objects.get(id=tweet_id)
#         return render(request, "edit.html", {"tweet": tweet})
#     if request.method == 'POST':
#         edittweet = Twitt.objects.get(id=tweet_id)
#         form = Tweetform(request.POST, request.FILES, instance=edittweet)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/")
#         else:
#             return HttpResponse("not valid")
#     form = Tweetform
#     return render(request, 'edit.html', {'tweets': tweets, 'form': form})

def edit(request, tweet_id):
    tweet = Twitt.objects.get(id=tweet_id)
    if request.method == 'POST':
        form = Tweetform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = Tweetform
    return render(request, 'edit.html', {'tweet': tweet, 'form': form})

def LikeView(request, tweet_id):
    tweet = Twitt.objects.get(id=tweet_id)
    new_value = tweet.likes + 1
    tweet.likes = new_value
    tweet.save()
    return HttpResponseRedirect('/')