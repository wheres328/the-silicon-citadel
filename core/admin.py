from django.contrib import admin
from django.contrib.admin import AdminSite
from django.shortcuts import render
from django.urls import path, reverse
from django.utils.html import format_html
from .models import NewsItem, BlogPost, Profile, Comment


class ForgeAndChipAdminSite(AdminSite):
    title = "The Silicon Citadel"
    site_header = "The Silicon Citadel - Admin"
    index_title = "Panel de Control"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("dashboard/", self.admin_view(self.dashboard_view), name="dashboard"),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        latest_news = NewsItem.objects.all().order_by("-created_at")[:3]
        latest_blogs = BlogPost.objects.all().order_by("-created_at")[:3]
        
        total_news = NewsItem.objects.count()
        total_blogs = BlogPost.objects.count()
        total_comments = Comment.objects.count()
        
        context = {
            **self.each_context(request),
            "title": "Dashboard",
            "latest_news": latest_news,
            "latest_blogs": latest_blogs,
            "total_news": total_news,
            "total_blogs": total_blogs,
            "total_comments": total_comments,
        }
        return render(request, "admin/dashboard.html", context)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role_badge", "is_vip", "is_staff_member")
    list_filter = ("role", "is_vip", "is_staff_member")
    search_fields = ("user__username",)
    ordering = ("-role",)
    
    def role_badge(self, obj):
        colors = {
            'member': '#6b7280',
            'vigilante': '#3b82f6',
            'guardian': '#8b5cf6',
            'capitan': '#f59e0b',
            'ancianos': '#10b981',
            'rey': '#ef4444',
        }
        color = colors.get(obj.role, '#6b7280')
        role_display = obj.get_role_display()
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 8px; border-radius: 3px; font-size: 11px; font-weight: bold;">{}</span>',
            color, role_display
        )
    role_badge.short_description = "Rango"


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "status_badge")
    list_filter = ("category", "created_at")
    search_fields = ("title", "description")
    list_per_page = 20
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    
    fieldsets = (
        ("Contenido", {
            "fields": ("title", "slug", "description", "image", "category")
        }),
        ("Metadatos", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )
    
    readonly_fields = ("created_at", "slug")
    
    def status_badge(self, obj):
        return format_html(
            '<span style="background: #d4af37; color: #000; padding: 3px 8px; border-radius: 3px; font-size: 11px;">PUBLICADO</span>'
        )
    status_badge.short_description = "Estado"


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "status_badge")
    list_filter = ("date", "author")
    search_fields = ("title", "content")
    list_per_page = 20
    date_hierarchy = "date"
    ordering = ("-date",)
    
    fieldsets = (
        ("Contenido", {
            "fields": ("title", "slug", "author", "content", "date")
        }),
        ("Metadatos", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )
    
    readonly_fields = ("created_at", "slug")
    
    def status_badge(self, obj):
        return format_html(
            '<span style="background: #10b981; color: #fff; padding: 3px 8px; border-radius: 3px; font-size: 11px;">PUBLICADO</span>'
        )
    status_badge.short_description = "Estado"


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "content_preview", "target_object", "created_at")
    list_filter = ("created_at",)
    search_fields = ("content", "user__username")
    list_per_page = 20
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = "Comentario"
    
    def target_object(self, obj):
        if obj.news_item:
            return f"Noticia: {obj.news_item.title}"
        elif obj.blog_post:
            return f"Blog: {obj.blog_post.title}"
        return "Sin objeto"
    target_object.short_description = "En"


admin_site = ForgeAndChipAdminSite(name="forge_admin")

admin_site.register(Profile, ProfileAdmin)
admin_site.register(NewsItem, NewsItemAdmin)
admin_site.register(BlogPost, BlogPostAdmin)
admin_site.register(Comment, CommentAdmin)
