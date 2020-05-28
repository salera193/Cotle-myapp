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
    apps = rec.apply_rec.all()
    params={
        'rec':rec,
        'apps': apps,
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

    rec = get_object_or_404(Recruit, pk=pk)
    #アプライしたかどうかの確認
    is_app = Apply.objects.filter(owner=request.user).filter(recruit=rec).count()
       
    if is_app==0:
    
        app= Apply()
        app.owner = request.user
        app.recruit = get_object_or_404(Recruit,pk=pk)
        app.save()
            
        rec.appcount +=1
        rec.save()
    
    
    return redirect(to='/')

def app_del(request, pk):
    if request.user.is_authenticated:
    
        rec = get_object_or_404(Recruit,pk=pk) 
        rec.appcount -= 1
        rec.save()

        
        app = Apply.objects.filter(owner=request.user).filter(recruit=rec)
        app.delete()
    return redirect(to='/')

def acc_app(request, pk, rpk):
    
    app = get_object_or_404(Apply,pk=pk)
    rec = get_object_or_404(Recruit,pk=rpk)
    
    #accept処理
    app.accept = True
    app.save()
    
    
    return redirect('rec_detail', pk=rec.pk)


def acc_cancel(request, pk, rpk):
    
    app = get_object_or_404(Apply,pk=pk)
    rec = get_object_or_404(Recruit,pk=rpk)
    
    #accept処理
    app.accept = False
    app.save()
    
    
    return redirect('rec_detail', pk=rec.pk)
