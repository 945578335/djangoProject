from django.shortcuts import render
import json
from phc import models
from mgr import views
from django.conf import settings
from phc.consumers import hash_chain_p
from phc import basic_hash_chain

sip = settings.ALLOWED_HOSTS[0]
def get_ip(request):
    global sip
    host = request.get_host().split(":")
    sip = host[0]
    return sip

def indexshow(request):
    sip = get_ip(request)
    return render(request,'index.html', {'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def basic_hash_index(request):
    sip = get_ip(request)
    phc_basic = models.PhcBasic.objects.all()
    return render(request, 'basic_index.html',{'phc_basic':phc_basic, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def basicshow1(request):
    sip = get_ip(request)
    phc_basic1 = models.PhcBasic.objects.get(id=1)
    basicchain1 = models.Basicchain1.objects.all()
    return render(request,'basic_hash1.html',{'basicchain1':basicchain1,'phc_basic1':phc_basic1, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def basicshow2(request):
    sip = get_ip(request)
    phc_basic2 = models.PhcBasic.objects.get(id=2)
    basicchain2 = models.Basicchain2.objects.all()
    return render(request,'basic_hash2.html',{'basicchain2':basicchain2,'phc_basic2':phc_basic2, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})


def share_hash_index(request):
    sip = get_ip(request)
    phc_share = models.PhcShare.objects.all()
    return render(request, 'share_index.html',{'phc_share':phc_share, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def shareshow1(request):
    sip = get_ip(request)
    phc_share1 = models.PhcShare.objects.get(id=1)
    sharechain1 = models.Sharechain1.objects.all()
    return render(request,'share_hash1.html',{'sharechain1':sharechain1,'phc_share1':phc_share1, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def shareshow2(request):
    sip = get_ip(request)
    phc_share2 = models.PhcShare.objects.get(id=2)
    sharechain2 = models.Sharechain2.objects.all()
    return render(request,'share_hash2.html',{'sharechain2':sharechain2,'phc_share2':phc_share2, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})


def salt_hash_index(request):
    sip = get_ip(request)
    phc_salt = models.PhcSalt.objects.all()
    return render(request, 'salt_index.html',{'phc_salt':phc_salt, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def saltshow1(request):
    sip = get_ip(request)
    phc_salt1 = models.PhcSalt.objects.get(id=1)
    saltchain1 = models.Saltchain1.objects.all()
    return render(request,'salt_hash1.html',{'saltchain1':saltchain1,'phc_salt1':phc_salt1, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def saltshow2(request):
    sip = get_ip(request)
    phc_salt2 = models.PhcSalt.objects.get(id=2)
    saltchain2 = models.Saltchain2.objects.all()
    return render(request,'salt_hash2.html',{'saltchain2':saltchain2,'phc_salt2':phc_salt2, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})


def mutual_hash_index(request):
    sip = get_ip(request)
    phc_mutual = models.PhcMutual.objects.all()
    return render(request, 'mutual_index.html',{'phc_mutual':phc_mutual, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def mutualshow(request):
    sip = get_ip(request)
    phc_mutual = models.PhcMutual.objects.get(id=1)
    mutualchain = models.Mutualchain.objects.all()
    return render(request,'mutual_hash.html',{'mutualchain':mutualchain,'phc_mutual':phc_mutual, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})


def first_sign_index(request):
    sip = get_ip(request)
    phc_first = models.PhcFirstsig.objects.all()
    return render(request,'first_index.html',{'phc_first':phc_first, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def firstshow1(request):
    sip = get_ip(request)
    phc_first1 = models.PhcFirstsig.objects.get(id=1)
    firstsign1 = models.Firstsig1.objects.all()
    return render(request,'first_sign1.html',{'firstsign1':firstsign1,'phc_first1':phc_first1, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def firstshow2(request):
    sip = get_ip(request)
    phc_first2 = models.PhcFirstsig.objects.get(id=2)
    firstsign2 = models.Firstsig2.objects.all()
    return render(request,'first_sign2.html',{'firstsign2':firstsign2,'phc_first2':phc_first2, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})


def final_sign_index(request):
    sip = get_ip(request)
    phc_final = models.PhcFinalsig.objects.all()
    return render(request,'final_index.html',{'phc_final':phc_final, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def finalshow1(request):
    sip = get_ip(request)
    phc_final1 = models.PhcFinalsig.objects.get(id=1)
    finalsign1 = models.Finalsig1.objects.all()
    return render(request,'final_sign1.html',{'finalsign1':finalsign1,'phc_final1':phc_final1, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def finalshow2(request):
    sip = get_ip(request)
    phc_final2 = models.PhcFinalsig.objects.get(id=2)
    finalsign2 = models.Finalsig2.objects.all()
    return render(request,'final_sign2.html',{'finalsign2':finalsign2,'phc_final2':phc_final2, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})


def interval_sign_index(request):
    sip = get_ip(request)
    phc_interval = models.PhcIntervalsig.objects.all()
    return render(request,'interval_index.html',{'phc_interval':phc_interval, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def intervalshow1(request):
    sip = get_ip(request)
    phc_interval1 = models.PhcIntervalsig.objects.get(id=1)
    intervalsign1 = models.Intervalsig1.objects.all()
    return render(request,'interval_sign1.html',{'intervalsign1':intervalsign1,'phc_interval1':phc_interval1, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def intervalshow2(request):
    sip = get_ip(request)
    phc_interval2 = models.PhcIntervalsig.objects.get(id=2)
    intervalsign2 = models.Intervalsig2.objects.all()
    return render(request,'interval_sign2.html',{'intervalsign2':intervalsign2,'phc_interval2':phc_interval2, 'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def trans_page(request):
    sip = get_ip(request)
    return render(request, 'trans_page.html', {'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]})

def datashow_page(request):
    sip = get_ip(request)
    return render(request, "performance_chart.html", {'username':request.session["username"], 'ip':sip, 'roomnum':request.session["ip"]});

def message_trace(request):
    sip = get_ip(request)
    # hash_chain_p =
    return render(request, 'message_trace.html',{'username': request.session["username"], 'ip': sip, 'roomnum': request.session["ip"]})

def trace(request):
    sip = get_ip(request)
    username_id = request.POST.get("username_id")
    print("username_id", username_id)
    trace_message = request.POST.get("trace_message")
    print("trace_message", trace_message)
    trace = "无法追溯"
    if hash_chain_p.__contains__(username_id) == False:
        return render(request, 'message_trace.html', {'username': request.session["username"], 'ip': sip, 'roomnum': request.session["ip"], "trace_message": trace})
    hash_chain = hash_chain_p[username_id]
    trace_flag = hash_chain.isContain(trace_message)
    trace = ""
    if trace_flag == True:
        trace = "此id的报文哈希链能被追溯"
    return render(request, 'message_trace.html', {'username': request.session["username"], 'ip': sip, 'roomnum': request.session["ip"], "trace_message":trace})