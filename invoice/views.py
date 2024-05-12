from .models import Invoice, Client, Item
from .utils import *
from payment.models import Payment
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.template import Engine, Context
from weasyprint import HTML

def index(request):
    invoices = Invoice.objects.order_by("number")[:10]
    for invoice in invoices:
        invoice.total = get_invoice_total(get_invoice_items(invoice))
    context = {"invoices": invoices}
    return render(request, "invoice/index.html", context)

def create(request):
    clients = Client.objects.order_by("name")
    context = {"clients": clients}
    return render(request, "invoice/create.html", context)

def new(request):
    client = get_object_or_404(Client, pk=request.POST["client"])
    due_date = request.POST["due_date"]
    if not due_date:
        due_date = None
    invoice = Invoice.objects.create(
        client=client,
        due_date=due_date,
    )

    # Count how many items have been added
    item_count = 1
    while True:
        try:
            request.POST.__getitem__(f'item-{item_count}-description')
            item_count += 1
        except MultiValueDictKeyError as e:
            break
    for i in range(1, item_count):
        new_item = Item.objects.create(
            invoice=invoice,
            description=request.POST.__getitem__(f'item-{i}-description'),
            hours=request.POST.__getitem__(f'item-{i}-hours'),
            rate=request.POST.__getitem__(f'item-{i}-rate'),
        )
    return HttpResponseRedirect(reverse("invoice:view", args=(invoice.number,)))

def view(request, invoice_number):
    invoice = get_object_or_404(Invoice, number=invoice_number)
    items = get_invoice_items(invoice)
    total = get_invoice_total(items)
    payments = Payment.objects.filter(invoice=invoice)
    paid = sum(payment.amount for payment in payments)
    owed = total - paid
    context = {
        "invoice": invoice,
        "items": items,
        "total": total,
        "payments": payments,
        "paid": paid,
        "owed": owed,
    }
    return render(request, "invoice/view.html", context)

def pdf(request, invoice_number):
    invoice = get_object_or_404(Invoice, number=invoice_number)
    client = invoice.client
    items = get_invoice_items(invoice)
    total = get_invoice_total(items)
    template = Engine.get_default().get_template("invoice/pdf.html")
    context = Context({
        "sender": {
            "name": "Test Ease",
            "addr": {
                "line1": "123 Alphabet Street",
                "line2": "Brouhaha, NJ, 42069",
            },
            "email": "broogle@groogle.com",
        },
        "receiver": {
            "name": client.name,
            "addr": {
                "line1": client.address_line1,
                "line2": client.address_line2,
            },
            "email": client.email,
        },
        "invoiceNumber": invoice.number,
        "createdDate": invoice.created_date.strftime(DATE_FORMAT),
        "dueDate": invoice.due_date.strftime(DATE_FORMAT),
        "total": total,
        "logo": None,
        "items": items,
    })
    html = template.render(context)
    pdf = HTML(string=html).write_pdf()
    return HttpResponse(
        pdf,
        headers={
            "Content-Type": "application/pdf",
            "Content-Disposition": f'attachment; filename="invoice-{invoice.number}.pdf"',
        },
    )
