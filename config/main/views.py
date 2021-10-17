from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from .forms import AddRestaurantForm


def index(request):
    search_query = request.POST.get('search_query')
    if request.method == 'POST' and not search_query:
        current_id = request.POST.get('id', None)
        contact = get_object_or_404(pk=current_id, klass=Restaurant)
        contact.delete()
        restaurant_list = Restaurant.objects.all()
    elif request.method == 'POST' and search_query:
        restaurant_list = Restaurant.objects.filter(special__contains=search_query)
    else:
        restaurant_list = Restaurant.objects.all()

    return render(request, 'index.html', {'restaurant_list': restaurant_list})


def add_restaurant_record(request):
    if request.method == "GET":
        form = AddRestaurantForm()
    else:
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add_restaurant.html', {'form': form})


def update_item(request, contact_id):
    if request.method == "GET":
        contact = get_object_or_404(pk=int(contact_id), klass=Restaurant)
        form = AddRestaurantForm(instance=contact)
    else:
        form = AddRestaurantForm(request.POST)
        body = {**request.POST}
        del body['csrfmiddlewaretoken']
        del body['id']
        for key in body:
            body[key] = body[key][0]
        print(body)
        obj,created = Restaurant.objects.update_or_create(pk=int(request.POST.get('id')), defaults={**body})
        print(obj, created)
        # contact = get_object_or_404(pk=int(contact_id), klass=Restaurant)
        # contact.name = request.POST.get('name')
        # contact.address = request.POST.get('address')
        # contact.special = request.POST.get('special')
        # contact.phone_number = request.POST.get('phone_number')
        # contact.save()
        return redirect('/')
    return render(request, 'update_item.html', {'form': form, 'contact_id':contact_id})
