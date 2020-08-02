from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    list=[]
    for i in range(1,11):
        list.append(i)
    context={'list':list}
    return render(request,"red/index.html",context)
    

def fav(request):
    if(request.method== 'POST'):
        no1=request.POST.get('no1')
        no2=request.POST.get('no2')

        no11=int(no1)
        no22=int(no2)

        if(no11<no22):
            list=[]
            for i in range(no11,no22):
                list.append(i)
            context={'list':list}
            return render(request,"red/fav.html",context)
        
        elif(no22<no11):
            return HttpResponse("Fail")

