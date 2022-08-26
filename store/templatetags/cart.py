from django import template


register = template.Library()

@register.filter(name='NOT')
def NOT(path):
    if path:
        return False
    return True
@register.filter(name='comp3')
def comp3(path):
    if path == '/order/':
        return False
    return True

@register.filter(name='comp')
def comp(path):
    if path == '/signup/':
        return False
    return True

@register.filter(name='comp2')
def comp2(path):
    if path == '/cart/':
        return False
    return True


@register.filter(name='logined')
def logined(path):
    if path:
        return 0
    return 1

@register.filter(name='Needpath')
def logined(request):
    # print(request.path)
    print(request.GET.get('category'))
    if request=="/":
        return 0
    return request.GET.get('category')

@register.filter(name='comp1')
def comp1(path):
    if path == '/login/':
        return False

@register.filter(name='cartitems')
def cartitems(data):
    count=0
    for item in data:
        count=data.get(item)+count
    return count


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    if not cart:cart={}
    keys = cart.keys()
    keys = list(keys)
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='quantity')
def quantity(product, cart):
    if not cart:cart={}
    keys = cart.keys()
    keys = list(keys)
    for id in keys:
        if int(id) == product.id:
            return cart[id]
    return False
