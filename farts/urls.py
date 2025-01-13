from django.urls import path

from . import views

app_name = 'farts'

urlpatterns = [
    path('add-fart/', views.add_fart, name='add_fart'),
    path('<int:pk>', views.show_fart, name='show_fart'),
    path('edit-fart/<int:pk>', views.add_fart, name='add_fart'),
    path('delete-fart/<int:pk>', views.delete_fart, name='delete_fart')
]
