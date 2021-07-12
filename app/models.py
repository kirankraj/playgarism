from django.db import models
from common.fields import *


class Login(models.Model):
    username: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30,
                                                                                                 unique=True)
    password: Password(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                                     max_length=8)
    type: Hidden() = models.CharField(max_length=5, default='U')


class User(models.Model):
    id:  Hidden()
    log: Foreign(Login) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    profile: File(path='static/profile', preview={'width': 50, 'height': 50}, css='display:none',
                  start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='avatar.jpg',
                                                                                                max_length=30)
    email: Email(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                               max_length=30)
class Teacher(models.Model):
    id: Hidden()
    log: Foreign(Login,use={'type':'T'}) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    employee_id: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    number: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)

    email: Email(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                               max_length=30)

class Document(models.Model):
    id: Hidden()
    user:Hidden(name="user_id",avoid='avoid')= models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    teacher:Combo(options=[Teacher,'id','name'],name="teacher_id") = models.ForeignKey(Teacher, default=0, on_delete=models.CASCADE)
    document: File(path='static/document', preview={'width': 50, 'height': 50}, css='display:none',
                 start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='avatar.pdf',
                                                                                               max_length=30)
    status: Hidden() = models.CharField(max_length=10,default="Pending")




class Principle(models.Model):
    id: Hidden()
    log: Foreign(Login,use={'type':'P'}) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    employee_id: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)

    email: Email(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                               max_length=30)
class Parent(models.Model):
    id: Hidden()
    log: Foreign(Login,use={'type':'G'}) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    student: Combo(options=[User, 'id', 'name'], name="student_id") = models.ForeignKey(User, default=0,
                                                                                           on_delete=models.CASCADE)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)

    email: Email(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                               max_length=30)


