from django.urls import reverse_lazy

from .forms import ContactForm
from django.views.generic import FormView

from common.views import CategoriesListMixin

from multi_store.models import ProductsCategories, ProductsSubGroup


# Create your views here.

class ContactView(CategoriesListMixin, FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("test:index")
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
