from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Category, Product, About, CarouselImage
from .forms import ContactForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    carousel_images = CarouselImage.objects.all()
    return render(request, 'index.html', {'categories': categories, 'carousel_images': carousel_images})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})

def about(request):
    about_content = About.objects.first()
    if not about_content:
        about_content = About.objects.create(content="Default content")
        return redirect('')
    return render(request, 'about_us.html', {'about_content': about_content})


# Add this function to main/views.py
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Contact Us Message from {name}',
                message,
                email,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})