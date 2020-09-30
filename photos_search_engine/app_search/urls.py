
from app_search import views

from django.urls import path


urlpatterns = [
    # search_results_page view
    path('', views.search_results_page, name='search_results_page'),
]
