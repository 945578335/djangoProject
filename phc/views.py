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
    return render(request,'index.html', {'username_ip':request.session["username_ip"], 'ip':sip, 'roomnum':request.session["ip"]})

def trans_page(request):
    sip = get_ip(request)

    return render(request, 'trans_page.html', {'username_ip':request.session["username_ip"], 'ip':sip, 'roomnum':request.session["roomnum"]})

def datashow_page(request):
    sip = get_ip(request)
    return render(request, "performance_chart.html", {'username_ip':request.session["username_ip"], 'ip':sip, 'roomnum':request.session["ip"]});

def message_trace(request):
    sip = get_ip(request)
    # hash_chain_p =
    return render(request, 'message_trace.html',{'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})

def trace(request):
    sip = get_ip(request)
    dip = request.POST.get("dip")

    trace_message = request.POST.get("trace_message")

    db = models.HashChain.objects.filter(sip=sip, dip=dip, chainhash=trace_message)
    if db.count() == 0:
        return render(request, 'message_trace.html',
                             {'username_ip': request.session["username_ip"], 'ip': sip,
                              'roomnum': request.session["ip"], "trace_message": "输入的报文哈希链没有被追溯到！"})
    else:
        chaindb = models.HashChain.objects.filter(sip=sip, dip=dip).values_list()
        chain_db = []
        for chain in chaindb:
            chainmsg = {}
            chainmsg["sip"] = chain[1]
            chainmsg["dip"] = chain[2]
            chainmsg["seq"] = chain[3]
            chainmsg["msghash"] = chain[7]
            chainmsg["chainhash"] = chain[8]
            chainmsg["action"] = chain[12]
            chain_db.append(chainmsg)
        return render(request, "show_chain.html", {'username_ip':request.session["username_ip"], 'ip':sip, 'dip':dip, 'roomnum':request.session["roomnum"],"anchor":trace_message, "chainmsg":json.dumps(chain_db)})

def show_chain_page(request):
    sip = str(request.GET.get("sip"))
    dip = str(request.GET.get("dip"))
    chaindb = models.HashChain.objects.filter(sip=dip, dip=sip).values_list()
    chain_db = []

    for chain in chaindb:
        chainmsg = {}
        chainmsg["sip"] = chain[1]
        chainmsg["dip"] = chain[2]
        chainmsg["seq"] = chain[3]
        chainmsg["msghash"] = chain[7]
        chainmsg["chainhash"] = chain[8]
        chainmsg["action"] = chain[12]
        chain_db.append(chainmsg)
    return render(request, "show_chain.html", {'username_ip':request.session["username_ip"], 'ip':sip, 'dip':dip, 'roomnum':request.session["roomnum"], "chainmsg":json.dumps(chain_db)})


def inquiry_page(request):
    sip = get_ip(request)
    return render(request, 'inquiry.html',{'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})

def inquiry(request):
    sip = get_ip(request)
    action = request.POST
    erro0 = "请输入查询条件!"
    erro1 = "此发送方IP不存在!"
    erro2 = "此接收方IP不存在!"
    erro3 = "此构建方式的报文哈希链不存在!"
    erro4 = "此签名方式的报文哈希链不存在!"
    erro5 = "符合此条件的报文哈希链不存在!"
    if (action['sip']!="") & (action['dip']=="") & (int(action['constype'])==0) & (int(action['signtype'])==0):
        print(1)
        results = models.HashChain.objects.filter(sip=action['sip'],seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',{'erro1': erro1, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request,'inquiry.html', {'results':dbdict,'username_ip':request.session["username_ip"], 'ip':sip, 'roomnum':request.session["ip"]})
    elif (action['sip']=="") & (action['dip']!="") & (int(action['constype'])==0) & (int(action['signtype'])==0):
        print(2)
        results = models.HashChain.objects.filter(dip=action['dip'],seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',{'erro2': erro2, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',{'results':dbdict,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']=="") & (int(action['constype'])!=0) & (int(action['signtype'])==0):
        print(3)
        results = models.HashChain.objects.filter(contype=action['constype'],seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',{'erro3': erro3, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',{'results':dbdict,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']=="") & (int(action['constype'])==0) & (int(action['signtype'])!=0):
        print(4)
        results = models.HashChain.objects.filter(signtype=action['signtype'],seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',{'erro4': erro4, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',{'results':dbdict,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']!="") & (int(action['constype'])==0) & (int(action['signtype'])==0):
        print(12)
        results = models.HashChain.objects.filter(sip=action['sip'],dip=action['dip'],seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',{'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',{'results':dbdict,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']=="") & (int(action['constype'])!=0) & (int(action['signtype'])==0):
        print(13)
        results = models.HashChain.objects.filter(sip=action['sip'],contype=action['constype'],seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',{'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',{'results':dbdict,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']=="") & (int(action['constype'])==0) & (int(action['signtype'])!=0):
        print(14)
        results = models.HashChain.objects.filter(sip=action['sip'], signtype=action['signtype'], seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']!="") & (int(action['constype'])!=0) & (int(action['signtype'])==0):
        print(23)
        results = models.HashChain.objects.filter(dip=action['dip'], contype=action['constype'], seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']!="") & (int(action['constype'])==0) & (int(action['signtype'])!=0):
        print(24)
        results = models.HashChain.objects.filter(dip=action['dip'], signtype=action['signtype'], seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']=="") & (int(action['constype'])!=0) & (int(action['signtype'])!=0):
        print(34)
        results = models.HashChain.objects.filter(contype=action['constype'], signtype=action['signtype'], seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']!="") & (int(action['constype'])!=0) & (int(action['signtype'])==0):
        print(123)
        results = models.HashChain.objects.filter(sip=action['sip'], dip=action['dip'], contype=action['constype'], seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']!="") & (int(action['constype'])==0) & (int(action['signtype'])!=0):
        print(124)
        results = models.HashChain.objects.filter(sip=action['sip'], dip=action['dip'], signtype=action['signtype'],
                                                      seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']=="") & (int(action['constype'])!=0) & (int(action['signtype'])!=0):
        print(134)
        results = models.HashChain.objects.filter(sip=action['sip'], contype=action['constype'], signtype=action['signtype'],
                                                      seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']!="") & (int(action['constype'])!=0) & (int(action['signtype'])!=0):
        print(234)
        results = models.HashChain.objects.filter(dip=action['dip'], contype=action['constype'],
                                                      signtype=action['signtype'],
                                                      seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']!="") & (int(action['constype'])!=0) & (int(action['signtype'])!=0):
        print(1234)
        results = models.HashChain.objects.filter(sip=action['sip'], dip=action['dip'], contype=action['constype'],
                                                      signtype=action['signtype'],
                                                      seq=1).values_list()
        if results.count() == 0:
            return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
            dbdict = inquiryquery_to_list(results)
            return render(request, 'inquiry.html',
                      {'results': dbdict, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    else:
        print(0)
        return render(request,'inquiry.html',{'erro0': erro0,'username_ip':request.session["username_ip"], 'ip':sip, 'roomnum':request.session["ip"]})


def inquiryquery_to_list(results):

    dbdict = []

    for chain in results:
        chainmsg = {}
        chainmsg["sip"] = chain[1]
        chainmsg["dip"] = chain[2]
        chainmsg["contype"] = chain[4]
        chainmsg["signtype"] = chain[5]
        dbdict.append(chainmsg)
    return dbdict

