from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
    path('api-token-auth/', auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


#
# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODQyODg5MiwiaWF0IjoxNzM3ODI0MDkyLCJqdGkiOiIxOGFlMzcwNTNkMTU0YzNmYmFmZmZlMzFiMDQ4YjQxOCIsInVzZXJfaWQiOjF9.u3mZGYDzkKrP9JVtC5AIFMgvVvdwVjfP64Ghzk9gDnk",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3OTEwNDkyLCJpYXQiOjE3Mzc4MjQwOTIsImp0aSI6IjJjYTkxYTAwZTUwNzQ2ZmM4Zjc0MjhjYjFiNmU5NWU0IiwidXNlcl9pZCI6MX0.Ag8ZN49Bsuy-__I6PGZvfgH8F_dSHgQViqFWBDjeU4s"