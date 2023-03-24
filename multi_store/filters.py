import django_filters
from django import forms
from django.db import models
from multi_store.models import *


class IPProductFilter(django_filters.FilterSet):
    attribute__resolution = django_filters.ModelMultipleChoiceFilter(queryset=ResolutionAttrValue.objects.all(),
                                                                     widget=forms.CheckboxSelectMultiple())

    attribute__lens = django_filters.ModelMultipleChoiceFilter(queryset=LensAttrValue.objects.all(),
                                                               widget=forms.CheckboxSelectMultiple())

    attribute__case = django_filters.ModelMultipleChoiceFilter(queryset=CaseAttrValue.objects.all(),
                                                               widget=forms.CheckboxSelectMultiple())

    attribute__ir = django_filters.ModelMultipleChoiceFilter(queryset=IRAttrValue.objects.all(),
                                                             widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Products
        fields = ['attribute__resolution', 'attribute__lens', 'attribute__case', 'attribute__ir']
