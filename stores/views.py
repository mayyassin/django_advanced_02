from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def create(request):
	store = StoreModelForm()
	if request.method == "POST":
		store = StoreModelForm(request.POST, request.FILES)
		if store.is_valid():
			store.save()
			return redirect('list')
	context = {
	"store": store,
	}
	return render(request, 'create.html', context)

def store_detail(request, slug_name):
	context = {
		"store": Store.objects.get(slug=slug_name)
	}
	return render(request, 'store_detail.html', context)



