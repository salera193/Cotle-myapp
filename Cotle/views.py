from django.shortcuts import render
from .models import Recruit
from django.utils import timezone 

def rec_list(request):
    
    Recs = Recruit.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    
    params ={'Recs': Recs}
    return render(request, 'Cotle/rec_list.html', params)
