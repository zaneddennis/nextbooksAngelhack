from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FindForm

# Create your views here.


def index(request):

    userFirstName = "Zane"
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    return render(
        request,
        "index.html",
        context={"userFirstName" : userFirstName}
    )


class ResourceDetailView(generic.DetailView):
    model = Resource


def find(request):
    if request.method == "POST":
        form = FindForm(request.POST)

        if form.is_valid():
            request.session["searchParams"] = request.POST.copy()

            return HttpResponseRedirect(reverse("feed"))

    else:
        form = FindForm()

    return render(request, "find.html", {"form": form})


def feed(request):
    resources = Resource.objects.all()
    params = request.session["searchParams"]
    print(request.session["searchParams"])

    #for v in ["level", "subject"]:
    #    print(params[v])
    #    resources = resources.filter(levelTag__exact=params[v])
    resources = resources.filter(levelTag__exact=params["level"])
    resources = resources.filter(subjectTag__exact=params["subject"])

    return render(request, "feed.html", {"resources": resources})


def quiz(request):
    return render(request, "quiz.html")
