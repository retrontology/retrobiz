from .models import Invoice, Client
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    invoices = Invoice.objects.order_by("number")[:10]
    context = {"invoices": invoices}
    return render(request, "invoice/index.html", context)

def create(request):
    clients = Client.objects.order_by("name")
    context = {"clients": clients}
    return render(request, "invoice/create.html", context)

def new(request):
    client = get_object_or_404(Client, pk=request.POST["client"])
    invoice = Invoice.objects.create(
        total=request.POST["total"],
        client=client,
        due_date=request.POST["due_date"],
    )
    return HttpResponseRedirect(reverse("invoice:view", args=(invoice.number,)))

def view(request, invoice_number):
    invoice = get_object_or_404(Invoice, number=invoice_number)
    context = {"invoice": invoice}
    return render(request, "invoice/view.html", context)