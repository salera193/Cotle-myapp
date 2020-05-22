from django.shortcuts import render, redirect
from .models import Recruit, Apply
from django.utils import timezone 
from django.shortcuts import get_object_or_404
from .forms import RecForm

def rec_list(request):
    
    Recs = Recruit.objects.order_by('pub_date').reverse()

    
    params ={
        'Recs': Recs, 
             }
    return render(request, 'Cotle/rec_list.html', params)

def rec_detail(request, pk):
    rec = get_object_or_404(Recruit, pk=pk)
    params={
        'rec':rec
        }
    return render(request, 'Cotle/rec_detail.html', params)    

def rec_new(request):
    if request.method =="POST":
        form = RecForm(request.POST)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.owner = request.user 
            rec.appcount = 0
            rec.pub_date = timezone.now()
            rec.save()
        return redirect(to='/')
        
    else:
        form = RecForm()        
    
    params = {'form':form }
    return render(request, 'Cotle/rec_edit.html', params)

def app_new(request, pk):
    
    app= Apply()
    app.owner = request.user
    app.recruit = get_object_or_404(Recruit,pk=pk)
    app.save()
    
    rec = get_object_or_404(Recruit, pk=pk)
    rec.appcount +=1
    rec.save()
    
    return redirect(to='/')