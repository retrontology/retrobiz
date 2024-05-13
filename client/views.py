from .models import Client
from invoice.utils import *
from invoice.models import Invoice
from payment.models import Payment
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

DEFAULT_MAX=20

def index(request, page_number=1, max_items=DEFAULT_MAX):
    clients = Client.objects.order_by("name")
    if request.GET.get("max"):
        max_items = request.GET.get("max")
    paginator = Paginator(clients, max_items)
    if request.GET.get("page"):
        page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "client/index.html", context)

def create(request):
    return render(request, "client/create.html")

def new(request):
    client = Client.objects.create(
        name=request.POST["name"],
        address_line1=request.POST["address_line1"],
        address_line2=request.POST["address_line2"],
        person_of_contact=request.POST["person_of_contact"],
        phone=request.POST["phone"],
        email=request.POST["email"],
    )
    return HttpResponseRedirect(reverse("client:view", args=(client.id,)))

def view(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    invoices = Invoice.objects.filter(client=client)
    billed = 0
    paid = 0
    for invoice in invoices:
        invoice.total = get_invoice_total(get_invoice_items(invoice))
        billed = billed + invoice.total
        invoice.payments = Payment.objects.filter(invoice=invoice)
        paid = paid + sum(payment.amount for payment in invoice.payments)
    
    owed = billed - paid
    context = {
        "client": client,
        "billed": billed,
        "paid": paid,
        "owed": owed,
        "invoices": invoices,
    }
    return render(request, "client/view.html", context)
