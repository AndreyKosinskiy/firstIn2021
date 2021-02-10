from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices

# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_publihed=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices,
    }
    print (state_choices)
    return render(request, 'pages/index.html', context=context)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # get MVP
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)[0]

    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context=context)
