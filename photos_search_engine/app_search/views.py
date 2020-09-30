from django.contrib.staticfiles import finders
from django.shortcuts import render

from pexels_api import API


# Get file path.
file = finders.find('text_files/pexels_api_key.txt')
f = open(file, 'r')
PEXELS_API_KEY = f.read()
# Create API object
api = API(PEXELS_API_KEY)


def search_results_page(request):
    """Show popular or search results

    Show photos when the user type keyword show related results,
    and when user visiting Home page show popular Pexels photos.
    """

    if request.method == 'POST':
        # When user submit keyword within the search input.
        keyword = request.POST.get('k')
    # On opening page, assign keyword with string to avoid error
    # within next if condition.
    else:
        keyword = ''

    # On empty keyword, or visiting Home page.
    if keyword.replace(' ', '') == '' or request.method == 'GET':
        response_object = api.popular(results_per_page=78)
    else:
        # On search keyword
        response_object = api.search(keyword, results_per_page=78)

    # Get list of photos dictionary object.
    photos_object = response_object.get('photos')

    # Divide the results by 3, so that, contribute the 78 items
    # between HTML grid rows equally, depends on the
    # popular(results_per_page) argument value(integer).
    # Each column corresponding to column of mites within the HTML.
    col_1 = []
    col_2 = []
    col_3 = []
    for count, item in enumerate(photos_object):
        # Append 9 items. Indexing starts from Zero.
        if count <= 25:
            col_1.append(item)
        # Append 10 items.
        elif count > 25 and count <= 51:
            col_2.append(item)
        # Append the rest items.
        else:
            col_3.append(item)

    context = {
        'col_1': col_1,
        'col_2': col_2,
        'col_3': col_3,
        # These two keys, used when there is unmatched results.
        'total_results': response_object.get('total_results'),
        'keyword': keyword,
    }
    return render(request, 'photos-results.html', context)
