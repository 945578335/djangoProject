import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from phc import models

def indexshow(request):
    return render(request,'index.html')

def basic_hash_index(request):
    phc_basic = models.PhcBasic.objects.all()
    return render(request, 'basic_index.html',{'phc_basic':phc_basic})

def basicshow1(request):
    phc_basic1 = models.PhcBasic.objects.get(id=1)
    basicchain1 = models.Basicchain1.objects.all()
    return render(request,'basic_hash1.html',{'basicchain1':basicchain1,'phc_basic1':phc_basic1})

def basicshow2(request):
    phc_basic2 = models.PhcBasic.objects.get(id=2)
    basicchain2 = models.Basicchain2.objects.all()
    return render(request,'basic_hash2.html',{'basicchain2':basicchain2,'phc_basic2':phc_basic2})


def share_hash_index(request):
    phc_share = models.PhcShare.objects.all()
    return render(request, 'share_index.html',{'phc_share':phc_share})

def shareshow1(request):
    phc_share1 = models.PhcShare.objects.get(id=1)
    sharechain1 = models.Sharechain1.objects.all()
    return render(request,'share_hash1.html',{'sharechain1':sharechain1,'phc_share1':phc_share1})

def shareshow2(request):
    phc_share2 = models.PhcShare.objects.get(id=2)
    sharechain2 = models.Sharechain2.objects.all()
    return render(request,'share_hash2.html',{'sharechain2':sharechain2,'phc_share2':phc_share2})


def salt_hash_index(request):
    phc_salt = models.PhcSalt.objects.all()
    return render(request, 'salt_index.html',{'phc_salt':phc_salt})

def saltshow1(request):
    phc_salt1 = models.PhcSalt.objects.get(id=1)
    saltchain1 = models.Saltchain1.objects.all()
    return render(request,'salt_hash1.html',{'saltchain1':saltchain1,'phc_salt1':phc_salt1})

def saltshow2(request):
    phc_salt2 = models.PhcSalt.objects.get(id=2)
    saltchain2 = models.Saltchain2.objects.all()
    return render(request,'salt_hash2.html',{'saltchain2':saltchain2,'phc_salt2':phc_salt2})


def mutual_hash_index(request):
    phc_mutual = models.PhcMutual.objects.all()
    return render(request, 'mutual_index.html',{'phc_mutual':phc_mutual})

def mutualshow(request):
    phc_mutual = models.PhcMutual.objects.get(id=1)
    mutualchain = models.Mutualchain.objects.all()
    return render(request,'mutual_hash.html',{'mutualchain':mutualchain,'phc_mutual':phc_mutual})


def first_sign_index(request):
    phc_first = models.PhcFirstsig.objects.all()
    return render(request,'first_index.html',{'phc_first':phc_first})

def firstshow1(request):
    phc_first1 = models.PhcFirstsig.objects.get(id=1)
    firstsign1 = models.Firstsig1.objects.all()
    return render(request,'first_sign1.html',{'firstsign1':firstsign1,'phc_first1':phc_first1})

def firstshow2(request):
    phc_first2 = models.PhcFirstsig.objects.get(id=2)
    firstsign2 = models.Firstsig2.objects.all()
    return render(request,'first_sign2.html',{'firstsign2':firstsign2,'phc_first2':phc_first2})


def final_sign_index(request):
    phc_final = models.PhcFinalsig.objects.all()
    return render(request,'final_index.html',{'phc_final':phc_final})

def finalshow1(request):
    phc_final1 = models.PhcFinalsig.objects.get(id=1)
    finalsign1 = models.Finalsig1.objects.all()
    return render(request,'final_sign1.html',{'finalsign1':finalsign1,'phc_final1':phc_final1})

def finalshow2(request):
    phc_final2 = models.PhcFinalsig.objects.get(id=2)
    finalsign2 = models.Finalsig2.objects.all()
    return render(request,'final_sign2.html',{'finalsign2':finalsign2,'phc_final2':phc_final2})


def interval_sign_index(request):
    phc_interval = models.PhcIntervalsig.objects.all()
    return render(request,'interval_index.html',{'phc_interval':phc_interval})

def intervalshow1(request):
    phc_interval1 = models.PhcIntervalsig.objects.get(id=1)
    intervalsign1 = models.Intervalsig1.objects.all()
    return render(request,'interval_sign1.html',{'intervalsign1':intervalsign1,'phc_interval1':phc_interval1})

def intervalshow2(request):
    phc_interval2 = models.PhcIntervalsig.objects.get(id=2)
    intervalsign2 = models.Intervalsig2.objects.all()
    return render(request,'interval_sign2.html',{'intervalsign2':intervalsign2,'phc_interval2':phc_interval2})