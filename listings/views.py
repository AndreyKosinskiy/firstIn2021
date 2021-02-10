from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_publihed=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context=context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context=context)


def search(request):
    context = {
        #'listings': listings,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices,
    }
    return render(request, 'listings/search.html',context=context)
