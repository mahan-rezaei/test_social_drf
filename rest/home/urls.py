from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


app_name = 'home'
urlpatterns = [
    path('vote/<int:question_id>/', views.CreateVoteView.as_view(), name='vote')
]


router = SimpleRouter()
router.register('questions', views.QuestionViewSet)
urlpatterns += router.urls
