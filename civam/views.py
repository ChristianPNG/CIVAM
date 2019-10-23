from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from .models import *
from guardian.shortcuts import assign_perm, get_perms, remove_perm, get_perms_for_model
from .forms import *


# Create your views here.
def index(request):
    return HttpResponse("index")

def collection_list(request):
    collection_list = Collection.objects.all()
    print(collection_list)
    context = {'collection_list' : collection_list}
    return render(request, 'civam/collection_list.html' ,context)

def item(request, collection_id, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if(request.method == 'POST'):
        form = StoryForm(request.POST)
        if form.is_valid():
            story_instance = form.save(commit=False)
            story_instance.item = item 
            story_instance.created_by = request.user
            story_instance.save()
            return redirect("")

    stories = Story.objects.filter(item_id=item_id)
    image = Image.objects.get(item_id=item_id)
    form = StoryForm()
    if not request.user.has_perm("civam.view_item",item):
        #add edit and delete options in template
        context = {'item': item, 'stories': stories, 'form': form, 'image': image}
        return render(request, 'civam/item.html', context)
    else:
        return HttpResponse(str(request.user)+" cannot view this item")

def new_item(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    if(request.method== 'POST'):
        item_form = ItemForm(request.POST, prefix='item')
        image_form = ImageForm(request.POST, prefix='image')
        video_form = VideoForm(request.POST, prefix='video')
    
        if item_form.is_valid():
            item_instance = item_form.save(commit=False)
            item_instance.collection = collection
            item_instance.save()
            if image_form.is_valid():
                content = image_form.cleaned_data['content']
                image_instance = Image(item=item_instance,content=content)
                image_instance.save()
            if video_form.is_valid():
                link = video_form.cleaned_data['link']
                video_instance = Video(link=link, item=item_instance)
                video_instance.save()
            return redirect("collections/{0}".format(collection_id))
    #regular GET
    item_form = ItemForm(prefix = 'item')
    image_form = ImageForm(prefix = 'image')
    video_form = VideoForm(prefix = 'video')
    context = {'item_form': item_form, 'image_form': image_form, 'video_form': video_form, 'collection': collection}
    return render(request, 'civam/new_item.html', context)

    

def collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    if not request.user.has_perm("civam.view_collection",collection):
        item_list = Item.objects.filter(collection=collection)
        context = {'item_list': item_list, 'collection': collection}
        #add edit and delete options in template
        return render(request, 'civam/collection.html', context)
    else:
        return HttpResponse(str(request.user)+" cannot view this collection")

def grant_perm(request, obj_type, obj, permi):
    if not obj:
        return HttpResponse("Select an object to give permissions to")
    elif obj_type.casefold() == "item":
        item = Item.objects.get(name__iexact=obj)
    elif obj_type.casefold() == "collection":
        item = Collection.objects.get(title__iexact=obj)
    else:
        return HttpResponse("Select an object type of the object")

    if not permi:
        return HttpResponse("No permission to grant")
    elif request.user.has_perm("civam."+permi, item):
        return HttpResponse("Permission *"+obj_type.capitalize()+" "+str(permi)+"* already granted")
    else:
        assign_perm("civam."+permi, request.user, item)
        return HttpResponse("Permission *"+obj_type.capitalize()+" "+str(permi)+"* granted")
      
def revoke_perm(request, obj_type, obj, permi):
    if not obj:
        return HttpResponse("Select an object to revoke permissions of")
    elif obj_type.casefold() == "item":
        item = Item.objects.get(name__iexact=obj)
    elif obj_type.casefold() == "collection":
        item = Collection.objects.get(title__iexact=obj)
    else:
        return HttpResponse("Select an object type of the object")

    if not permi:
        return HttpResponse("No permission to revoke")
    elif not request.user.has_perm("civam."+permi,item):
        return HttpResponse("Permission *"+obj_type.capitalize()+" "+str(permi)+"* already revoked")
    else:
        remove_perm(permi, request.user, item)
        return HttpResponse("Permission *"+obj_type.capitalize()+" "+str(permi)+"* revoked")

