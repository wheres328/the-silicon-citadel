"""
=========================================
URLS DEL PROYECTO - THE SILICON CITADEL
=========================================

Este archivo mapea las URLs a sus vistas correspondientes.

Estructura de URLs:
- Raíz (/): Página principal
- /news/<slug>: Detalle de noticia
- /blog/<slug>: Detalle de blog
- /blogs/: Listado de todos los blogs
- /actualizaciones/: Listado de noticias
- /categories/: Página de categorías
- /account/: Sistema de autenticación
- /creator/: Panel de creador de contenido
- /mod/: Panel de moderación
- /servicios/, /contacto/, /privacidad/: Páginas estáticas
"""

from django.urls import path
from . import views

urlpatterns = [
    # =====================================
    # PÁGINAS PÚBLICAS
    # =====================================
    path("", views.index, name="index"),                                    # Home
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),    # Detalle noticia
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),   # Detalle blog
    path("blogs/", views.blogs, name="blogs"),                            # Todos los blogs
    path("actualizaciones/", views.actualizaciones, name="actualizaciones"),  # Todas las noticias
    path("vault/", views.vault, name="vault"),                           # Búsqueda
    path("connect/", views.connect, name="connect"),                     # Página de conexión
    path("search-results/", views.search_results, name="search_results"), # Resultados de búsqueda
    
    # Categorías
    path("categories/", views.categories_view, name="categories"),       # Galería de categorías
    path("categories/<str:category_name>/", views.category_detail, name="category_detail"),  # Detalle categoría
    
    # =====================================
    # AUTENTICACIÓN
    # =====================================
    path("account/login/", views.login_view, name="login"),
    path("account/logout/", views.logout_view, name="logout"),
    path("account/register/", views.register_view, name="register"),
    path("account/profile/", views.profile_view, name="profile"),
    
    # =====================================
    # CREADOR DE CONTENIDO (CREADOR/ADMIN)
    # =====================================
    path("creator/my-news/", views.my_news_view, name="my_news"),           # Mis noticias
    path("creator/my-blogs/", views.my_blogs_view, name="my_blogs"),        # Mis blogs
    path("creator/delete-news/<int:news_id>/", views.delete_news, name="delete_news"),
    path("creator/delete-blog/<int:blog_id>/", views.delete_blog, name="delete_blog"),
    path("creator/edit-news/<int:news_id>/", views.edit_news, name="edit_news"),
    path("creator/edit-blog/<int:blog_id>/", views.edit_blog, name="edit_blog"),
    
    # =====================================
    # ACCIONES PÚBLICAS
    # =====================================
    path("content/delete-news/<int:news_id>/", views.delete_news_public, name="delete_news_public"),
    path("content/delete-blog/<int:blog_id>/", views.delete_blog_public, name="delete_blog_public"),
    path("donate/", views.donate, name="donate"),
    path("upgrade-vip/", views.upgrade_vip, name="upgrade_vip"),
    path("create-news/", views.create_news, name="create_news"),
    path("create-blog/", views.create_blog, name="create_blog"),
    path("tribute/", views.tribute, name="tribute"),
    path("toggle-bookmark/", views.toggle_bookmark, name="toggle_bookmark"),
    path("guild-apply/", views.guild_application, name="guild_application"),
    path("add-comment/", views.add_comment, name="add_comment"),
    
    # =====================================
    # PÁGINAS ESTÁTICAS
    # =====================================
    path("servicios/", views.servicios, name="servicios"),
    path("contacto/", views.contacto, name="contacto"),
    path("privacidad/", views.privacidad, name="privacidad"),
    path("terminos/", views.terminos, name="terminos"),
    
    # =====================================
    # MODERACIÓN (STAFF)
    # =====================================
    path("mod/", views.mod_panel, name="mod_panel"),
    path("mod/report/", views.create_report, name="create_report"),
    path("mod/report/<int:report_id>/", views.resolve_report, name="resolve_report"),
    path("mod/ban/<int:user_id>/", views.ban_user, name="ban_user"),
    path("mod/unban/<int:ban_id>/", views.unban_user, name="unban_user"),
    path("mod/delete-comment/<int:comment_id>/", views.delete_comment_mod, name="delete_comment_mod"),
]
