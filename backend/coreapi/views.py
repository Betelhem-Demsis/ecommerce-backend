from django.shortcuts import render,redirect
from item.models import Category,Item
from django.shortcuts import get_object_or_404
from .forms import SignupForm



def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    catagories=Category.objects.all()
    return render(request,'coreapi/index.html',{   
        'catagories':catagories,
        'items':items,
    })
def contact(request):
    return render(request,'coreapi/contact.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form=SignupForm
    return render(request,'coreapi/signup.html',{
        'form':form
    })
