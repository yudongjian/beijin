from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from app01 import models
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

import math
import json
import os


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def page_error(request):
    return render(request, '404.html', status=500)



# 菜单
def menu(request):
        return render(request, 'menu.html', {'login_statu': request.session.get('user')})


def base(request):
    return render(request, 'a_base.html')

def menu2(request):
    return render(request, 'menu2.html', {'login_statu': request.session.get('user')})


