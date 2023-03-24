from http import HTTPStatus

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DeleteView, CreateView, ListView
from common.views import EmailNewsMixin

from .models import Cart, CartItem, Likes, CheckoutOrder
from multi_store.models import UserShoppingCart
from .forms import ShoppingCartForm, CheckOutForm
from django.conf import settings
from common.views import CategoriesListMixin

from multi_store.models import ProductsCategories, ProductsSubGroup, UserShoppingCart

import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = settings.DOMAIN_NAME
endpoint_secret = settings.STRIPE_ENDPOINT_SECRET


class CartView(EmailNewsMixin, CategoriesListMixin, TemplateView):
    template_name = 'shoping_cart/cart.html'
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()

    # form_class = ShoppingCartForm

    def get_context_data(self, **kwargs):
        data = super(CartView, self).get_context_data(**kwargs)
        data['shopping_cart'] = UserShoppingCart.objects.filter(user=self.request.user)
        return data


@login_required
def add_to_basket(request, product_id):
    baskets = UserShoppingCart.objects.filter(user=request.user, product_id=product_id)

    if not baskets.exists():
        UserShoppingCart.objects.create(user=request.user, product_id=product_id, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def del_from_basket(request, product_id):
    baskets = UserShoppingCart.objects.filter(user=request.user, product_id=product_id)

    if baskets.exists():
        basket = baskets.first()
        if basket.quantity > 0:
            basket.quantity -= 1
            basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_basket(request, basket_id):
    basket = UserShoppingCart.objects.filter(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class DeleteFromCartView(DeleteView):
    model = Cart
    success_url = reverse_lazy('shoping_cart:cart')


class CheckOutView(EmailNewsMixin, CategoriesListMixin, CreateView):
    template_name = 'shoping_cart/checkout.html'
    products_categories = ProductsCategories.objects.all()
    products_groups = ProductsSubGroup.objects.all()
    form_class = CheckOutForm
    success_url = reverse_lazy('shoping_cart:checkout')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1Mj2IOFJ5I6YSCca27Dwf1lS',
                        'quantity': 1,
                    },
                ],
                metadata={'checkout_id': self.object.id},
                mode='payment',
                success_url='{}{}'.format(YOUR_DOMAIN, reverse('shoping_cart:success_view')),
                cancel_url='{}{}'.format(YOUR_DOMAIN, reverse('shoping_cart:cancel_view')),
            )
        except Exception as e:
            return repr(e)

        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Fulfill the purchase...
        fulfill_order(session)

    # Passed signature verification
    return HttpResponse(status=200)


def fulfill_order(session):
    order = CheckoutOrder.objects.get(id=session['metadata']['checkout_id'])
    order.status_paid(mark=True)


class LikesView(TemplateView):
    template_name = 'shoping_cart/likes.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['likes'] = Likes.objects.filter(user=self.request.user)
        return data


@login_required
def add_to_likes(request, product_id):
    likes = Likes.objects.filter(user=request.user, product_id=product_id)

    if not likes.exists():
        Likes.objects.create(user=request.user, product_id=product_id)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def del_from_likes(request, product_id):
    like = Likes.objects.filter(user=request.user, product_id=product_id)
    like.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class SuccessView(TemplateView):
    template_name = 'shoping_cart/success.html'


class CancelView(TemplateView):
    template_name = 'shoping_cart/cart.html'


class CheckoutsListView(ListView):
    template_name = 'shoping_cart/checkouts_history.html'
    model = CheckoutOrder

    def get_queryset(self):
        data = super().get_queryset()
        return data.filter(initiator=self.request.user).order_by('-id')


class OrderDetailView(DeleteView):
    template_name = 'shoping_cart/order_detail.html'
    model = CheckoutOrder
