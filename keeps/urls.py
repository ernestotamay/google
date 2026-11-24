from django.urls import path
from . import views

app_name = "keeps"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),          # 127.0.0.1:8000/keeps/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), 
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:tag_id>/vote/", views.vote, name="vote"),
]