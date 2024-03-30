from django.shortcuts import render
from django.http import HttpResponse
from datacollection.models import MedicineData
# Create your views here.
def home(request):
    return render(request, "datacollection/home.html")

def landingpage(request):
    # return HttpResponse('This is success!')
    if request.method=='POST':
        pname = request.POST['pname']
        batchid = request.POST['batchid']
        lotno = request.POST['lotno']
        mandate = request.POST['mandate']
        exdate = request.POST['exdate']
        protocolid = request.POST['protocolid']
        # print(pname, batchid, lotno, mandate, exdate, protocolid)
        data = MedicineData(pname=pname, batchid=batchid, lotno=lotno, mandate=mandate, exdate=exdate, protocolid=protocolid)
        data.save()
        print("The data is written.")
    return render(request, "datacollection/landingpage.html")