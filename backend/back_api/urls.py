from django.urls import path
from .views import NavItemsViews, AdvantageTileItemsViews

urlpatterns = [
    path('nav-items/', NavItemsViews.as_view()),
    path('adv-items/', AdvantageTileItemsViews.as_view()),
]