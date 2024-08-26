from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation
from .forms import ConversationForm
# Create your views here.


@login_required
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

@login_required
def inbox(request):
    conversations=Conversation.objects.filter(members__in=[request.user.id])

    return render(request,'conversation/inbox.html',{
        'conversations':conversations
    })

@login_required
def detail(request,pk):
    conversation=Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method=='POST':
        form=ConversationForm(request.POST)

        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()

            conversation.save()
            return redirect('connection:detail',pk=pk)
        else:
           form=ConversationForm()


    return render(request,'conversation/detail.html',{
        'conversation':conversation,
        'form':form
    })
