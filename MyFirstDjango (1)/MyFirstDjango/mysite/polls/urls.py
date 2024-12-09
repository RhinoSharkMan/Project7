from tkinter.font import names

from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>", views.detail, name="detail"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:question_id>/results/", views.results, name="results"),
    path('surveys/', views.survey_list, name='survey_list'),
    path('surveys/<int:survey_id>/', views.survey_detail, name='survey_detail'),
]