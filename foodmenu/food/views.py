from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
# def items(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/items.html')
#     context = {
#         'item_list':item_list,
#     }
#     return render(request, "food/items.html", context=context)

def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        "item":item,
    }
    return render(request, 'food/details.html', context=context)

def add_items(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:item')
    return render(request, 'food/item_form.html', {'form':form})

class AddItemView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']

    def form_valid(self, form):
        form.instance.username = self.request.user

        return super().form_valid(form)
    
    template_name = 'food/item_form.html'


def update_items(request, item_id):
    item = Item.objects.get(id = item_id)

    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:item')
    return render(request, 'food/item_form.html', {'form':form})

def delete_items(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:item')
    return render(request, 'food/item_delete.html', {'item':item})

class ItemClassView(ListView):
    model = Item
    template_name = 'food/items.html'
    context_object_name = 'item_list'

class ItemDetails(DetailView):
    model = Item
    template_name = 'food/details.html'
