from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


def index(request):
    # show all tv shows in table
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)


def create_form(request):
    # show a form to create a show
    return render(request, 'create.html')


def create_show(request):
    # create an instance of the Show class
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/create')
    else:
        if request.method == "POST":
            
            show_title = request.POST.get('show_title', False)
            show_network = request.POST.get('show_network', False)
            show_description = request.POST.get('show_description', False)

            print(request.POST)
            Show.objects.create(title=request.POST['show_title'], network=request.POST['show_network'],
                            release_date=request.POST['show_release_date'], description=request.POST['show_description'])
            print(Show.objects.get(id=1))
        return redirect('/shows')


def show_show(request, show_id):
    # show one instance of a show on a template
    context = {
        "a_show": Show.objects.get(id=show_id)
    }
    return render(request, 'a_show.html', context)


def delete_show(request, show_id):
    # delete a show from database
    if request.method == "POST":
        show_to_delete = Show.objects.get(id=show_id)
        show_to_delete.delete()
    return redirect('/shows')


def edit_show(request, show_id):
    # show a form to edit a show instance
    context = {
        'a_show': Show.objects.get(id=show_id)
    }
    # date= Show.objects.get(id=show_id).release_date
    return render(request, "edit_show.html", context)


def update_show(request, show_id):
    # update the single show in the database and save
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        if request.method == "POST":

            show_title = request.POST.get('show_title', False)
            show_network = request.POST.get('show_network', False)
            show_description = request.POST.get('show_description', False)

            show_to_update = Show.objects.get(id=show_id)
            show_to_update.title = request.POST['show_title']
            show_to_update.network = request.POST['show_network']
            show_to_update.release_date = request.POST['show_release_date']
            show_to_update.description = request.POST['show_description']
            show_to_update.save()
        return redirect(f'/shows/{show_id}')
