from django.shortcuts import render,HttpResponse

# Create your views here.
from common import __views
from app.models import *
from plagiarism.settings import STASTIC_FOLDER
import os


def index(request):
    login = Login.objects.filter(username='admin', password='admin').first()
    if login is None:
        login = Login(username='admin', password='admin', type='A').save();
        login = Login.objects.filter(username='admin', password='admin').first()
        User(log=login, name='Admin', email='admin').save();
    return __views.__form(request, 'User', 'index')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login = Login.objects.filter(username=username, password=password).first()

        delete_session(request)
        if login is not None:
            # request.session['profile'] = user.profile;
            request.session['log_id'] = login.id;

            request.session['role'] = login.type;
    datas = User.objects.all()
    page = 'index.html'
    if login is None:
        __views.addmessage(request, __views.TAG_ERROR, 'Username or password incorrect')
        return render(request, page, {'model': datas})
    elif login.type is 'A':
        page = 'admin/index.html'
    elif login.type is 'U':
        user = User.objects.filter(log=login).first()
        request.session['name'] = user.name;
        request.session['user_id'] = user.id;
        page = 'user/index.html'
    elif login.type is 'T':
        user = Teacher.objects.filter(log=login).first()
        request.session['name'] = user.name;
        request.session['user_id'] = user.id;
        page = 'Teacher/home.html'

    elif login.type is 'P':
        user = Principle.objects.filter(log=login).first()
        request.session['name'] = user.name;
        request.session['user_id'] = user.id;
        page = 'principal/home.html'
    elif login.type is 'G':
        user = Parent.objects.filter(log=login).first()
        request.session['name'] = user.name;
        request.session['user_id'] = user.id;
        page = 'parent/home.html'
    return render(request, page, {'model': datas})
    return render(request, page, {'model': datas})


def delete_session(request):
    try:
        del request.session['name']
        del request.session['profile']
        del request.session['log_id']
        del request.session['user_id']
        del request.session['role']
    except  KeyError:
        pass


def logout(request):
    delete_session(request)
    return render(request, 'index.html')


def detail(request):
    objs = User.objects.all()
    return render(request, 'principal/detail.html', {'objs': objs})


def teacherdetail(request):
    objs = Teacher.objects.all()
    return render(request, 'principal/teacherdetail.html', {'objs': objs})


def contact(request):
    return render(request, 'parent/contact.html')


# def view(request):
#     objs = Document.objects.all()
#     return render(request, 'Teacher/view.html', {'objs': objs})

from app.detecter.plagiarism import checker



def check(request):
    return render(request, 'Teacher/checker.html', {'data': checker()})


def viewmore(request):
    filename = request.GET.get('filename')
    isdup = request.GET.get('isdup')
    data = Document.objects.filter(document=filename).first()
    return render(request, 'Teacher/viewmore.html', {'data': data, 'isdup': isdup})


def approve(request):
    id = request.GET.get('id')
    status = request.GET.get('status')
    data = Document.objects.filter(id=id).first()
    data.status = status
    data.save()
    return render(request, 'Teacher/checker.html', {'data': checker()})


def upload(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(file):
            ext = file.name.split('.')[1]
            filename = "{}.{}".format(round(time.time() * 1000), ext)
            __views.handle_uploaded_file(file,'bindings',filename)

        process(x)
    return HttpResponse("File(s) uploaded!")
