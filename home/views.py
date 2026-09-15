from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def dine_in(request):
    return render(request, 'dine_in.html')

def delivery(request):
    return render(request, 'delivery.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    query = request.GET.get('q', '').strip()

    # Static pages available for search — extend this as you add more pages/models
    pages = [
        {
            'title': 'Home',
            'url_name': 'home',
            'description': 'Welcome to My Restaurant — delicious food, great atmosphere.',
            'keywords': ['home', 'welcome', 'main', 'restaurant'],
        },
        {
            'title': 'About',
            'url_name': 'about',
            'description': 'Learn more about My Restaurant.',
            'keywords': ['about', 'story', 'who we are', 'history'],
        },
        {
            'title': 'Services',
            'url_name': 'services',
            'description': 'Explore the services we offer.',
            'keywords': ['services', 'offerings', 'menu'],
        },
        {
            'title': 'Dine In',
            'url_name': 'dine_in',
            'description': 'Enjoy a dine-in experience at our restaurant.',
            'keywords': ['dine in', 'dine-in', 'eat here', 'restaurant seating', 'table'],
        },
        {
            'title': 'Delivery',
            'url_name': 'delivery',
            'description': 'Get your favorite meals delivered to your door.',
            'keywords': ['delivery', 'order', 'food delivery', 'takeout'],
        },
        {
            'title': 'Contact',
            'url_name': 'contact',
            'description': 'Get in touch with us.',
            'keywords': ['contact', 'reach us', 'phone', 'email', 'address'],
        },
    ]

    results = []
    if query:
        q_lower = query.lower()
        for page in pages:
            haystack = ' '.join([page['title'], page['description']] + page['keywords']).lower()
            if q_lower in haystack:
                results.append(page)

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)