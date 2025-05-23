from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        description = request.POST.get('description','')
        Item.objects.create(name=name, description=description)
        return redirect('item_list')  # Or another page/view name
    return render(request, 'create_item.html')  # Show form if GET
def item_list(request):
    items=Item.objects.all()
    return render(request,'item_list.html',{'items':items})
def update_item(request ,id):
    item=get_object_or_404(Item,id=id)
    if request.method=='POST':
        item.name=request.POST['name']
        item.description=request.POST['description']
        item.save()
        return redirect('item_list')
    return render(request,'update_item.html',{'item':item})
def delete_item(request,id):
    item=get_object_or_404(Item,id=id)
    item.delete()
    return redirect('item_list')