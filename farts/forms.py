from enum import auto
from unicodedata import category
from django.forms import ModelForm, Textarea
from django import forms
from farts.models import Fart
from tags.models import Categories, Projects, Topics
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, LayoutObject
from dal import autocomplete


class FartForm(ModelForm):
    """
    Form to add a fart
    """

    class Meta:
        """
        Form content
        """
        model = Fart
        fields = ['category', 'topic',
                  'project', 'title', 'type', 'text', 'audio', 'image', 'link']
        widgets = {
            'type': forms.RadioSelect(),
            'category': autocomplete.ModelSelect2(url='/tags/categories-autocomplete/'),
            'topic': autocomplete.ModelSelect2(url='/tags/topics-autocomplete/'),
            'project': autocomplete.ModelSelect2(url='/tags/projects-autocomplete/'),
            'image': forms.ClearableFileInput(attrs={'capture': 'user'})

        }
        labels = {
            'type': '',
            'text': 'Input text:',
            'audio': 'Upload audio:',
            'image': 'Upload image:',
            'link': 'Add link:'
        }
        help_texts = {

        }

    def __init__(self, *args, **kwargs):
        super(FartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        self.helper.use_custom_control = True
        self.helper.form_style = 'inline'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-12'
        self.helper.field_class = 'col-12'
        self.helper.form_tag = False


class FilterForm(forms.Form):
    """
    Filter Categories
    """
    TYPE_CHOICES = [
        ('TEXT', 'T'),
        ('AUDIO', 'A'),
        ('IMAGE', 'I'),
        ('LINK', 'L'),
    ]

    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        empty_label="-- Category --",
        required=False,
        widget=autocomplete.ModelSelect2(url='/tags/filter-categories-autocomplete', attrs={
            'data-placeholder': '-- Category --'
        })

    )
    topic = forms.ModelChoiceField(
        queryset=Topics.objects.all(),
        empty_label="-- Topic --",
        required=False,
        widget=autocomplete.ModelSelect2(url='/tags/filter-topics-autocomplete', attrs={
            'data-placeholder': '-- Topic --'
        })
    )
    project = forms.ModelChoiceField(
        queryset=Projects.objects.all(),
        empty_label="-- Project --",
        required=False,
        widget=autocomplete.ModelSelect2(url='/tags/filter-projects-autocomplete', attrs={
            'data-placeholder': '-- Project --'
        })
    )
    type = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TYPE_CHOICES,
    )

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['category'].label = False
        self.fields['topic'].label = False
        self.fields['project'].label = False
        self.helper.use_custom_control = True
        self.helper.form_style = 'inline'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-12'
        self.helper.field_class = 'col-12'
        self.helper.form_tag = False
        self.helper.help_text_inline = True
