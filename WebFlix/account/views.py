from django.shortcuts import render, redirect
from .forms import AddUser
from .models import UserData, UserStat
from django.conf import settings
# Create your views here.

def account(request):
    length = ""
    navigate = request.session.get(settings.SESSION_NAVIGATE, {})
    user = request.session.get(settings.SESSION_USER, {})

    userstat = []

    if len(user) > 0:
        for el in user:
            ses_user = el["login"]

        userstat = UserStat.objects.filter(login = ses_user).first()
    

    length = len(user)
    navlength = len(navigate)
    data = {
        "user": user,
        "length": length,
        'navigate': navigate,
        'navlength': navlength,
        'userstat' : userstat
    }
    for el in navigate:
        if len(el["nav_name"]) == 0:
            print("аккаунт")
        else:
            print(el["nav_name"])
    return render(request, "account/account.html", data)


def register(request):
    error = ""
    if request.method == "POST":
        forms = AddUser(request.POST)
        repassword = request.POST.get("repassword")
        password = request.POST.get("password")
        logins = request.POST.get("login")
        if len(logins) != 0 and len(password) != 0:
            if forms.is_valid():
                if  password == repassword:
                        objects = UserData.objects.filter(login = logins).first()
                        if objects:
                            error = "Пользователь с таким логином уже зарегистрирован"
                        else:
                            userstat = UserStat(login = logins, science = 0, kriminal = 0, comedy =0, horror = 0, multfilm = 0, dram  = 0 , fantazy = 0, serial = 0, film = 0)
                            userstat.save()
                            forms.save()
                            return redirect("auth")
                else:
                    error = "Пароли должны совпадать"
            else:
                error = "Данные заполены не корректно"
        else:
            error ="Вы не заполнили все строки"        
       
    form = AddUser()

    data = {
        "form": form,
        "error": error
    }
    return render(request, 'account/register.html', data)

def auth(request):
    error = ""
    if request.method == "POST":
         logins = request.POST.get("login")
         password = request.POST.get("password")
         user = request.session.get(settings.SESSION_USER, {})
         request.session.pop(settings.SESSION_USER, None)
         auth = UserData.objects.filter(login = logins, password = password).first()
         
         if auth:
              user = []
              user.append({
                  "id": auth.id, "login": auth.login, "name": auth.name , "surname": auth.surname , "mail": auth.mail , "password": auth.password , "image": auth.image
              })
              request.session[settings.SESSION_USER] = user
              return redirect("account")
         else: 
            error = "Неверный пользователь или пароль"
    
    data = {
        "error": error
    }
    return render(request, 'account/auth.html', data)

def delsesuser(request):
    request.session.pop(settings.SESSION_USER, None)
    return redirect("account")

def addphoto(request):
    user = request.session.get(settings.SESSION_USER, {})
    url = request.POST.get("url")
    logins = ""
    for el in user:
        logins = el["login"]

    auth = UserData.objects.filter(login = logins).first()
    auth.image = url
    auth.save()
    for el in user: # обновляем данные в списке
        if el["login"] == logins:
            el["image"] = auth.image

    request.session[settings.SESSION_USER] = user

    return redirect("account")

def myData(request):
    navigate = request.session.get(settings.SESSION_NAVIGATE, {})
    request.session.pop(settings.SESSION_NAVIGATE, None)
    navigate = []

    navigate.append({
        "nav_name": "myData"
    })

    request.session[settings.SESSION_NAVIGATE] = navigate

    return redirect("account")

def setting(request):
    navigate = request.session.get(settings.SESSION_NAVIGATE, {})
    request.session.pop(settings.SESSION_NAVIGATE, None)
    navigate = []

    navigate.append({
        "nav_name": "setting"
    })

    request.session[settings.SESSION_NAVIGATE] = navigate

    return redirect("account")

def support(request):
    navigate = request.session.get(settings.SESSION_NAVIGATE, {})
    request.session.pop(settings.SESSION_NAVIGATE, None)
    navigate = []

    navigate.append({
        "nav_name": "support"
    })

    request.session[settings.SESSION_NAVIGATE] = navigate

    return redirect("account")

def analitic(request):
    navigate = request.session.get(settings.SESSION_NAVIGATE, {})
    request.session.pop(settings.SESSION_NAVIGATE, None)
    navigate = []

    navigate.append({
        "nav_name": "analitic"
    })

    request.session[settings.SESSION_NAVIGATE] = navigate
    return redirect("account")

def backUp(request):
    request.session.pop(settings.SESSION_NAVIGATE, None)
    return redirect("account")

def changeLogin(request):
    user = request.session.get(settings.SESSION_USER, {})
    login = request.POST.get("login")
    session_data = ""
    if len(login) != 0:
        for el in user:
            session_data = el["login"]
            el["login"] = login
        
        data = UserData.objects.filter( login = session_data).first()
        data.login = login
        data.save()
        request.session[settings.SESSION_USER] = user

    return redirect('account')

def changeName(request):
    user = request.session.get(settings.SESSION_USER, {})
    name = request.POST.get("name")
    session_data = ""
    if len(name) != 0:
        for el in user:
            session_data = el["name"]
            el["name"] = name
        
        data = UserData.objects.filter( name = session_data).first()
        data.name = name
        data.save()
        request.session[settings.SESSION_USER] = user

    return redirect('account')

def changeSurname(request):
    user = request.session.get(settings.SESSION_USER, {})
    surname = request.POST.get("surname")
    session_data = ""
    if len(surname) != 0:
        for el in user:
            session_data = el["surname"]
            el["surname"] = surname
        
        data = UserData.objects.filter( surname = session_data).first()
        data.surname = surname
        data.save()
        request.session[settings.SESSION_USER] = user

    return redirect('account')

def changeMail(request):
    user = request.session.get(settings.SESSION_USER, {})
    mail = request.POST.get("mail")
    session_data = ""
    if len(mail) != 0:
        for el in user:
            session_data = el["mail"]
            el["mail"] = mail
        
        data = UserData.objects.filter( mail = session_data).first()
        data.mail = mail
        data.save()
        request.session[settings.SESSION_USER] = user

    return redirect('account')

def changePass(request):
    user = request.session.get(settings.SESSION_USER, {})
    password = request.POST.get("password")
    session_data = ""
    if len(password) != 0:
        for el in user:
            session_data = el["password"]
            el["password"] = password
        
        data = UserData.objects.filter( password = session_data).first()
        data.password = password
        data.save()
        request.session[settings.SESSION_USER] = user

    return redirect('account')
