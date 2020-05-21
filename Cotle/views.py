from django.shortcuts import render
from .models import Recruit
from django.utils import timezone 
from django.shortcuts import get_object_or_404
from .forms import RecForm

def rec_list(request):
    
    Recs = Recruit.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    
    params ={'Recs': Recs}
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
            rec.pub_date = timezone.now()
            rec.save()
    else:
        form = RecForm()        
    
    params = {'form':form }
    return render(request, 'Cotle/rec_edit.html', params)