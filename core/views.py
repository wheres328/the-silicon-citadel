"""
=========================================
VISTAS DEL PROYECTO - THE SILICON CITADEL
=========================================

Este archivo contiene todas las funciones de vista (views) del proyecto.
Cada función maneja una página específica del sitio.

Estructura general:
- Vistas públicas: index, actualizaciones, blogs, categorías, detalles
- Vistas de autenticación: login, logout, register
- Vistas de usuario: profile, my_news, my_blogs
- Vistas de moderación: mod_panel, reports, bans
- Vistas de acciones: create, edit, delete, toggle_bookmark, comments

Para agregar una nueva página:
1. Crear la función en views.py
2. Agregar la URL en urls.py
3. Crear el template en templates/
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsItem, BlogPost, Bookmark, Comment, Report, Ban, Profile
from django.db.models import Q, Count
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import NewsItemForm, BlogPostForm


# =========================================
# VISTAS PÚBLICAS - PÁGINAS PRINCIPALES
# =========================================

def index(request):
    """
    Página principal (Home)
    Muestra las últimas noticias (hasta 10) y blogs (hasta 7)
    """
    news_items = NewsItem.objects.all().order_by("-created_at")[:10]
    blog_posts = BlogPost.objects.all().order_by("-date")[:7]

    stats = {
        "books": "35,432,102",
        "papers": "98,123,556",
        "comics": "2,451,000",
        "magazines": "1,102,000",
    }

    context = {
        "news_items": news_items,
        "blog_posts": blog_posts,
        "stats": stats,
    }
    return render(request, "index.html", context)


def actualizaciones(request):
    """
    Página de listado de noticias/actualizaciones
    Usa paginación (10 por página)
    """
    from django.core.paginator import Paginator
    
    news_list = NewsItem.objects.all().order_by("-created_at")
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get("page")
    news_page = paginator.get_page(page_number)
    
    return render(request, "actualizaciones.html", {
        "news": news_page,
        "page_obj": news_page,
    })


def blogs(request):
    """
    Página de listado de todos los artículos/blogs
    Usa paginación (10 por página)
    """
    from django.core.paginator import Paginator
    
    blog_list = BlogPost.objects.all().order_by("-date")
    paginator = Paginator(blog_list, 10)
    page_number = request.GET.get("page")
    blog_page = paginator.get_page(page_number)
    
    return render(request, "blogs.html", {
        "blogs": blog_page,
        "page_obj": blog_page,
    })


def news_detail(request, slug):
    """
    Página de detalle de una noticia
    Muestra contenido completo, comentarios, opciones de bookmark
    """
    item = get_object_or_404(NewsItem, slug=slug)
    user_bookmarks = []
    can_edit = False
    can_delete = False
    
    if request.user.is_authenticated:
        user_bookmarks = list(
            Bookmark.objects.filter(
                user=request.user, news_item__isnull=False
            ).values_list("news_item_id", flat=True)
        )
        can_edit = request.user.is_staff or (hasattr(request.user, 'profile') and request.user.profile.can_edit())
        can_delete = request.user.is_staff or (hasattr(request.user, 'profile') and request.user.profile.can_delete())
    
    comments = item.comments.all().select_related("user")
    return render(
        request,
        "news_detail.html",
        {"item": item, "user_bookmarks": user_bookmarks, "comments": comments, "can_edit": can_edit, "can_delete": can_delete},
    )


def blog_detail(request, slug):
    """
    Página de detalle de un artículo/blog
    Muestra contenido completo, comentarios, opciones de bookmark
    """
    post = get_object_or_404(BlogPost, slug=slug)
    user_bookmarks = []
    can_edit = False
    can_delete = False
    
    if request.user.is_authenticated:
        user_bookmarks = list(
            Bookmark.objects.filter(
                user=request.user, blog_post__isnull=False
            ).values_list("blog_post_id", flat=True)
        )
        can_edit = request.user.is_staff or (hasattr(request.user, 'profile') and request.user.profile.can_edit())
        can_delete = request.user.is_staff or (hasattr(request.user, 'profile') and request.user.profile.can_delete())
    
    comments = post.comments.all().select_related("user")
    return render(
        request,
        "blog_detail.html",
        {"post": post, "user_bookmarks": user_bookmarks, "comments": comments, "can_edit": can_edit, "can_delete": can_delete},
    )


def vault(request):
    # This will be the new "Library" or "Vault" page
    query = request.GET.get("q", "")
    if query:
        # In a real app, we would search across books/papers models
        # For now, let's keep it as a results page
        return render(request, "vault.html", {"query": query, "is_search": True})
    return render(request, "vault.html", {"is_search": False})


def connect(request):
    # This will be the "Donate" / "Community" page
    return render(request, "connect.html")


def search_results(request):
    query = request.GET.get("q", "")
    # Basic search across news and blog for now
    news_results = (
        NewsItem.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        if query
        else []
    )
    blog_results = (
        BlogPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        if query
        else []
    )

    context = {
        "query": query,
        "news_results": news_results,
        "blog_results": blog_results,
    }
    return render(request, "search_results.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Bienvenido de nuevo, {username}!")
                return redirect("index")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect("index")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Cuenta creada con éxito. ¡Bienvenido a Forge & Chip!"
            )
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def is_staff(user):
    return user.is_staff


@login_required
def profile_view(request):
    # Crear perfil si no existe
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user, role='member')
    
    bookmarks = Bookmark.objects.filter(user=request.user).order_by("-created_at")
    recent_comments = Comment.objects.filter(user=request.user).order_by("-created_at")[:10]
    
    news_count = NewsItem.objects.filter().count()
    blogs_count = BlogPost.objects.filter().count()
    
    return render(
        request,
        "profile_new.html",
        {
            "bookmarks": bookmarks,
            "bookmarks_count": bookmarks.count(),
            "comments_count": recent_comments.count(),
            "news_count": news_count,
            "blogs_count": blogs_count,
            "recent_comments": recent_comments,
        },
    )


@login_required
@user_passes_test(is_staff)
def my_news_view(request):
    news_items = NewsItem.objects.all().order_by("-created_at")
    return render(request, "my_content.html", {
        "news_items": news_items,
        "content_type": "news",
        "page_title": "Mis Actualizaciones"
    })


@login_required
@user_passes_test(is_staff)
def my_blogs_view(request):
    blog_posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "my_content.html", {
        "blog_posts": blog_posts,
        "content_type": "blog",
        "page_title": "Mis Artículos"
    })


@login_required
@user_passes_test(is_staff)
def delete_news(request, news_id):
    news_item = get_object_or_404(NewsItem, id=news_id)
    news_item.delete()
    messages.success(request, "Actualización eliminada correctamente.")
    return redirect("my_news")


@login_required
@user_passes_test(is_staff)
def delete_blog(request, blog_id):
    blog_post = get_object_or_404(BlogPost, id=blog_id)
    blog_post.delete()
    messages.success(request, "Artículo eliminado correctamente.")
    return redirect("my_blogs")


def can_edit(user):
    if not user.is_authenticated:
        return False
    if not hasattr(user, 'profile'):
        return False
    return user.profile.can_edit()

def can_delete(user):
    if not user.is_authenticated:
        return False
    if not hasattr(user, 'profile'):
        return False
    return user.profile.can_delete()


@login_required
def edit_news(request, news_id):
    news_item = get_object_or_404(NewsItem, id=news_id)
    
    if not can_edit(request.user):
        messages.error(request, "No tienes permisos para editar.")
        return redirect("index")
    
    if request.method == "POST":
        form = NewsItemForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Actualización editada con éxito!")
            return redirect("my_news")
    else:
        form = NewsItemForm(instance=news_item)
    
    return render(request, "edit_content.html", {
        "form": form,
        "item": news_item,
        "content_type": "news",
        "page_title": "Editar Actualización"
    })


@login_required
def edit_blog(request, blog_id):
    blog_post = get_object_or_404(BlogPost, id=blog_id)
    
    if not can_edit(request.user):
        messages.error(request, "No tienes permisos para editar.")
        return redirect("index")
    
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Artículo editado con éxito!")
            return redirect("my_blogs")
    else:
        form = BlogPostForm(instance=blog_post)
    
    return render(request, "edit_content.html", {
        "form": form,
        "item": blog_post,
        "content_type": "blog",
        "page_title": "Editar Artículo"
    })


@login_required
def delete_news_public(request, news_id):
    if not can_delete(request.user):
        messages.error(request, "No tienes permisos para eliminar.")
        return redirect("index")
    
    news_item = get_object_or_404(NewsItem, id=news_id)
    news_item.delete()
    messages.success(request, "Actualización eliminada correctamente.")
    return redirect("my_news")


@login_required
def delete_blog_public(request, blog_id):
    if not can_delete(request.user):
        messages.error(request, "No tienes permisos para eliminar.")
        return redirect("index")
    
    blog_post = get_object_or_404(BlogPost, id=blog_id)
    blog_post.delete()
    messages.success(request, "Artículo eliminado correctamente.")
    return redirect("my_blogs")


@login_required
def toggle_bookmark(request):
    """Toggle a bookmark for a news item or blog post."""
    if request.method == "POST":
        item_type = request.POST.get("item_type")
        item_id = request.POST.get("item_id")

        if item_type == "news":
            item = get_object_or_404(NewsItem, id=item_id)
            bookmark, created = Bookmark.objects.get_or_create(
                user=request.user, news_item=item
            )
        elif item_type == "blog":
            item = get_object_or_404(BlogPost, id=item_id)
            bookmark, created = Bookmark.objects.get_or_create(
                user=request.user, blog_post=item
            )
        else:
            return redirect("index")

        if not created:
            bookmark.delete()
            messages.info(request, "Eliminado de tus anales personales.")
        else:
            messages.success(request, "Guardado en tus anales de la ciudadela.")

        # Redirect back to where we came from
        return redirect(request.META.get("HTTP_REFERER", "index"))
    return redirect("index")


@user_passes_test(is_staff)
def create_news(request):
    if request.method == "POST":
        form = NewsItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Noticia publicada con éxito!")
            return redirect("profile")
    return redirect("profile")


@user_passes_test(is_staff)
def create_blog(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Entrada de blog publicada con éxito!")
            return redirect("profile")
    return redirect("profile")


def donate(request):
    return render(request, "donate.html")


@login_required
def upgrade_vip(request):
    if request.method == "POST":
        profile = request.user.profile
        profile.is_vip = True
        profile.save()
        messages.success(
            request, "¡Felicidades! Ahora eres un miembro VIP de Forge & Chip."
        )
        return redirect("profile")
    return render(request, "upgrade_vip.html")


def tribute(request):
    """View for the Dwarf Fortress tribute page."""
    return render(request, "tribute.html")


def error_404(request, exception):
    """Custom 404 Error Page."""
    return render(request, "404.html", status=404)


def guild_application(request):
    """View for the Guild of Technicians application page."""
    return render(request, "guild_application.html")


@login_required
def add_comment(request):
    """Handle comment submission via POST."""
    if request.method == "POST":
        item_type = request.POST.get("item_type")
        item_id = request.POST.get("item_id")
        content = request.POST.get("content")

        if not content:
            messages.error(request, "El mensaje no puede estar vacío.")
            return redirect(request.META.get("HTTP_REFERER", "index"))

        if item_type == "news":
            item = get_object_or_404(NewsItem, id=item_id)
            Comment.objects.create(user=request.user, news_item=item, content=content)
        elif item_type == "blog":
            post = get_object_or_404(BlogPost, id=item_id)
            Comment.objects.create(user=request.user, blog_post=post, content=content)
        else:
            return redirect("index")

        messages.success(request, "Tu sabiduría ha sido grabada en los anales.")
        return redirect(request.META.get("HTTP_REFERER", "index"))
    return redirect("index")


def categories_view(request):
    """View for the categories gallery page."""
    from django.db.models import Count
    
    category_data = {
        "General": {"icon": "📦", "desc": "Noticias y actualizaciones generales.", "color": "amber"},
        "Laptops & Portátiles": {"icon": "💻", "desc": "Estaciones de trabajo móviles, Ultrabooks y Gaming laptops de alta gama.", "color": "amber"},
        "Tablets & iPads": {"icon": "📱", "desc": "Dispositivos táctiles para diseño, consumo de medios y movilidad total.", "color": "blue"},
        "Consolas de Forja": {"icon": "🎮", "desc": "Sistemas de entretenimiento: PS5, Xbox Series, Switch y retro-emulación.", "color": "purple"},
        "PC Desktop": {"icon": "🖥️", "desc": "Torres personalizadas, estaciones de minería y setups profesionales.", "color": "emerald"},
        "Componentes Core": {"icon": "⚙️", "desc": "Procesadores (CPU), Gráficas (GPU), RAM y almacenamiento masivo.", "color": "red"},
        "Periféricos & Accesorios": {"icon": "⌨️", "desc": "Teclados mecánicos, ratones de precisión y audio de alta fidelidad.", "color": "cyan"},
        "Taller de Reparación": {"icon": "🔧", "desc": "Servicios técnicos: Reballing, cambio de pantallas y aligerado de carga.", "color": "orange"},
        "Redes & Enlaces": {"icon": "📡", "desc": "Routers, switches, antenas y conectividad de largo alcance.", "color": "indigo"},
        "Alquimia de Software": {"icon": "💾", "desc": "Sistemas operativos, firmwares personalizados y herramientas de diagnóstico.", "color": "fuchsia"},
        "Artefactos & Gadgets": {"icon": "⌚", "desc": "Smartwatches, tecnología wearable y gadgets experimentales.", "color": "rose"},
    }
    
    category_counts = dict(NewsItem.objects.values('category').annotate(count=Count('id')).values_list('category', 'count'))
    
    categories = []
    for cat_name, cat_info in category_data.items():
        categories.append({
            "id": cat_name,
            "title": cat_name,
            "icon": cat_info["icon"],
            "desc": cat_info["desc"],
            "count": category_counts.get(cat_name, 0),
            "color": cat_info["color"],
        })
    
    return render(request, "categories.html", {"categories": categories})


def category_detail(request, category_name):
    from django.core.paginator import Paginator
    
    news_items = NewsItem.objects.filter(category=category_name).order_by("-created_at")
    paginator = Paginator(news_items, 12)
    page_number = request.GET.get("page")
    news_page = paginator.get_page(page_number)
    
    category_info = {
        "General": {"icon": "📦", "desc": "Noticias y actualizaciones generales.", "color": "amber"},
        "Laptops & Portátiles": {"icon": "💻", "desc": "Estaciones de trabajo móviles, Ultrabooks y Gaming laptops de alta gama.", "color": "amber"},
        "Tablets & iPads": {"icon": "📱", "desc": "Dispositivos táctiles para diseño, consumo de medios y movilidad total.", "color": "blue"},
        "Consolas de Forja": {"icon": "🎮", "desc": "Sistemas de entretenimiento: PS5, Xbox Series, Switch y retro-emulación.", "color": "purple"},
        "PC Desktop": {"icon": "🖥️", "desc": "Torres personalizadas, estaciones de minería y setups profesionales.", "color": "emerald"},
        "Componentes Core": {"icon": "⚙️", "desc": "Procesadores (CPU), Gráficas (GPU), RAM y almacenamiento masivo.", "color": "red"},
        "Periféricos & Accesorios": {"icon": "⌨️", "desc": "Teclados mecánicos, ratones de precisión y audio de alta fidelidad.", "color": "cyan"},
        "Taller de Reparación": {"icon": "🔧", "desc": "Servicios técnicos: Reballing, cambio de pantallas y aligerado de carga.", "color": "orange"},
        "Redes & Enlaces": {"icon": "📡", "desc": "Routers, switches, antenas y conectividad de largo alcance.", "color": "indigo"},
        "Alquimia de Software": {"icon": "💾", "desc": "Sistemas operativos, firmwares personalizados y herramientas de diagnóstico.", "color": "fuchsia"},
        "Artefactos & Gadgets": {"icon": "⌚", "desc": "Smartwatches, tecnología wearable y gadgets experimentales.", "color": "rose"},
    }.get(category_name, {"icon": "📦", "desc": "", "color": "amber"})
    
    return render(request, "category_detail.html", {
        "category_name": category_name,
        "category_info": category_info,
        "news": news_page,
        "page_obj": news_page,
    })


def can_moderate(user):
    if not user.is_authenticated:
        return False
    if user.is_staff or user.is_superuser:
        return True
    if not hasattr(user, 'profile'):
        return False
    return user.profile.can_moderate()


def can_ban(user):
    if not user.is_authenticated:
        return False
    if user.is_staff or user.is_superuser:
        return True
    if not hasattr(user, 'profile'):
        return False
    return user.profile.can_ban()


@login_required
@user_passes_test(can_moderate)
def mod_panel(request):
    # Crear perfil si no existe
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user, role='rey' if request.user.is_superuser else 'member')
    
    # Si es superuser, tiene todos los permisos
    if request.user.is_superuser:
        news_form = NewsItemForm()
        blog_form = BlogPostForm()
        my_news = NewsItem.objects.all().order_by("-created_at")[:5]
        my_blogs = BlogPost.objects.all().order_by("-created_at")[:5]
    elif hasattr(request.user, 'profile') and request.user.profile.can_edit():
        news_form = NewsItemForm()
        blog_form = BlogPostForm()
        my_news = NewsItem.objects.all().order_by("-created_at")[:5]
        my_blogs = BlogPost.objects.all().order_by("-created_at")[:5]
    else:
        news_form = None
        blog_form = None
        my_news = []
        my_blogs = []
    
    reports = Report.objects.filter(status='pending').order_by('-created_at')[:20]
    comments = Comment.objects.all().order_by('-created_at')[:50]
    users_count = User.objects.count()
    pending_reports = Report.objects.filter(status='pending').count()
    active_bans = Ban.objects.filter(is_active=True).count()
    total_news = NewsItem.objects.count()
    total_blogs = BlogPost.objects.count()
    latest_news = NewsItem.objects.all().order_by("-created_at")[:5]
    latest_blogs = BlogPost.objects.all().order_by("-created_at")[:5]
    
    return render(request, "mod_panel.html", {
        "reports": reports,
        "comments": comments,
        "users_count": users_count,
        "reports_count": pending_reports,
        "pending_reports": pending_reports,
        "active_bans": active_bans,
        "total_news": total_news,
        "total_blogs": total_blogs,
        "latest_news": latest_news,
        "latest_blogs": latest_blogs,
        "news_form": news_form,
        "blog_form": blog_form,
        "my_news": my_news,
        "my_blogs": my_blogs,
    })


@login_required
def create_report(request):
    if request.method == "POST":
        report_type = request.POST.get("report_type")
        content = request.POST.get("content")
        comment_id = request.POST.get("comment_id")
        user_id = request.POST.get("user_id")
        
        if not content:
            messages.error(request, "El reporte no puede estar vacío.")
            return redirect(request.META.get("HTTP_REFERER", "index"))
        
        report = Report.objects.create(
            reporter=request.user,
            report_type=report_type,
            content=content
        )
        
        if comment_id:
            report.comment = get_object_or_404(Comment, id=comment_id)
        if user_id:
            report.reported_user = get_object_or_404(User, id=user_id)
        
        report.save()
        messages.success(request, "Reporte enviado. Gracias por mantener la comunidad limpia.")
        return redirect(request.META.get("HTTP_REFERER", "index"))
    return redirect("index")


@login_required
@user_passes_test(can_moderate)
def resolve_report(request, report_id):
    if not can_moderate(request.user):
        messages.error(request, "No tienes permisos de moderador.")
        return redirect("index")
    
    report = get_object_or_404(Report, id=report_id)
    
    if request.method == "POST":
        action = request.POST.get("action")
        notes = request.POST.get("notes", "")
        
        report.resolved_by = request.user
        report.resolution_notes = notes
        
        if action == "dismiss":
            report.status = "dismissed"
            messages.info(request, "Reporte descartado.")
        elif action == "resolve":
            report.status = "resolved"
            messages.success(request, "Reporte resuelto.")
        
        report.save()
        return redirect("mod_panel")
    
    return render(request, "resolve_report.html", {"report": report})


@login_required
@user_passes_test(can_ban)
def ban_user(request, user_id):
    if request.method == "POST":
        user_to_ban = get_object_or_404(User, id=user_id)
        reason = request.POST.get("reason")
        ban_type = request.POST.get("ban_type")
        
        if not reason:
            messages.error(request, "El motivo del ban es requerido.")
            return redirect("mod_panel")
        
        from django.utils import timezone
        from datetime import timedelta
        
        ban = Ban.objects.create(
            user=user_to_ban,
            banned_by=request.user,
            reason=reason,
            ban_type=ban_type
        )
        
        if ban_type == "temporary":
            days = int(request.POST.get("days", 7))
            ban.expires_at = timezone.now() + timedelta(days=days)
            ban.save()
            messages.success(request, f"Usuario baneado temporalmente por {days} días.")
        else:
            messages.success(request, f"Usuario {user_to_ban.username} baneado permanentemente.")
        
        return redirect("mod_panel")
    
    user_to_ban = get_object_or_404(User, id=user_id)
    return render(request, "ban_user.html", {"user_to_ban": user_to_ban})


@login_required
@user_passes_test(can_ban)
def unban_user(request, ban_id):
    ban = get_object_or_404(Ban, id=ban_id)
    ban.is_active = False
    ban.save()
    messages.success(request, f"Usuario {ban.user.username} desbaneado.")
    return redirect("mod_panel")


@login_required
@user_passes_test(can_moderate)
def delete_comment_mod(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, "Comentario eliminado.")
    return redirect(request.META.get("HTTP_REFERER", "index"))


def servicios(request):
    paquetes = [
        {
            "nombre": "Paquete Impulso",
            "precio": "RD$7,500",
            "badge": "🥉",
            "color": "bronze",
            "descripcion": "Ideal para pequeños negocios que quieren presencia profesional.",
            "incluye": [
                "Sitio web de 1 a 3 páginas",
                "Diseño adaptable a celular",
                "Botón directo a WhatsApp",
                "Formulario de contacto",
                "Integración con Google Maps",
                "Entrega en 5-7 días",
            ],
            "perfecto_para": "Salones, barberías, técnicos, consultores",
        },
        {
            "nombre": "Paquete Crecimiento",
            "precio": "RD$18,000",
            "badge": "🥈",
            "color": "silver",
            "descripcion": "Para negocios que quieren captar clientes constantemente.",
            "incluye": [
                "Todo lo del paquete Impulso",
                "Hasta 6 páginas",
                "Optimización SEO local básica",
                "Integración con redes sociales",
                "Configuración de Google Business",
                "Capacitación básica para usar el sitio",
            ],
            "perfecto_para": "Clínicas, abogados, restaurantes, academias",
        },
        {
            "nombre": "Paquete Ventas Online",
            "precio": "RD$35,000",
            "badge": "🥇",
            "color": "gold",
            "descripcion": "Para negocios que quieren vender por internet.",
            "incluye": [
                "Tienda online (hasta 30 productos)",
                "Carrito de compras",
                "Integración de pagos",
                "Configuración de envíos",
                "SEO básico",
                "30 días de soporte",
                "Entrenamiento en gestión de productos",
            ],
            "perfecto_para": "Tiendas de ropa, suplementos, productos naturales",
        },
    ]
    
    mantenimiento = {
        "nombre": "Plan Mantenimiento",
        "precio": "RD$2,500/mes",
        "descripcion": "Mantén tu sitio actualizado y seguro",
        "incluye": [
            "Actualizaciones de contenido",
            "Cambios menores",
            "Respaldo mensual",
            "Soporte prioritario",
        ],
    }
    
    return render(request, "servicios.html", {
        "paquetes": paquetes,
        "mantenimiento": mantenimiento,
    })


def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")
        tipo = request.POST.get("tipo", "general")
        
        # Aquí podrías enviar un email o guardar en la base de datos
        messages.success(request, f"¡Gracias {nombre}! Tu mensaje ha sido enviado. Te responderé pronto.")
        return redirect("contacto")
    
    return render(request, "contacto.html")


def privacidad(request):
    return render(request, "privacidad.html")


def terminos(request):
    return render(request, "terminos.html")


def portafolio(request):
    from .models import Portfolio, Testimonial
    
    trabajos = Portfolio.objects.filter(activo=True).order_by("-orden", "-created_at")
    testimonios = Testimonial.objects.filter(activo=True).order_by("-created_at")[:5]
    
    return render(request, "portafolio.html", {
        "trabajos": trabajos,
        "testimonios": testimonios,
    })


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        nombre = request.POST.get("nombre", "")
        
        from .models import Subscriber
        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request, "Este email ya está suscrito.")
        else:
            Subscriber.objects.create(email=email, nombre=nombre)
            messages.success(request, "¡Te has suscrito correctamente!")
        
        return redirect(request.META.get("HTTP_REFERER", "index"))
    
    return redirect("index")
