from django.shortcuts import render
from .models import Company, get_company
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    try:
        company = get_company()
    except ObjectDoesNotExist as e:
        company = None

    if company:
        context = {
            'company': company
        }
        return render(request, "company/view.html", context)
    else:
        return HttpResponseRedirect(reverse("company:edit"))

def edit(request):
    company = get_company()
    context = {
        'company': company
    }
    return render(request, "company/edit.html", context)

def save(request):
    name=request.POST["name"]
    address_line1=request.POST["address_line1"]
    address_line2=request.POST["address_line2"]
    owner=request.POST["owner"]
    phone=request.POST["phone"]
    email=request.POST["email"]
    company = get_company()
    if company:
        company.name = name
        company.address_line1 = address_line1
        company.address_line2 = address_line2
        company.owner = owner
        company.phone = phone
        company.email = email
        company.save()
    else:
        company = Company.objects.create(
            name=name,
            address_line1=address_line1,
            address_line2=address_line2,
            owner=owner,
            phone=phone,
            email=email,
        )
    return HttpResponseRedirect(reverse("company:index"))
