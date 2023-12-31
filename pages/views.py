from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    context = {
        "key": "lock", "key2": "lock2", "key3": "lock3"
    }
    return HttpResponse("<!DOCTYPE html><html><head><title>My Homepage</title><style>body{font-family:Arial,sans-serif;background-color:#f2f2f2;margin:0;padding:0;}.container{max-width:800px;margin:0 auto;padding:20px;}h1{color:#333;text-align:center;}p{color:#666;line-height:1.5;}.button{display:inline-block;padding:10px 20px;background-color:#007bff;color:#fff;text-decoration:none;border-radius:4px;transition:background-color 0.3s ease;}.button:hover{background-color:#0056b3;}</style></head><body><div class='container'><h1>Welcome to My Homepage</h1><p>This is a sample homepage created using HTML and inline CSS.</p><p>Feel free to explore the content and click the button below to get started.</p><a href='#' class='button'>Get Started</a></div></body></html>")


def homepage_view(request, *args, **kwargs):
    context = {
        "key": "lock", "key2": "lock2", "key3": "lock3"
    }
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    context = {
        "key": "lock", "key2": "lock2", "key3": "lock3"
    }
    return render(request, "about.html", {})

