from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    people = [
        {'name': 'Messi', 'age': 38},
        {'name': 'Stephan', 'age': 30},
        {'name': 'Taehyung', 'age': 27},
        {'name': 'Durook', 'age': 17},
        {'name': 'Kakashi', 'age': 28},
    ]

    vegetables = ['Pumpkin', 'Tomato', 'Potato']
    return render(request, "home/index.html", context={'page': 'Home','peoples': people, 'vegetables': vegetables})


def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html", context)


def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html", context)


def success_page(request):
    print('success page')
    return HttpResponse("<h1>Hey this is success page.</h1>")
