from django.urls import path
from mddb_portal import views


urlpatterns = [
    path('exampleview/', views.example_view, name='exampleview')
]
