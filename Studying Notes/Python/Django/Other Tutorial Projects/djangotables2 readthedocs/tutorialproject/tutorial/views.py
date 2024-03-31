from django.shortcuts import render 
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .models import Person
from .tables import PersonTable
from .filters  import PersonFilter

class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = PersonTable
    model = Person
    template_name = "tutorial/template.html"
    
    filterset_class = PersonFilter