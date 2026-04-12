from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# ===== Views da pagina HOME =====
# ================================
def home(request):
    home = Home.objects.first()
    highlights = Highlight.objects.all()
    packages = Package.objects.all()
    package_bg = PackageBackground.objects.first()
    gallery = Gallery.objects.all()
    return render(request, 'index.html', {'highlights': highlights, 'gallery': gallery, 'home': home, 'packages': packages, 'package_bg': package_bg})

# ===== Views da pagina BLOG =====
# ================================
def blog(request):
    blog = Blog.objects.first()
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'blog': blog})

def details(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'details.html', {'post' : post})


# ===== Views da pagina SOBRE =====
# ================================
def about(request):
    history = History.objects.all()
    mission = Mission.objects.all()
    equipe = Equipe.objects.all()
    services = Services.objects.all()
    return render(request, 'about.html', {'history': history, 'mission': mission, 'equipes': equipe, 'services': services})



# ==== Views da pagina RESERVAS =====
# ===============================
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
    