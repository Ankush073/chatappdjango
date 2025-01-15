from django.shortcuts import render
from django.contrib.auth import get_user_model
from chatapp.models import ChatModel
# Create your views here.


User = get_user_model()
def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'main/chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})
