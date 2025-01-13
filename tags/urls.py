from django.urls import path
from tags.views import CategoriesAutocomplete, TopicsAutocomplete, ProjectsAutocomplete
from tags.models import Categories, Topics, Projects

app_name = 'tags'

urlpatterns = [
    path('filter-categories-autocomplete/', CategoriesAutocomplete.as_view(
        model=Categories), name='categories_autocomplete'),
    path('filter-topics-autocomplete/', TopicsAutocomplete.as_view(
        model=Topics), name='topics_autocomplete'),
    path('filter-projects-autocomplete/', ProjectsAutocomplete.as_view(
        model=Projects), name='projects_autocomplete'),
    path('categories-autocomplete/', CategoriesAutocomplete.as_view(
        model=Categories,
        create_field='name'), name='categories_autocomplete'),
    path('topics-autocomplete/', TopicsAutocomplete.as_view(
        model=Topics,
        create_field='name'), name='topics_autocomplete'),
    path('projects-autocomplete/', ProjectsAutocomplete.as_view(
        model=Projects,
        create_field='name'), name='projects_autocomplete')
]
