# The Silicon Citadel

Comunidad tecnológica de República Dominicana - Foro, blog y portal de servicios técnicos.

## 🚀 Características

- **Noticias y Actualizaciones** - Publicación de noticias tecnológicas con categorías
- **Blog/Manuseritos** - Artículos y guías con editor Markdown
- **Sistema de Usuarios** - Roles: member, vigilante, guardian, capitán, ancianos, rey
- **Sistema de Moderación** - Panel de control para staff
- **Comentarios y Bookmarks** - Interacción con contenido
- **Buscador** - Búsqueda en noticias y blogs

## 🛠️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/the-silicon-citadel.git
cd the-silicon-citadel

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

## 📁 Estructura

```
the-silicon-citadel/
├── core/               # App principal
│   ├── models.py       # Modelos de datos
│   ├── views.py        # Vistas del sitio
│   ├── urls.py         # Rutas
│   ├── forms.py        # Formularios
│   └── admin.py        # Configuración admin
├── templates/          # Templates HTML
├── static/             # CSS, JS, imágenes
├── silicon/            # Configuración Django
├── db.sqlite3          # Base de datos
└── requirements.txt     # Dependencias
```

## 🔧 Configuración

### Variables de Entorno (Producción)

```bash
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DATABASE_URL=postgres://user:pass@localhost:5432/dbname
```

### Servidor de Producción

```bash
# Usar gunicorn
gunicorn silicon.wsgi:application --bind 0.0.0.0:8000
```

## 📝 Rutas Principales

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal |
| `/blogs/` | Todos los artículos |
| `/actualizaciones/` | Todas las noticias |
| `/categories/` | Galería de categorías |
| `/account/login/` | Iniciar sesión |
| `/account/register/` | Registrarse |
| `/creator/my-news/` | Mis noticias |
| `/creator/my-blogs/` | Mis blogs |
| `/mod/` | Panel de moderación |

## 🎨 Tecnologías

- **Backend:** Django 4.2+
- **Frontend:** Tailwind CSS + Vanilla JS
- **Markdown:** marked.js + DOMPurify
- **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)

## 📄 Licencia

MIT License - Libre uso y modificación.

---

*The Silicon Citadel - Forjando el futuro tecnológico de RD*
