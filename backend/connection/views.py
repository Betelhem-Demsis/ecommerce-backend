from django.shortcuts import render,get_object_or_404,redirect
from item.models import Item
from .models import Conversation
from .forms import ConversationForm
# Create your views here.

def new_connection(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)


    if item.created_by ==request.user:
        return redirect('dashboard:index')
    
    conversation=Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversation:
        return redirect('connection:detail',pk=conversation.first().id)

    if request.method=='POST':
        form=ConversationForm(request.POST)
        if form.is_valid():
            conversation=form.save(commit=False)
            conversation.item=item
            conversation.save()
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            return redirect('item:detail',pk=item_pk)
    else:
        form=ConversationForm()

    return render(request,'connection/new_connection.html')
