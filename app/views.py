from django.shortcuts import render
import datetime

# Create your views here.
def filters(request):

    dates=datetime.datetime.now()
    d={'data':'We aRE soFTWArE dEVElopeRs','dates':dates,'b':10}
    return render(request,'filters.html',context=d)