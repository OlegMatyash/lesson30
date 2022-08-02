from django.urls import path

import users
from users import views

urlpatterns = [
    path('', users.views.UserView.as_view()),
    path('<int:pk>/', users.views.UserDetailView.as_view()),
    path('create/', users.views.UserCreateView.as_view()),
    path('<int:pk>/update/', users.views.UserUpdateView.as_view()),
    path('<int:pk>/delete/', users.views.UserDeleteView.as_view()),
]
