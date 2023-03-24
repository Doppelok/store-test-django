from multi_store.models import UserShoppingCart
from shoping_cart.models import Likes


def baskets(request):
    user = request.user
    return {'baskets': UserShoppingCart.objects.filter(user=user) if user.is_authenticated else []}
