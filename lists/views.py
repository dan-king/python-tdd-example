from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world')

    # items = Item.objects.all()        

    return render(request, 'home.html')

    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    # else:
    #     new_item_text = ''

    # return render(request, 'home.html', {
    #     'new_item_text': new_item_text,
    # })

    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # else:
    #     return render(request, 'home.html')
    # return render(request, 'home.html', {
    #     #'new_item_text': request.POST.get('item_text', ''),
    #     'new_item_text': item.text,
    # })

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world')

def view_list(request):
    items = Item.objects.all()        
    return render(request, 'list.html', {'items': items})

