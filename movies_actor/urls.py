from django.urls import path
from .views import ActorView,MovieView,AcMv
urlpatterns = [
    path('actor',ActorView.as_view()),
    path('movie',MovieView.as_view()),
    path('acmv',AcMv.as_view())
]