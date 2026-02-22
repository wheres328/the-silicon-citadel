"""
=========================================
MODELOS DEL PROYECTO - THE SILICON CITADEL
=========================================

Este archivo define todas las entidades de la base de datos.

Modelos principales:
- Profile: Perfil de usuario con roles y niveles de acceso
- NewsItem: Noticias/actualizaciones del sitio
- BlogPost: Artículos/blogs
- Comment: Comentarios en noticias y blogs
- Bookmark: Marcadores de usuarios
- Report: Reportes de contenido
- Ban: Baneos de usuarios

Relaciones importantes:
- User (Django) → Profile (uno a uno)
- NewsItem/BlogPost → Comment (uno a muchos)
- User → Bookmark (muchos a muchos)
- User → Report (muchos a muchos)
"""

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ROLE_CHOICES = [
        # Miembro normal
        ('member', 'Miembro'),
        # Staff - Moderación
        ('vigilante', '👁️ Vigilante del Portón'),      # Moderador - borrar comentarios, suspender
        ('guardian', '🛡️ Guardian de la Muralla'),    # Admin de mods - ban permanente, reportes
        ('capitan', '🔨 Capitán del Martillo'),       # Super Mod - supervisar mods, normas
        # Staff - Administración
        ('ancianos', '📜 Consejo de Ancianos'),       # Decisiones estratégicas
        ('rey', '👑 Rey bajo la Montaña'),           # Control total
    ]
    
    ROLE_LEVELS = {
        'member': 0,
        'vigilante': 1,
        'guardian': 2,
        'capitan': 3,
        'ancianos': 4,
        'rey': 5,
    }
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_vip = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    is_staff_member = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def get_role_level(self):
        return self.ROLE_LEVELS.get(self.role, 0)
    
    def can_edit(self):
        return self.role in ['vigilante', 'guardian', 'capitan', 'ancianos', 'rey'] or self.user.is_staff
    
    def can_delete(self):
        return self.role in ['guardian', 'capitan', 'ancianos', 'rey'] or self.user.is_staff
    
    def can_moderate(self):
        return self.role in ['vigilante', 'guardian', 'capitan', 'ancianos', 'rey'] or self.user.is_staff
    
    def can_ban(self):
        return self.role in ['guardian', 'capitan', 'ancianos', 'rey'] or self.user.is_staff
    
    def can_manage_staff(self):
        return self.role in ['capitan', 'ancianos', 'rey'] or self.user.is_staff
    
    def can_change_rules(self):
        return self.role in ['capitan', 'ancianos', 'rey'] or self.user.is_staff
    
    def can_full_admin(self):
        return self.role in ['ancianos', 'rey'] or self.user.is_staff
    
    def can_super_admin(self):
        return self.role == 'rey' or self.user.is_superuser


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not hasattr(instance, "profile"):
        Profile.objects.create(user=instance)
    instance.profile.save()


class NewsItem(models.Model):
    CATEGORY_CHOICES = [
        ("General", "General"),
        ("Laptops & Portátiles", "Laptops & Portátiles"),
        ("Tablets & iPads", "Tablets & iPads"),
        ("Consolas de Forja", "Consolas de Forja"),
        ("PC Desktop", "PC Desktop"),
        ("Componentes Core", "Componentes Core"),
        ("Periféricos & Accesorios", "Periféricos & Accesorios"),
        ("Taller de Reparación", "Taller de Reparación"),
        ("Redes & Enlaces", "Redes & Enlaces"),
        ("Alquimia de Software", "Alquimia de Software"),
        ("Artefactos & Gadgets", "Artefactos & Gadgets"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300, null=True, blank=True, help_text="Descripción corta para la lista de actualizaciones (máx 300 caracteres)")
    description = models.TextField()
    image = models.ImageField(upload_to="news_thumbs/", null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True, help_text="URL de imagen externa (ej: desde Google Images, Imgur, etc.)")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="General")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_description(self):
        return self.short_description if self.short_description else self.description

    @property
    def get_image(self):
        return self.image.url if self.image else self.image_url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Última actualización"
        verbose_name_plural = "Últimas actualizaciones"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, default="Admin")
    short_description = models.CharField(max_length=300, null=True, blank=True, help_text="Descripción corta para listas (máx 300 caracteres)")
    content = models.TextField()
    image = models.ImageField(upload_to="blog_thumbs/", null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True, help_text="URL de imagen externa")
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_image(self):
        return self.image.url if self.image else self.image_url

    @property
    def get_description(self):
        return self.short_description if self.short_description else self.content

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Entrada de Blog"
        verbose_name_plural = "Entradas de Blog"


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    news_item = models.ForeignKey(
        NewsItem, on_delete=models.CASCADE, null=True, blank=True
    )
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        item = self.news_item.title if self.news_item else self.blog_post.title
        return f"Marcador de {self.user.username} para {item}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    news_item = models.ForeignKey(
        NewsItem,
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
        blank=True,
    )
    blog_post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
        blank=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        target = self.news_item.title if self.news_item else self.blog_post.title
        return f"Comentario de {self.user.username} en {target}"

    class Meta:
        ordering = ["-created_at"]


class Report(models.Model):
    REPORT_TYPES = [
        ('spam', 'Spam'),
        ('inappropriate', 'Inapropiado'),
        ('harassment', 'Acoso'),
        ('fake', 'Falso/Engaño'),
        ('other', 'Otro'),
    ]
    
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_made')
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_received', null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES, default='other')
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pendiente'),
        ('reviewed', 'Revisado'),
        ('resolved', 'Resuelto'),
        ('dismissed', 'Descartado'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reports_resolved')
    resolution_notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Reporte de {self.reporter.username} - {self.get_report_type_display()}"


class Ban(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bans')
    banned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='bans_given')
    reason = models.TextField()
    ban_type = models.CharField(max_length=20, choices=[
        ('temporary', 'Temporal'),
        ('permanent', 'Permanente'),
    ], default='permanent')
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Ban para {self.user.username} - {self.get_ban_type_display()}"
    
    def is_expired(self):
        if self.ban_type == 'permanent':
            return False
        if self.expires_at and self.expires_at < timezone.now():
            self.is_active = False
            self.save()
            return True
        return False


class Portfolio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="portfolio/", null=True, blank=True)
    url = models.URLField(blank=True)
    categoria = models.CharField(max_length=50, choices=[
        ('web', 'Sitio Web'),
        ('tienda', 'Tienda Online'),
        ('app', 'Aplicación'),
        ('otro', 'Otro'),
    ], default='web')
    cliente = models.CharField(max_length=100, blank=True)
    completado = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    orden = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-orden', '-created_at']


class Testimonial(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, blank=True)
    mensaje = models.TextField()
    foto = models.ImageField(upload_to="testimonials/", null=True, blank=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Testimonio de {self.nombre}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
