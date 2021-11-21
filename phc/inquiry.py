from django.shortcuts import render
from mgr import models
from django.conf import settings

sip = settings.ALLOWED_HOSTS[0]
def get_ip(request):
    global sip
    host = request.get_host().split(":")
    sip = host[0]
    return sip

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
        results = models.Hashchain.objects.filter(sip=action['sip'],seq=1)
        print(results)
        if results.count() == 0:
          return render(request, 'inquiry.html',{'erro1': erro1, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
          return render(request,'inquiry.html', {'results':results,'username_ip':request.session["username_ip"], 'ip':sip, 'roomnum':request.session["ip"]})
    elif (action['sip']=="") & (action['dip']!="") & (int(action['constype'])==0) & (int(action['signtype'])==0):
        print(2)
        results = models.Hashchain.objects.filter(dip=action['dip'],seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',{'erro2': erro2, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',{'results':results,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']=="") & (int(action['constype'])!=0) & (int(action['signtype'])==0):
        print(3)
        results = models.Hashchain.objects.filter(contype=action['constype'],seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',{'erro3': erro3, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',{'results':results,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']=="") & (int(action['constype'])==0) & (int(action['signtype'])!=0):
        print(4)
        results = models.Hashchain.objects.filter(signtype=action['signtype'],seq=1)
        print(results)
        if results.count() == 0:
          return render(request, 'inquiry.html',{'erro4': erro4, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',{'results':results,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']!="") & (int(action['constype'])==0) & (int(action['signtype'])==0):
        print(12)
        results = models.Hashchain.objects.filter(sip=action['sip'],dip=action['dip'],seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',{'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',{'results':results,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']=="") & (int(action['constype'])!=0) & (int(action['signtype'])==0):
        print(13)
        results = models.Hashchain.objects.filter(sip=action['sip'],contype=action['constype'],seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',{'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',{'results':results,'username_ip': request.session["username_ip"], 'ip': sip, 'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']=="") & (int(action['constype'])==0) & (int(action['signtype'])!=0):
        print(14)
        results = models.Hashchain.objects.filter(sip=action['sip'], signtype=action['signtype'], seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']!="") & (int(action['constype'])!=0) & (int(action['signtype'])==0):
        print(23)
        results = models.Hashchain.objects.filter(dip=action['dip'], contype=action['constype'], seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']!="") & (int(action['constype'])==0) & (int(action['signtype'])!=0):
        print(24)
        results = models.Hashchain.objects.filter(dip=action['dip'], signtype=action['signtype'], seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']=="") & (int(action['constype'])!=0) & (int(action['signtype'])!=0):
        print(34)
        results = models.Hashchain.objects.filter(contype=action['constype'], signtype=action['signtype'], seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']!="") & (int(action['constype'])!=0) & (int(action['signtype'])==0):
        print(123)
        results = models.Hashchain.objects.filter(sip=action['sip'], dip=action['dip'], contype=action['constype'], seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']!="") & (int(action['constype'])==0) & (int(action['signtype'])!=0):
        print(124)
        results = models.Hashchain.objects.filter(sip=action['sip'], dip=action['dip'], signtype=action['signtype'],
                                                      seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']=="") & (int(action['constype'])!=0) & (int(action['signtype'])!=0):
        print(134)
        results = models.Hashchain.objects.filter(sip=action['sip'], contype=action['constype'], signtype=action['signtype'],
                                                      seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']=="") & (action['dip']!="") & (int(action['constype'])!=0) & (int(action['signtype'])!=0):
        print(234)
        results = models.Hashchain.objects.filter(dip=action['dip'], contype=action['constype'],
                                                      signtype=action['signtype'],
                                                      seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    elif (action['sip']!="") & (action['dip']!="") & (int(action['constype'])!=0) & (int(action['signtype'])!=0):
        print(1234)
        results = models.Hashchain.objects.filter(sip=action['sip'], dip=action['dip'], contype=action['constype'],
                                                      signtype=action['signtype'],
                                                      seq=1)
        if results.count() == 0:
          return render(request, 'inquiry.html',
                          {'erro5': erro5, 'username_ip': request.session["username_ip"], 'ip': sip,
                           'roomnum': request.session["ip"]})
        else:
          return render(request, 'inquiry.html',
                      {'results': results, 'username_ip': request.session["username_ip"], 'ip': sip,
                       'roomnum': request.session["ip"]})
    else:
        print(0)
        return render(request,'inquiry.html',{'erro0': erro0,'username_ip':request.session["username_ip"], 'ip':sip, 'roomnum':request.session["ip"]})
