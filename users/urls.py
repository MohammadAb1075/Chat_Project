from django.urls import path, re_path, include

# from . import views
from . import views

urlpatterns = [
    # path('list/', views.user_list_view),
    path('item/', views.UserListItemView.as_view()),
    # path('login/', views.login_view),
    path('login/', views.LoginView.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('user/list/', views.UserListView.as_view()),
    # path('profile/', views.EditProfile.as_view()),
    path('profile/', views.EditProfileView.as_view())
    # path('', include('django.contrib.auth.urls')), # new
]

















# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('list/',views.user_list_view),
#     # path('list/', views.user_list),
#     # re_path('list/(?P<id>\d{0,10})', views.conversation_view),
#
#     # path('item/',views.user_list_item_view),
#     path('item/',views.UserListItemView.as_view()),
#     path('login/',views.LoginView.as_view()),
#     path('signup/',views.SignUpView.as_view()),
#
# ]
