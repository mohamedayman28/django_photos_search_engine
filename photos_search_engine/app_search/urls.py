from app_search import views

from django.urls import path


urlpatterns = [
    # index_page view
    path('', views.index_page, name='index_page'),
    # search_results_page view
    path('search/', views.search_results_page, name='search_results_page'),
]
