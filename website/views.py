from django.shortcuts import render,redirect
from website import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def home(request):
    return render(request,"home.html")

def index(request):
    return render(request,"index.html")

def home_test(request):
    return render(request,'home_test.html')

def source(request):

    if request.method =="GET":
        current_page = request.GET.get('p', 1)
        current_page = int(current_page)
        total_count = models.Source.objects.all().count()
        from static.common.page import PagerHelper
        obj1 = PagerHelper(total_count,current_page,'/source')
        pager = obj1.pager_str()
        obj = models.Source.objects.all()[obj1.db_start:obj1.db_end]
        key_word = []
        return render(request,"source.html",{"obj":obj,"key_word":key_word,"str_pager":pager})
    elif request.method =="POST":
        key_word = request.POST.get("keyword")
        # print(req)
        # obj = models.Source.objects.all()
        current_page = request.GET.get('p', 1)
        current_page = int(current_page)
        total_count = models.Source.objects.all().count()
        from static.common.page import PagerHelper
        obj1 = PagerHelper(total_count,current_page,'/source')
        pager = obj1.pager_str()
        obj = models.Source.objects.all()[obj1.db_start:obj1.db_end]

        return render(request,"source.html",{"obj":obj,"key_word":key_word,"str_pager":pager})


    # if request.method =="GET":
    #
    #     obj = models.Source.objects.all()
    #     key_word = []
    #
    #     return render(request,"source.html",{"obj":obj,"key_word":key_word})
    # elif request.method =="POST":
    #     key_word = request.POST.get("keyword")
    #     # print(req)
    #     obj = models.Source.objects.all()
    #
    #     return render(request,"source.html",{"obj":obj,"key_word":key_word})


def people(request,nid):
    obj = models.People.objects.all()[0:6]

    return render(request,"people.html",{"obj":obj,"nid":int(nid)})

def about(request):
    return render(request,"about.html")

def art(request):
    return render(request,"art.html")

def community(request):
    return render(request,"community.html")

def login(request):
    return render(request,"login.html")

def login_people(request,nid):
    if request.method == "GET":
        obj=models.People.objects.all()
        return render(request,"login/login_people.html",{"obj":obj})
    elif request.method == "POST":
        name = request.POST.get('name',None)
        picture = request.POST.get('picture',None)
        grade = request.POST.get('grade',None)
        position = request.POST.get('position',None)
        blog = request.POST.get('blog',None)
        introduce = request.POST.get('introduce',None)

        if name and picture and grade and position and blog and introduce:
        #
            models.People.objects.create(name=name,picture=picture,grade=grade,position=position,blog=blog,introduce=introduce)
        # else:
        #     # return HttpResopnse("²»ÄÜÎª¿Õ")
        #     from tkinter import messagebox
        #     messagebox.showinfo("Warning","Information can't be empty")

        # return redirect("/login_people-1/")

        id = int(nid)
        # print(id)
        obj = models.People.objects.filter(id=id).delete()
        # id = request.POST.get("")
        # print(id)
        # obj = models.People.objects.all()
        # print(obj)
        # return render(request,"login/login-people.html",{"obj":obj})
        # d = "/login_people" + nid
        return redirect("/login_people-" + nid + "/")
def login_source(request,nid):
    if request.method == "GET":
        obj = models.Source.objects.all()
        return render(request,"login/login_source.html",{"obj":obj})
    elif request.method == "POST":
        name = request.POST.get('name', None)
        link = request.POST.get('link', None)
        code = request.POST.get('code', None)
        # position = request.POST.get('position', None)
        # blog = request.POST.get('blog', None)
        # introduce = request.POST.get('introduce', None)
        if name and link and code:
            models.Source.objects.create(name=name,link=link,code=code)
        id = int(nid)
        # print(id)
        obj = models.Source.objects.filter(id=id).delete()
        return redirect("/login_source-" + nid + "/")



