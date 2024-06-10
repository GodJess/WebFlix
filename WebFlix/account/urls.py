from django.urls import path
from . import views

urlpatterns = [
    path("", views.account, name = "account"),
    path("register/", views.register, name = "register"),
    path("auth/", views.auth, name = "auth"),
    path("delete_ses_user/", views.delsesuser, name = "delsesuser"),
    path("addphoto/", views.addphoto, name = "addphoto"),
    path("myData/", views.myData, name = "myData"),
    path("setting/", views.setting, name = "setting"),
    path("support/", views.support, name = "support"),
    path("analitic/", views.analitic, name = "analitic"),
    path("backUp/", views.backUp, name = "backUp"),
    path("changeLogin/", views.changeLogin, name = "changeLogin"),
    path("changeName/", views.changeName, name = "changeName"),
    path("changeSurname/", views.changeSurname, name = "changeSurname"),
    path("changeMail/", views.changeMail, name = "changeMail"),
    path("changePass/", views.changePass, name = "changePass"),

]
