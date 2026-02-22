# Notas del Proyecto - The Silicon Citadel

---

## 📋 Estado del Proyecto

**Última actualización:** 22/Feb/2026

### Páginas principales:

- `/` - Home
- `/blogs/` - Todos los artículos
- `/actualizaciones/` - Todas las noticias
- `/categories/` - Categorías
- `/creator/my-news/` - Mis noticias
- `/creator/my-blogs/` - Mis blogs

---

## ✅ Mejoras Realizadas

1. **Sistema de Markdown** - Editor con vista previa y guía
2. **Imágenes externas** - Soporte para URLs de imágenes
3. **Descripción corta** - Para listas truncadas
4. **Seguridad XSS** - DOMPurify para sanitizar HTML
5. **Limpieza de código** - Comentarios y organización

---

## ⚠️ Notas para Producción

Antes de poner en producción, configurar en `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['tusitio.com']
SECRET_KEY = os.environ.get('SECRET_KEY')
```

---

## 💡 Ideas y Nuevas Funcionalidades

_(Pega tus ideas aquí)_

## Error

OperationalError at /
no such table: core_newsitem
Request Method: GET
Request URL: https://the-silicon-citadel.onrender.com/
Django Version: 4.2.28
Exception Type: OperationalError
Exception Value:
no such table: core_newsitem
Exception Location: /opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py, line 328, in execute
Raised during: core.views.index
Python Executable: /opt/render/project/src/.venv/bin/python3.14
Python Version: 3.14.3
Python Path:
['/opt/render/project/src',
'/opt/render/project/src/.venv/bin',
'/opt/render/project/python/Python-3.14.3/lib/python314.zip',
'/opt/render/project/python/Python-3.14.3/lib/python3.14',
'/opt/render/project/python/Python-3.14.3/lib/python3.14/lib-dynload',
'/opt/render/project/src/.venv/lib/python3.14/site-packages']
Server time: Sun, 22 Feb 2026 15:49:00 +0000
Error during template rendering
In template /opt/render/project/src/templates/index.html, error at line 65

