from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Fart
from .forms import FartForm, FilterForm

@login_required
def add_fart(request, pk=None):
    """
    Add or edit Fart
    """
    # active_user = request.user
    this_type = 'NEW'
    if pk:
        try:
            this_fart = Fart.objects.get(pk=pk)
            form = FartForm(instance=this_fart)
            this_type = this_fart.type
        except:
            messages.error(request,
                           'This work does not exist')
            return redirect('farts')
    else:
        this_fart = None
        form = FartForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        this_form = FartForm(request.POST, request.FILES, instance=this_fart)
        # check whether it's valid:
        if this_form.is_valid():
            this_fart = this_form.save(commit=False)
            this_fart.date = timezone.now()
            this_fart.save()
            filter_form = FilterForm()
            all_farts = Fart.objects.all()
            # this_beat.user = active_user
            # this_beat.save()
            # next = request.POST.get('next', '/')
            return render(request, "farts.html", {
                "farts": all_farts,
                "filter_form": filter_form
            })
    else:
        return render(request, "add-fart.html", {
            "form": form,
            "fart_type": this_type
        })

@login_required
def farts(request):
    """
    Add or edit Fart
    """
    filter_form = FilterForm()
    all_farts = Fart.objects.all().order_by('-date')
    filtered_type = 'BRAIN'
    if request.method == 'POST':
        filter_farts = FilterForm(request.POST)

        if filter_farts.is_valid():
            try:
                filter_types = filter_farts.cleaned_data['type']
                print(filter_types)
                for filter_type in filter_types:
                    print(filter_type)
                    filtered_type = filter_type
                    all_farts = all_farts.filter(type=filter_type)
                #filter_form.fields['type'].initial = filter_types

            except:
                pass
            try:
                filter_category = filter_farts.cleaned_data['category'].id
                all_farts = all_farts.filter(category=filter_category)
                filter_form.fields['category'].initial = filter_category
            except:
                pass
            try:
                filter_topic = filter_farts.cleaned_data['topic'].id
                all_farts = all_farts.filter(topic=filter_topic)
                filter_form.fields['topic'].initial = filter_topic
            except:
                pass
            try:
                filter_project = filter_farts.cleaned_data['project'].id
                all_farts = all_farts.filter(project=filter_project)
                filter_form.fields['project'].initial = filter_project
            except:
                pass
    return render(request, "farts.html", {
                  "farts": all_farts,
                  "filter_form": filter_form,
                  "filtered_type": filtered_type
                  })

@login_required
def delete_fart(request, pk=None):
    """
    Delete Fart
    """
    this_fart = Fart.objects.get(pk=pk)
    if this_fart.image:
        this_fart.image.delete()
    if this_fart.audio:
        this_fart.audio.delete()
    this_fart.delete()
    messages.success(request,
                     'Successfully unfarted!')
    return redirect('farts')

@login_required
def show_fart(request, pk=None):
    """
    Show Fart
    """
    this_fart = Fart.objects.get(pk=pk)

    return render(request, "show-fart.html", {
                  "fart": this_fart
                  })
