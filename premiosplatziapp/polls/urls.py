from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    #donde vamos: /polls/5/
    path("", views.IndexView.as_view(), name="index"),
    #donde vamos: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #donde vamos: /polls/5/results
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    #donde vamos: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]