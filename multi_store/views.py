from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, ListView, FormView
from .filters import IPProductFilter
from .models import *
from common.views import CategoriesListMixin, EmailNewsMixin


# Create your views here.


class IndexView(EmailNewsMixin, CategoriesListMixin, TemplateView):
    template_name = 'multi_store/index.html'
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        data['products'] = Products.objects.all().order_by('-id')[:4]
        return data

    def get(self, request, *args, **kwargs):
        data = super().get(request, *args, **kwargs)
        search = self.request.GET.get('search')
        if search:
            url = reverse('test:search', args=(search,))
            return HttpResponseRedirect(url)
        return data


class ShopCategoryView(EmailNewsMixin, CategoriesListMixin, ListView):
    template_name = 'multi_store/shop_categories.html'
    queryset = ProductsCategories.objects.all()
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()


class ShopGroupsView(EmailNewsMixin, CategoriesListMixin, ListView):
    template_name = 'multi_store/shop_groups.html'
    model = ProductsSubGroup
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()

    def get_queryset(self):
        data = super(ShopGroupsView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return data.filter(product_category_id=category_id)


class ShopProductsView(EmailNewsMixin, CategoriesListMixin, ListView):
    template_name = 'multi_store/shop.html'
    model = Products
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        queryset = self.get_queryset()
        filters = IPProductFilter(self.request.GET, queryset)
        a = self.request
        b = self.kwargs
        # product_attribute = TypicalProductAttr.objects.filter(sub_group_id=self.kwargs['group_id'])
        # attr_value = [AttrValue.objects.filter(typical_pr_attr_id=tpa) for tpa in product_attribute]

        # data['product_attribute'] = product_attribute
        # data['attr_value'] = attr_value
        data['filters'] = filters
        data['groups'] = self.kwargs['group_id']
        return data

    def get_queryset(self):
        data = super(ShopProductsView, self).get_queryset()
        group_id = self.kwargs.get('group_id')
        data = data.filter(product_group_id=group_id)
        filters = IPProductFilter(self.request.GET, queryset=data)
        return filters.qs


class ProductDetailView(EmailNewsMixin, CategoriesListMixin, DetailView):
    model = Products
    template_name = 'multi_store/product_detail.html'
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()


class SearchView(CategoriesListMixin, ListView):
    template_name = 'multi_store/search.html'
    model = Products
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()

    def get_queryset(self):
        data = super().get_queryset()
        name = self.kwargs.get('name')
        return data.filter(name__contains=name)
