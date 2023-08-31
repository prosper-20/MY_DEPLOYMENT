from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from . models import News, Subscribers, Category
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def homepage(request):
    if request.method == "POST":
        input_email = request.POST.get("email")
        if not Subscribers.objects.filter(email=input_email).exists():
            Subscribers.objects.create(email=input_email)
            return redirect(reverse("home"))
        else:
            return HttpResponse("Email Address is taken")  
    elif request.method == "GET":
        all_news = get_list_or_404(News)
        context = { "all_news": all_news}
    return render(request, "index.html", context)


def detail(request, slug):
    current_news = get_object_or_404(News, slug=slug)
    context = {"current_news": current_news}
    return render(request, "single-post.html", context)


def category(request):
    all_categories = Category.objects.all()
    context = {"all_categories": all_categories}
    return render(request, "category.html", context)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
