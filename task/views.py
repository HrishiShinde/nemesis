from django.shortcuts import redirect, render
import requests

from task.models import User

# Create your views here.
def renderLogin(request):
    return render(request, "index.html")

def renderRegister(request):
    return render(request, "register.html")

def renderHome(request):

    db = User.objects.values()

    return render(request, "home.html", {"data" : db})

def doLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pwd = request.POST.get("pass")

        db = User.objects.get(email = email)
        if email == db.email:
            if pwd == db.password:
                request.session['id'] = db.id

                # url = "http://127.0.0.1:8000/api/token/"
                # data = {"username" : email, "password" : pwd}

                # req = requests.post(url, data)

                # print(req.text)

                return redirect("/logshow")
            return render(request, "login.html")
        return render(request, "login.html")

def doRegister(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("pass")
        address = request.POST.get("address")

        db = User.objects.create(name = name, email = email , password= pwd, address = address)
        db.save()

        db = User.objects.get(email = email)
        request.session['id'] = db.id

        return redirect("/home")

def doLogout(request):
    
    del request.session['id']
    return render(request, "index.html", {"success" : "Logout successsful"})

def delete(request, id):

    print(id)

    db = User.objects.get(id = id)
    db.delete()

    # return render(request, "home.html", {"success" : "Data deleted successfully"})
    return redirect("/home")

def update(request):
    if request.method == "POST":
        id = request.POST.get("id")
        print(id)
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")

        db = User.objects.get(id = id)
        db.name = name
        db.email = email
        db.address = address
        db.save()

        return redirect("/home")

