from .models import Invoice, Item

def get_items(invoice: Invoice):
    items = Item.objects.filter(invoice=invoice)
    for item in items:
        item.total = item.hours * item.rate
    return items

def get_total(items):
    return sum(item.total for item in items)