from django.shortcuts import render, redirect, HttpResponse
from .models import Content, Season1, Comment
from account.models import UserStat
from django.views.generic import DetailView
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, "main/index.html")

def main(request):
    request.session.pop(settings.SESSION_NAVIGATE, None)
    content = Content.objects.all()
    
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def fantazy(request):
    content = Content.objects.filter(genre = "fantazy")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def science(request):
    content = Content.objects.filter(genre = "science")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def kriminal(request):
    content = Content.objects.filter(genre = "kriminal")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def comedy(request):
    content = Content.objects.filter(genre = "comedy")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)


def horror(request):
    content = Content.objects.filter(genre = "horror")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def multfilm(request):
    content = Content.objects.filter(genre = "multfilm")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def dram(request):
    content = Content.objects.filter(genre = "dram")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def serial(request):
    content = Content.objects.filter(view = "serial")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def film(request):
    content = Content.objects.filter(view = "film")
    data = {
        "content": content,

    }
    return render(request, "main/main.html", data)

def search(request):
    words = request.POST.get("search")
    content = Content.objects.filter(name__icontains = words)
    data = {
        "content": content,
        "words": words,
    }
    return render(request, "main/main.html", data)

def details(request):
    data = request.session.get(settings.SESSION_VIDEO, {})
    list_video = request.session.get(settings.SESSION_LIST_VIDEO, {})
    play = request.session.get(settings.SESSION_PLAY_VIDEO, {})
    comment = request.session.get(settings.SESSION_COMMENT, {})
    user = request.session.get(settings.SESSION_USER, {})


    for key , value in data.items():
        comment = Comment.objects.filter( serialName = value["name"])

    isUser = len(user)
    length = len(play)

    context ={
        "data": data,
        "list_video": list_video,
        "play": play,
        "length": length,
        "comment" : comment,
        "isUser" : isUser
    }

    return render(request, "main/details_content.html", context)

def details_content(request):

    if request.method == 'POST':
        data = request.session.get(settings.SESSION_VIDEO, {})
        list_video = request.session.get(settings.SESSION_LIST_VIDEO, {})
        user = request.session.get(settings.SESSION_USER, {})
        request.session.pop(settings.SESSION_PLAY_VIDEO, None)
        # comment = request.session.get(settings.SESSION_COMMENT, {})

        ses_user = ""


        id = request.POST.get("id")
        content = Content.objects.filter(id=id).first()
        
        if len(user) > 0:
            for el in user:
                ses_user = el["login"]

            userstat = UserStat.objects.filter(login = ses_user).first()

            if content.view == "serial":
                userstat.serial = int(userstat.serial)  + 1
            else:
                userstat.film = int(userstat.film)  + 1

            if content.genre == "comedy":
                userstat.comedy = int(userstat.comedy)  + 1
                
            elif content.genre == "kriminal":
                userstat.kriminal = int(userstat.kriminal)  + 1
            
            elif content.genre == "fantazy":
                userstat.fantazy = int(userstat.fantazy)  + 1

            elif content.genre == "science":
                userstat.science = int(userstat.science)  + 1
            
            elif content.genre == "horror":
                userstat.horror = int(userstat.horror)  + 1    
            
            elif content.genre == "multfilm":
                userstat.multfilm = int(userstat.multfilm)  + 1

            elif content.genre == "dram":
                userstat.dram = int(userstat.dram)  + 1
            userstat.save()


        
        request.session.pop(settings.SESSION_LIST_VIDEO, None)
        # request.session.pop(settings.SESSION_COMMENT, None)

        for key in list(data.keys()):
            del data[key]
        
        mass = []
        
        for i in range(int(content.countseason)):
            mass.append(i+1)
        
        data[id] = {
            "image": content.image, "name": content.name,
            "description": content.description, "release_date": content.release_date,
            "review": content.review, "countseason": mass
        }
        
        request.session[settings.SESSION_VIDEO] = data

        # comment = []
        # for key, value in data.items():
        #     comm = Comment.objects.filter(serialName = value["name"])
        #     if comm:
        #         for el in comm:
        #             comment.append({
        #                 "loginCom": el.loginCom , "serialName": el.serialName, "text" : el.text, "like": el.like, "dislike": el.dislike
        #             })
        # request.session[settings.SESSION_COMMENT] = comment

        
        list_video = []
        for key, value in data.items():
            video = Season1.objects.filter(serialname=value["name"], numberseason=1)
            if video:
                for el in video:
                    list_video.append({
                        "name": el.serialname, "link": el.linkseries, "number": el.numberseason,
                        "prevewimage": el.prevewimage, "numberseries": el.numberseries
                    })

        request.session[settings.SESSION_LIST_VIDEO] = list_video
                     

        return redirect("details")
    else:
        return HttpResponse('Invalid request')
    
def play_video(request):
    play = request.session.get(settings.SESSION_PLAY_VIDEO, {})
    list_video = request.session.get(settings.SESSION_LIST_VIDEO, {})
    request.session.pop(settings.SESSION_PLAY_VIDEO, None)

    series = request.POST.get("series")
    season = request.POST.get("season")
    serialname = request.POST.get("serialname")
    play = []
    season = Season1.objects.filter(serialname=serialname, numberseason=season, numberseries=series).first()
    if season:
        play.append({
                "video": season.linkseries,
            })
    request.session[settings.SESSION_PLAY_VIDEO] = play
    return redirect("details")

def add_video(request):
    list_video = request.session.get(settings.SESSION_LIST_VIDEO, {})
    request.session.pop(settings.SESSION_LIST_VIDEO, None)

    serialname = request.POST.get("serialname")
    season = request.POST.get("season")
    video = Season1.objects.filter(serialname = serialname, numberseason = season)

    list_video = []
    if video:
        for el in video:
            list_video.append({
                "name": el.serialname, "link": el.linkseries, "number": el.numberseason,
                "prevewimage": el.prevewimage, "numberseries": el.numberseries
            })

    request.session[settings.SESSION_LIST_VIDEO] = list_video
                     

    return redirect("details")


def addcomment(request):
    user = request.session.get(settings.SESSION_USER, {})
    login = ""


    serialName = request.POST.get("serialName")
    text = request.POST.get("text")

    like = 0
    dislike = 0
    if len(text) > 0:    
        if len(user) != 0:
            for el in user:
                login = el["login"]

            comment = Comment( loginCom = login  ,serialName = serialName ,text = text ,like = like ,dislike = dislike)
            comment.save()
        
    

    return redirect("details")