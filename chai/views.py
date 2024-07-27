from django.shortcuts import render,get_object_or_404
from .models import ChaiVarity,Notes
# Create your views here.
def all_chai(request):
    # give data of tea model
    tea = ChaiVarity.objects.all()
    return render(request,'chai/index.html',{'chais':tea})

def chaiDetails(request,chai_id):
    chai = get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'chai/chaidetails.html',{'chai':chai})

def order(request):
    return render(request,'chai/order.html')


def notes(request):
    note = Notes.objects.all()
    print(note)
    return render(request,'chai/notes.html',{'notes':note})