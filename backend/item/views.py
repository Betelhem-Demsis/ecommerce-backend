from django.shortcuts import get_object_or_404, render,redirect
from django.db.models import Q
from .models import Item,Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm ,EditItemForm

def items(request):
    query=request.GEt('query')
    catagory_id=request.GET.get('catagory',0)
    catagories=Category.objects.all()
    items=Item.objects.filter(is_sold=False)
     
    if catagory_id:
        items=items.filter(category_id=catagory_id)
        
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,'item/items.html',{
        'items':items,
        'query':query,
        'catagories':catagories,
       ' catagory_id':int(catagory_id)
    })


def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
        'item':item, 
        'related_items':related_items
        })

@login_required
def new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    else:
        form=NewItemForm()
    return render(request,'item/form.html',{
        'form':form,
        'tirle':'new item'
    })

@login_required
def edit(request):
    item=get_object_or_404(Item, pk=pk ,created_by=request.user)
    if request.method=='POST':
        form=EditItemForm(request.POST,request.FILES)

        if form.is_valid():
            form.save
            return redirect('item:detail',pk=item.id)
    else:
        form=EditItemForm(instance=item)

    return render( request,'item/form.html',{
        'form':form,
        'title':'edit item'
    })
 
@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

