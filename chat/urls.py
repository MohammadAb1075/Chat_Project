from django.urls import path, re_path

from chat.views import ChatView,MessageListView,ConversationList

urlpatterns = [
    # path('list/', views.user_list),
    # re_path('list/(?P<id>\d{0,10})', views.conversation_view),
    path('message/',ChatView.as_view()),
    path('message/list/',MessageListView.as_view()),
    path('conversation/',ConversationList.as_view()),

]