no such table: core_newsitem
55 </form>
56 </div>
57
58 <!-- SECCIÓN DE ENTRADAS DETALLADAS -->
59 <div class="card" style="background-color: var(--card-bg);">
60 <h2 class="text-xl font-black italic uppercase tracking-tighter mb-4 flex items-center gap-2" style="color: var(--text-main);">
61 <span class="text-yellow-600">📜</span> Fortress Dispatches
62 </h2>
63  
64 <div class="news-scroll-container">
65 {% for item in news_items %}
66 <a href="{% url 'news_detail' item.slug %}" class="news-item">
67 {% if item.image or item.image_url %}
68 <img src="{{ item.get_image }}" alt="{{ item.title }}" class="news-item-img border border-white/5">
69 {% else %}
70 <img src="https://placehold.co/80x80/1a1a15/fbbf24?text=ARTIFACT" alt="Thumbnail" class="news-item-img border border-white/5">
71 {% endif %}
72 <div class="news-item-content">
73 <span class="news-item-title link-custom font-bold italic">{{ item.title }}</span>
74 <p class="news-item-desc text-[11px] leading-relaxed">{{ item.get_description|truncatewords:15 }}</p>
75 <div class="news-item-meta text-[9px] uppercase font-bold tracking-tighter flex items-center gap-4">
Traceback Switch to copy-and-paste view
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py, line 89, in \_execute
return self.cursor.execute(sql, params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py, line 328, in execute
return super().execute(query, params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
The above exception (no such table: core_newsitem) was the direct cause of the following exception:
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/core/handlers/exception.py, line 55, in inner
response = get_response(request)
^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/core/handlers/base.py, line 197, in \_get_response
response = wrapped_callback(request, \*callback_args, \*\*callback_kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/core/views.py, line 57, in index
return render(request, "index.html", context)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/shortcuts.py, line 24, in render
content = loader.render_to_string(template_name, context, request, using=using)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/loader.py, line 62, in render_to_string
return template.render(context, request)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/backends/django.py, line 61, in render
return self.template.render(context)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 175, in render
return self.\_render(context)
^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 167, in \_render
return self.nodelist.render(context)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 966, in render_annotated
return self.render(context)
^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/loader_tags.py, line 157, in render
return compiled_parent.\_render(context)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 167, in \_render
return self.nodelist.render(context)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 966, in render_annotated
return self.render(context)
^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/loader_tags.py, line 63, in render
result = block.nodelist.render(context)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py, line 966, in render_annotated
return self.render(context)
^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/defaulttags.py, line 194, in render
len_values = len(values)
^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py, line 382, in **len**
self.\_fetch_all()
^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py, line 1886, in \_fetch_all
self.\_result_cache = list(self.\_iterable_class(self))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py, line 93, in **iter**
results = compiler.execute_sql(
…
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/sql/compiler.py, line 1562, in execute_sql
cursor.execute(sql, params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py, line 102, in execute
return super().execute(sql, params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py, line 67, in execute
return self.\_execute_with_wrappers(
…
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py, line 80, in \_execute_with_wrappers
return executor(sql, params, many, context)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py, line 84, in \_execute
with self.db.wrap_database_errors:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/utils.py, line 91, in **exit**
raise dj_exc_value.with_traceback(traceback) from exc_value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py, line 89, in \_execute
return self.cursor.execute(sql, params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py, line 328, in execute
return super().execute(query, params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
Request information
USER
AnonymousUser

GET
No GET data

POST
No POST data

FILES
No FILES data

No cookie data

META
Variable Value
HTTP*ACCEPT
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/\_;q=0.8'
HTTP_ACCEPT_ENCODING
'gzip, br'
HTTP_ACCEPT_LANGUAGE
'es-419,es;q=0.8'
HTTP_CACHE_CONTROL
'max-age=0'
HTTP_CDN_LOOP
'cloudflare; loops=1'
HTTP_CF_CONNECTING_IP
'190.167.253.91'
HTTP_CF_IPCOUNTRY
'DO'
HTTP_CF_RAY
'9d1fa183ce0df3a1-PDX'
HTTP_CF_VISITOR
'{"scheme":"https"}'
HTTP_HOST
'the-silicon-citadel.onrender.com'
HTTP_PRIORITY
'u=0, i'
HTTP_RENDER_PROXY_TTL
'4'
HTTP_RNDR_ID
'8fb242dd-3acd-4779'
HTTP_SEC_CH_UA
'"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"'
HTTP_SEC_CH_UA_MOBILE
'?0'
HTTP_SEC_CH_UA_PLATFORM
'"Windows"'
HTTP_SEC_FETCH_DEST
'document'
HTTP_SEC_FETCH_MODE
'navigate'
HTTP_SEC_FETCH_SITE
'cross-site'
HTTP_SEC_FETCH_USER
'?1'
HTTP_SEC_GPC
'1'
HTTP_TRUE_CLIENT_IP
'190.167.253.91'
HTTP_UPGRADE_INSECURE_REQUESTS
'1'
HTTP_USER_AGENT
('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
'Gecko) Chrome/145.0.0.0 Safari/537.36')
HTTP_X_FORWARDED_FOR
'190.167.253.91, 104.23.160.40, 10.22.87.3'
HTTP_X_FORWARDED_PROTO
'https'
HTTP_X_REQUEST_START
'1771775340188216'
PATH_INFO
'/'
QUERY_STRING
''
RAW_URI
'/'
REMOTE_ADDR
'127.0.0.1'
REMOTE_PORT
'40296'
REQUEST_METHOD
'GET'
SCRIPT_NAME
''
SERVER_NAME
'0.0.0.0'
SERVER_PORT
'10000'
SERVER_PROTOCOL
'HTTP/1.1'
SERVER_SOFTWARE
'gunicorn/25.1.0'
gunicorn.socket
<socket.socket fd=11, family=2, type=1, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 40296)>
wsgi.early_hints
<function \_make_early_hints_callback.<locals>.send_early_hints at 0x7857c881fd70>
wsgi.errors
<gunicorn.http.wsgi.WSGIErrorsWrapper object at 0x7857c91bd360>
wsgi.file_wrapper
<class 'gunicorn.http.wsgi.FileWrapper'>
wsgi.input
<gunicorn.http.body.Body object at 0x7857c862e0f0>
wsgi.input_terminated
True
wsgi.multiprocess
False
wsgi.multithread
False
wsgi.run_once
False
wsgi.url_scheme
'https'
wsgi.version
(1, 0)
Settings
Using settings module silicon.settings
Setting Value
ABSOLUTE_URL_OVERRIDES
{}
ADMINS
[]
ALLOWED_HOSTS
['the-silicon-citadel.onrender.com']
APPEND_SLASH
True
AUTHENTICATION_BACKENDS
['django.contrib.auth.backends.ModelBackend']
AUTH_PASSWORD_VALIDATORS
'**\*\*\*\***\*\*\*\***\*\*\*\***'
AUTH_USER_MODEL
'auth.User'
BASE_DIR
PosixPath('/opt/render/project/src')
CACHES
{'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
CACHE_MIDDLEWARE_ALIAS
'default'
CACHE_MIDDLEWARE_KEY_PREFIX
'**\*\*\*\***\*\*\*\***\*\*\*\***'
CACHE_MIDDLEWARE_SECONDS
600
CSRF_COOKIE_AGE
31449600
CSRF_COOKIE_DOMAIN
None
CSRF_COOKIE_HTTPONLY
False
CSRF_COOKIE_MASKED
False
CSRF_COOKIE_NAME
'csrftoken'
CSRF_COOKIE_PATH
'/'
CSRF_COOKIE_SAMESITE
'Lax'
CSRF_COOKIE_SECURE
False
CSRF_FAILURE_VIEW
'django.views.csrf.csrf_failure'
CSRF_HEADER_NAME
'HTTP_X_CSRFTOKEN'
CSRF_TRUSTED_ORIGINS
[]
CSRF_USE_SESSIONS
False
DATABASES
{'default': {'ATOMIC_REQUESTS': False,
'AUTOCOMMIT': True,
'CONN_HEALTH_CHECKS': False,
'CONN_MAX_AGE': 0,
'ENGINE': 'django.db.backends.sqlite3',
'HOST': '',
'NAME': PosixPath('/opt/render/project/src/db.sqlite3'),
'OPTIONS': {},
'PASSWORD': '**\*\*\*\***\*\*\*\***\*\*\*\***',
'PORT': '',
'TEST': {'CHARSET': None,
'COLLATION': None,
'MIGRATE': True,
'MIRROR': None,
'NAME': None},
'TIME_ZONE': None,
'USER': ''}}
DATABASE_ROUTERS
[]
DATA_UPLOAD_MAX_MEMORY_SIZE
2621440
DATA_UPLOAD_MAX_NUMBER_FIELDS
1000
DATA_UPLOAD_MAX_NUMBER_FILES
100
DATETIME_FORMAT
'N j, Y, P'
DATETIME_INPUT_FORMATS
['%Y-%m-%d %H:%M:%S',
'%Y-%m-%d %H:%M:%S.%f',
'%Y-%m-%d %H:%M',
'%m/%d/%Y %H:%M:%S',
'%m/%d/%Y %H:%M:%S.%f',
'%m/%d/%Y %H:%M',
'%m/%d/%y %H:%M:%S',
'%m/%d/%y %H:%M:%S.%f',
'%m/%d/%y %H:%M']
DATE_FORMAT
'N j, Y'
DATE_INPUT_FORMATS
['%Y-%m-%d',
'%m/%d/%Y',
'%m/%d/%y',
'%b %d %Y',
'%b %d, %Y',
'%d %b %Y',
'%d %b, %Y',
'%B %d %Y',
'%B %d, %Y',
'%d %B %Y',
'%d %B, %Y']
DEBUG
True
DEBUG_PROPAGATE_EXCEPTIONS
False
DECIMAL_SEPARATOR
'.'
DEFAULT_AUTO_FIELD
'django.db.models.BigAutoField'
DEFAULT_CHARSET
'utf-8'
DEFAULT_EXCEPTION_REPORTER
'django.views.debug.ExceptionReporter'
DEFAULT_EXCEPTION_REPORTER_FILTER
'django.views.debug.SafeExceptionReporterFilter'
DEFAULT_FILE_STORAGE
'django.core.files.storage.FileSystemStorage'
DEFAULT_FROM_EMAIL
'webmaster@localhost'
DEFAULT_INDEX_TABLESPACE
''
DEFAULT_TABLESPACE
''
DISALLOWED_USER_AGENTS
[]
EMAIL_BACKEND
'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST
'localhost'
EMAIL_HOST_PASSWORD
'**\*\*\*\***\*\*\*\***\*\*\*\***'
EMAIL_HOST_USER
''
EMAIL_PORT
25
EMAIL_SSL_CERTFILE
None
EMAIL_SSL_KEYFILE
'**\*\*\*\***\*\*\*\***\*\*\*\***'
EMAIL_SUBJECT_PREFIX
'[Django] '
EMAIL_TIMEOUT
None
EMAIL_USE_LOCALTIME
False
EMAIL_USE_SSL
False
EMAIL_USE_TLS
False
FILE_UPLOAD_DIRECTORY_PERMISSIONS
None
FILE_UPLOAD_HANDLERS
['django.core.files.uploadhandler.MemoryFileUploadHandler',
'django.core.files.uploadhandler.TemporaryFileUploadHandler']
FILE_UPLOAD_MAX_MEMORY_SIZE
2621440
FILE_UPLOAD_PERMISSIONS
420
FILE_UPLOAD_TEMP_DIR
None
FIRST_DAY_OF_WEEK
0
FIXTURE_DIRS
[]
FORCE_SCRIPT_NAME
None
FORMAT_MODULE_PATH
None
FORM_RENDERER
'django.forms.renderers.DjangoTemplates'
IGNORABLE_404_URLS
[]
INSTALLED_APPS
['django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'core']
INTERNAL_IPS
[]
LANGUAGES
[('af', 'Afrikaans'),
('ar', 'Arabic'),
('ar-dz', 'Algerian Arabic'),
('ast', 'Asturian'),
('az', 'Azerbaijani'),
('bg', 'Bulgarian'),
('be', 'Belarusian'),
('bn', 'Bengali'),
('br', 'Breton'),
('bs', 'Bosnian'),
('ca', 'Catalan'),
('ckb', 'Central Kurdish (Sorani)'),
('cs', 'Czech'),
('cy', 'Welsh'),
('da', 'Danish'),
('de', 'German'),
('dsb', 'Lower Sorbian'),
('el', 'Greek'),
('en', 'English'),
('en-au', 'Australian English'),
('en-gb', 'British English'),
('eo', 'Esperanto'),
('es', 'Spanish'),
('es-ar', 'Argentinian Spanish'),
('es-co', 'Colombian Spanish'),
('es-mx', 'Mexican Spanish'),
('es-ni', 'Nicaraguan Spanish'),
('es-ve', 'Venezuelan Spanish'),
('et', 'Estonian'),
('eu', 'Basque'),
('fa', 'Persian'),
('fi', 'Finnish'),
('fr', 'French'),
('fy', 'Frisian'),
('ga', 'Irish'),
('gd', 'Scottish Gaelic'),
('gl', 'Galician'),
('he', 'Hebrew'),
('hi', 'Hindi'),
('hr', 'Croatian'),
('hsb', 'Upper Sorbian'),
('hu', 'Hungarian'),
('hy', 'Armenian'),
('ia', 'Interlingua'),
('id', 'Indonesian'),
('ig', 'Igbo'),
('io', 'Ido'),
('is', 'Icelandic'),
('it', 'Italian'),
('ja', 'Japanese'),
('ka', 'Georgian'),
('kab', 'Kabyle'),
('kk', 'Kazakh'),
('km', 'Khmer'),
('kn', 'Kannada'),
('ko', 'Korean'),
('ky', 'Kyrgyz'),
('lb', 'Luxembourgish'),
('lt', 'Lithuanian'),
('lv', 'Latvian'),
('mk', 'Macedonian'),
('ml', 'Malayalam'),
('mn', 'Mongolian'),
('mr', 'Marathi'),
('ms', 'Malay'),
('my', 'Burmese'),
('nb', 'Norwegian Bokmål'),
('ne', 'Nepali'),
('nl', 'Dutch'),
('nn', 'Norwegian Nynorsk'),
('os', 'Ossetic'),
('pa', 'Punjabi'),
('pl', 'Polish'),
('pt', 'Portuguese'),
('pt-br', 'Brazilian Portuguese'),
('ro', 'Romanian'),
('ru', 'Russian'),
('sk', 'Slovak'),
('sl', 'Slovenian'),
('sq', 'Albanian'),
('sr', 'Serbian'),
('sr-latn', 'Serbian Latin'),
('sv', 'Swedish'),
('sw', 'Swahili'),
('ta', 'Tamil'),
('te', 'Telugu'),
('tg', 'Tajik'),
('th', 'Thai'),
('tk', 'Turkmen'),
('tr', 'Turkish'),
('tt', 'Tatar'),
('udm', 'Udmurt'),
('uk', 'Ukrainian'),
('ur', 'Urdu'),
('uz', 'Uzbek'),
('vi', 'Vietnamese'),
('zh-hans', 'Simplified Chinese'),
('zh-hant', 'Traditional Chinese')]
LANGUAGES_BIDI
['he', 'ar', 'ar-dz', 'ckb', 'fa', 'ur']
LANGUAGE_CODE
'es-es'
LANGUAGE_COOKIE_AGE
None
LANGUAGE_COOKIE_DOMAIN
None
LANGUAGE_COOKIE_HTTPONLY
False
LANGUAGE_COOKIE_NAME
'django_language'
LANGUAGE_COOKIE_PATH
'/'
LANGUAGE_COOKIE_SAMESITE
None
LANGUAGE_COOKIE_SECURE
False
LOCALE_PATHS
[]
LOGGING
{}
LOGGING_CONFIG
'logging.config.dictConfig'
LOGIN_REDIRECT_URL
'/accounts/profile/'
LOGIN_URL
'/accounts/login/'
LOGOUT_REDIRECT_URL
None
MANAGERS
[]
MEDIA_ROOT
PosixPath('/opt/render/project/src/media')
MEDIA_URL
'/media/'
MESSAGE_STORAGE
'django.contrib.messages.storage.fallback.FallbackStorage'
MIDDLEWARE
['django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware']
MIGRATION_MODULES
{}
MONTH_DAY_FORMAT
'F j'
NUMBER_GROUPING
0
PASSWORD_HASHERS
'**\*\*\*\***\*\*\*\***\*\*\*\***'
PASSWORD_RESET_TIMEOUT
'**\*\*\*\***\*\*\*\***\*\*\*\***'
PREPEND_WWW
False
ROOT_URLCONF
'silicon.urls'
SECRET_KEY
'**\*\*\*\***\*\*\*\***\*\*\*\***'
SECRET_KEY_FALLBACKS
'**\*\*\*\***\*\*\*\***\*\*\*\***'
SECURE_BROWSER_XSS_FILTER
True
SECURE_CONTENT_TYPE_NOSNIFF
True
SECURE_CROSS_ORIGIN_OPENER_POLICY
'same-origin'
SECURE_HSTS_INCLUDE_SUBDOMAINS
False
SECURE_HSTS_PRELOAD
False
SECURE_HSTS_SECONDS
0
SECURE_PROXY_SSL_HEADER
None
SECURE_REDIRECT_EXEMPT
[]
SECURE_REFERRER_POLICY
'same-origin'
SECURE_SSL_HOST
None
SECURE_SSL_REDIRECT
False
SERVER_EMAIL
'root@localhost'
SESSION_CACHE_ALIAS
'default'
SESSION_COOKIE_AGE
1209600
SESSION_COOKIE_DOMAIN
None
SESSION_COOKIE_HTTPONLY
True
SESSION_COOKIE_NAME
'sessionid'
SESSION_COOKIE_PATH
'/'
SESSION_COOKIE_SAMESITE
'Lax'
SESSION_COOKIE_SECURE
False
SESSION_ENGINE
'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE
False
SESSION_FILE_PATH
None
SESSION_SAVE_EVERY_REQUEST
False
SESSION_SERIALIZER
'django.contrib.sessions.serializers.JSONSerializer'
SETTINGS_MODULE
'silicon.settings'
SHORT_DATETIME_FORMAT
'm/d/Y P'
SHORT_DATE_FORMAT
'm/d/Y'
SIGNING_BACKEND
'django.core.signing.TimestampSigner'
SILENCED_SYSTEM_CHECKS
[]
STATICFILES_DIRS
[PosixPath('/opt/render/project/src/static')]
STATICFILES_FINDERS
['django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder']
STATICFILES_STORAGE
'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT
PosixPath('/opt/render/project/src/staticfiles')
STATIC_URL
'/static/'
STORAGES
{'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'}}
TEMPLATES
[{'APP_DIRS': True,
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [PosixPath('/opt/render/project/src/templates')],
'OPTIONS': {'context_processors': ['django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
'django.template.context_processors.media']}}]
TEST_NON_SERIALIZED_APPS
[]
TEST_RUNNER
'django.test.runner.DiscoverRunner'
THOUSAND_SEPARATOR
','
TIME_FORMAT
'P'
TIME_INPUT_FORMATS
['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
TIME_ZONE
'UTC'
USE_DEPRECATED_PYTZ
False
USE_I18N
True
USE_L10N
True
USE_THOUSAND_SEPARATOR
False
USE_TZ
True
USE_X_FORWARDED_HOST
False
USE_X_FORWARDED_PORT
False
WSGI_APPLICATION
'silicon.wsgi.application'
X_FRAME_OPTIONS
'DENY'
YEAR_MONTH_FORMAT
'F Y'
You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard page generated by the handler for this status code.
