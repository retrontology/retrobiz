from .models import Client
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    clients = Client.objects.order_by("name")[:10]
    context = {"clients": clients}
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
    context = {"client": client}
    return render(request, "client/view.html", context)