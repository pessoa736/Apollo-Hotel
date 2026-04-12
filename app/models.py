from django.db import models
from django.contrib.auth.models import User
from django_prose_editor.fields import ProseEditorField

# ===== Model da pagina HOME =====
# ================================

# == Model para a section HERO
class Home(models.Model):
    image = models.ImageField(upload_to='home/')
    
    def __str__(self):
        return self.image.url

# == Model para a section Detalhes
class Highlight(models.Model):
    image = models.ImageField(upload_to='highlights/')
    subtitle = models.CharField(max_length=50)
    
    def __str__(self):
        return self.subtitle
    
# == Model para a section Pacotes e Descontos
class Package(models.Model):
    image = models.ImageField(upload_to='packages/')
    
    def __str__(self):
        return self.image.url

class PackageBackground(models.Model):
    image = models.ImageField(upload_to='packages/')
    
    def __str__(self):
        return self.image.url
    
# == Model para a section Galeria
class Gallery(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    
    def __str__(self):
        return self.description

# ===== Model da pagina BLOG =====
# ================================
class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    
    def __str__(self):
        return self.image.url

# ===== Model das postagens do blog =====
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=119)
    created_at = models.DateTimeField(auto_now_add=True)
    user_img = models.ImageField(upload_to='user_img/')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    
    thumbnail = models.ImageField(upload_to='posts/')
    thumb_subtitle = models.CharField(max_length=50)
    image = models.ImageField(upload_to='posts/')
    img_subtitle = models.CharField(max_length=50)
    
    body = ProseEditorField(sanitize=True,
        extensions={
            # Core text formatting
            "Bold": True,
            "Italic": True,
            "Strike": True,
            "Underline": True,
            "HardBreak": True,

            # Structure
            "Heading": {
                "levels": [1, 2, 3, 4]  # Only allow h1, h2, h3
            },
            "BulletList": True,
            "OrderedList": True,
            "ListItem": True, # Used by BulletList and OrderedList
            "Blockquote": True,

            # Advanced extensions
            "Link": {
                "enableTarget": True,  # Enable "open in new window"
                "protocols": ["http", "https", "mailto"],  # Limit protocols
            },
            "Table": True,
            "TableRow": True,
            "TableHeader": True,
            "TableCell": True,

            # Editor capabilities
            "History": True,       # Enables undo/redo
            "HTML": True,          # Allows HTML view
            "Typographic": True,   # Enables typographic chars
        }
    )
    
    class Meta:
        ordering = ['-created_at']  
    
    def __str__(self):
        return self.title
    

# ===== Reservas de quartos =====
    
class Reservation(models.Model):
    type_of_room_choices = [
        ('casal', 'Casal'),
        ('solteiro', 'Solteiro'),
        ('Suite Princes', 'Suite Princes'),
        ('suite', 'Suite'),
    ]
    
    name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    type_of_room = models.CharField(max_length=20, choices=type_of_room_choices)
    adult = models.IntegerField(default=0)      
    child = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

# ====== Model da pagina SOBRE =====
# ==================================
class History(models.Model):
    image = models.ImageField(upload_to='history/')
    
    def __str__(self):
        return self.image.url
    
class Mission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.title

class Equipe(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    
    def __str__(self):
        return self.name
    
class Services(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')
        
    def __str__(self):
        return self.title