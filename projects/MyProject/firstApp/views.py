from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.http import HttpResponse


def hi(request):
    return HttpResponse("<h2>Welcome to django</h2>")


def hello(request, name):
    return HttpResponse("<h3>Welcome to django Session</h3>" + name)


def rollno(reg, id):
    txt = '<h2>your rollno is {} <h2>'.format(id)
    return HttpResponse(txt)


def message(request):
    return render(request, 'firstApp/message.html', {})


def register(request):
    if request.method == 'POST':
        name = request.POST['username']
        mobileno = request.POST['mobilenum']
        email = request.POST['email']
        # print(name)
        return HttpResponse("Done successfully")
    return render(request, 'firstApp/signup.html', {})


def details(request):
    data = {'name': "Ranga", 'RollNum': "4a2"}
    return render(request, 'firstApp/details.html', {'data': data})


def login(request):
    static_name = 'user1'
    static_password = 'pswd'
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        if static_name == name and static_password == static_password:
            return HttpResponse("logged in successfully")
        else:
            return HttpResponse("invalid credentials")
    return render(request, 'firstApp/login.html', {})


def score(request):
    if request.method == 'POST':
        team1 = request.POST.get('team1')
        team2 = request.POST.get('team2')
        if team1 is not None:
            val1 = int(request.POST.get('t1val')) + 1
            val2 = int(request.POST.get('t2val'))
            scores = {'t1val': val1, 't2val': val2}
            return render(request, 'firstApp/scoreboard.html', scores)
        elif team2 is not None:
            val2 = int(request.POST.get('t2val')) + 1
            val1 = int(request.POST.get('t1val'))
            scores = {'t1val': val1, 't2val': val2}
            return render(request, 'firstApp/scoreboard.html', scores)
    else:
        return render(request, 'firstApp/scoreboard.html')


def home(request):
    return render(request, 'firstApp/home.html')


def restaurant(request):
    if request.method == 'POST':
        biryani = request.POST['biryani']
        butternaans = request.POST['butternaans']

        biryani_cost = 220 * int(biryani)
        butternaans_cost = 10 * int(butternaans)
        total = biryani_cost + butternaans_cost
        menu = {'biryani': biryani, 'butternaans': butternaans, 'biryani_cost': biryani_cost,
                'butternaans_cost': butternaans_cost, 'total': total}
        return render(request, 'firstApp/restaurantapplication.html', {'menu': menu})
    return render(request, 'firstApp/restaurantapp.html')
