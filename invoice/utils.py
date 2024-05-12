from .models import Invoice, Item

DATE_FORMAT = "%B %d, %Y"

def get_invoice_items(invoice: Invoice):
    items = Item.objects.filter(invoice=invoice)
    for item in items:
        item.total = item.hours * item.rate
    return items

def get_invoice_total(items):
    return sum(item.total for item in items)
