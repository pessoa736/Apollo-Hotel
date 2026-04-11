from django.shortcuts import render, redirect
from .models import Post, Reservation
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'index.html')

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def reservations(request):
    if request.method == 'POST':
        
        name = request.POST.get("name")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        type_of_room = request.POST.get("type_of_room")
        adult = request.POST.get("adult")
        child = request.POST.get("child")
        print(name, check_in, check_out, type_of_room, adult, child)
        reserva = Reservation.objects.create(
            name=name,
            check_in=check_in,
            check_out=check_out,
            type_of_room=type_of_room,
            adult=adult,
            child=child
        )
        reserva.save()

    return redirect('home')
    