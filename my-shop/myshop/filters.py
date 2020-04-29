# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.widgets import Select
from django.utils.translation import ugettext_lazy as _
from django_filters import FilterSet

from djng.forms import NgModelFormMixin
from djng.styling.bootstrap3.forms import Bootstrap3Form

from shop.filters import ModelChoiceFilter

from myshop.models import Manufacturer, Product


class FilterForm(NgModelFormMixin, Bootstrap3Form):
    scope_prefix = 'filters'


class ManufacturerFilterSet(FilterSet):
    manufacturer = ModelChoiceFilter(
        queryset=Manufacturer.objects.all(),
        widget=Select(attrs={'ng-change': 'filterChanged()'}),
        empty_label=_("Any Manufacturer"),
        help_text=_("Restrict product on this manufacturer only"),
    )

    class Meta:
        model = Product
        form = FilterForm
        fields = ['manufacturer']

    @classmethod
    def get_render_context(cls, request, queryset):
        # create filter set with bound form, to enable the selected option
        filter_set = cls(data=request.GET)

        # we only want to show manufacturers for products available in the current list view
        filter_field = filter_set.filters['manufacturer'].field
        filter_field.queryset = filter_field.queryset.filter(
            id__in=queryset.values_list('manufacturer_id'))
        return dict(filter_set=filter_set)
