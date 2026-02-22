"""
=========================================
FORMULARIOS DEL PROYECTO - THE SILICON CITADEL
=========================================

Este archivo define los formularios para crear y editar contenido.

Formularios:
- NewsItemForm: Para crear/editar noticias
  Campos: title, short_description, description, image, image_url, category
  
- BlogPostForm: Para crear/editar artículos/blogs
  Campos: title, author, short_description, content, image, image_url, date

Notas:
- Los campos image_url permiten usar imágenes externas (URL)
- short_description se usa para las listas (truncado automático)
- El contenido principal usa Markdown para formato
"""

from django import forms
from .models import NewsItem, BlogPost


class NewsItemForm(forms.ModelForm):
    """Formulario para crear y editar noticias"""
    class Meta:
        model = NewsItem
        fields = ["title", "short_description", "description", "image", "image_url", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Título de la actualización...",
                }
            ),
            "short_description": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Descripción corta para la lista (máx 300 caracteres)...",
                    "maxlength": "300",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Descripción completa...",
                    "rows": 6,
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "https://ejemplo.com/imagen.jpg",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "image": forms.FileInput(attrs={"class": "form-input-file"}),
        }


class BlogPostForm(forms.ModelForm):
    """Formulario para crear y editar artículos/blogs"""
    class Meta:
        model = BlogPost
        fields = ["title", "author", "short_description", "content", "image", "image_url", "date"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Título del artículo..."}
            ),
            "author": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nombre del autor..."}
            ),
            "short_description": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Descripción corta para listas (máx 300 caracteres)...",
                    "maxlength": "300",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Contenido completo del blog...",
                    "rows": 12,
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "https://ejemplo.com/imagen.jpg",
                }
            ),
            "image": forms.FileInput(attrs={"class": "form-input-file"}),
            "date": forms.DateInput(attrs={"class": "form-input", "type": "date"}),
        }
