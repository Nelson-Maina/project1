from django.shortcuts import get_object_or_ 404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


def index(request):
    # display from the database
    # listings = Listing.objects.all()
    # to order the listing with reference to descending date order
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # adding pagination
    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # generates a 404 error page coz of the missed page
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
