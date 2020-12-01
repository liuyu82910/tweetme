from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)
    # return HttpResponse("<h3>This is our home page</h3>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    '''
    REST API VIEW
    Return JSON, consumed by JS
    '''
    data = {
    "id": tweet_id,
    # "image": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['content'] = "No such content"
        status = 404
    return JsonResponse(data, status=status)
