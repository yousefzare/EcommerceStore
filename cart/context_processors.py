from cart.card import Card


def card(request):
    return {
        'card': Card(request)
    }
