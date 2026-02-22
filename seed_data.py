import os
import django
from django.utils import timezone
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silicon.settings")
django.setup()

from core.models import NewsItem, BlogPost


def populate():
    # News Items
    news_data = [
        (
            "Nueva interfaz lanzada",
            "Hemos migrado oficialmente a Forge & Chip con sistema Django.",
            "Tecnología",
        ),
        (
            "98 Millones de Papers",
            "Nuevas fuentes añadidas a SciDB para researchers.",
            "Ciencia",
        ),
        (
            "Donaciones Activas",
            "Ya puedes donar usando criptomonedas directamente.",
            "Comunidad",
        ),
    ]

    for title, desc, cat in news_data:
        NewsItem.objects.get_or_create(title=title, description=desc, category=cat)

    # Blog Posts
    blog_data = [
        (
            "Migración a Django",
            "Hoy explicamos por qué Django es el futuro de nuestro desarrollo.",
            date(2026, 2, 20),
        ),
        (
            "Seguridad del Conocimiento",
            "Cómo protegemos los metadatos de Forge & Chip.",
            date(2026, 2, 18),
        ),
        (
            "Guía de Usuario",
            "Aprende a usar los nuevos filtros de búsqueda.",
            date(2025, 12, 10),
        ),
    ]

    for title, content, bdate in blog_data:
        BlogPost.objects.get_or_create(title=title, content=content, date=bdate)

    print("Datos iniciales creados con éxito.")


if __name__ == "__main__":
    populate()
