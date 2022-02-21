from django.urls import path
from .views import RatingDetail, RatingList

app_name = 'api'

urlpatterns = [
    path('<int:pk>', RatingDetail.as_view()),
    path('', RatingList.as_view())
]
