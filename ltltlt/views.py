from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Item, Price
from price_updater import scraper

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'index.html'
    model = Item
    def get_queryset(self):
        """Return the last five published questions."""
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'item_detail.html'
    model = Item
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        prices = Item.objects.get(id=self.kwargs['pk']).price_set.all().values()
        context['prices'] = list(prices)
        return context

def getPrices(request, pk):
    prices = Item.objects.get(id=pk).price_set.all().values()
    return JsonResponse(list(prices), safe=False)

class ItemCreate(LoginRequiredMixin, generic.CreateView):
    model = Item
    fields = ['item_number']

class ItemDelete(LoginRequiredMixin, generic.DeleteView):
    model = Item
    success_url = reverse_lazy('ltltlt:index')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def handleCreate(request):
    print(request)
    name = 'placeholder'
    number = request.POST['item_number']
    name, img, price = scraper.getItemNameChrome(number)
    user = request.user
    item = Item(item_number=number, user=user, item_name=name, img_url=img)
    item.save()
    item.price_set.create(price=price)
    return HttpResponseRedirect(reverse('ltltlt:index'))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ltltlt:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

