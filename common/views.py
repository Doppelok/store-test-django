from users.forms import EmailNewsForm


class CategoriesListMixin:
    products_categories = None
    products_groups = None

    def get_context_data(self, **kwargs):
        data = super(CategoriesListMixin, self).get_context_data(**kwargs)
        data['products_categories'] = self.products_categories
        data['products_groups'] = self.products_groups
        return data


class EmailNewsMixin:
    # form = EmailNewsForm
    pass
