from django.contrib.staticfiles import finders
from django.shortcuts import render, redirect

from pexels_api import API


# Get file path.
result = finders.find('text_files/pexels_api_key.txt')
f = open(result, 'r')
PEXELS_API_KEY = f.read()
# Create API object
api = API(PEXELS_API_KEY)


def index_page(request):
    """Get popular images on Pexels when user in Home page."""
    # API full response object.
    response_object = api.popular(results_per_page=15, page=1)

    # List of dictionary photos object.
    photos_object = response_object.get('photos')

    # Divide the results by 3, so that, contribute between HTML grid
    # rows equally, depends on the popular(results_per_page) argument
    # integer.
    col_1 = []
    col_2 = []
    col_3 = []
    for count, item in enumerate(photos_object):
        # Append 5 items. Indexing starts from Zero.
        if count <= 4:
            col_1.append(item)
        # Append 6 items.
        elif count > 4 and count <= 10:
            col_2.append(item)
        # Append the rest items.
        else:
            col_3.append(item)

    context = {
        'col_1': col_1,
        'col_2': col_2,
        'col_3': col_3,
    }
    return render(request, 'opening-page.html', context)


def search_results_page(request):
    """Show photos on search query."""
    query = request.POST.get('q')
    if query == '':
        response_object = api.popular(results_per_page=30, page=1)
    else:
        response_object = api.search(query, results_per_page=30, page=1)

    photos_object = response_object.get('photos')

    col_1 = []
    col_2 = []
    col_3 = []
    for count, item in enumerate(photos_object):
        if count <= 9:
            col_1.append(item)
        elif count > 9 and count <= 19:
            col_2.append(item)
        else:
            col_3.append(item)

    context = {
        'col_1': col_1,
        'col_2': col_2,
        'col_3': col_3,
    }
    return render(request, 'opening-page.html', context)
