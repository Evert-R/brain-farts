from django.shortcuts import render
from dal import autocomplete

from tags.models import Categories, Topics, Projects
# Create your views here.


class CategoriesAutocomplete(autocomplete.Select2QuerySetView):
    """
    Autocomplete categories
    """

    def get_queryset(self):
        try:
            print(self.request.POST['create'])
        except:
            pass
        qs = Categories.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

    def has_add_permission(self, request):
        return True


class TopicsAutocomplete(autocomplete.Select2QuerySetView):
    """
    Autocomplete Topics
    """

    def get_queryset(self):

        qs = Topics.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class ProjectsAutocomplete(autocomplete.Select2QuerySetView):
    """
    Autocomplete Projects
    """

    def get_queryset(self):

        qs = Projects.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
