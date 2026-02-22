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

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 966, in render_annotated
return self.render(context)
~~~~~~~~~~~^^^^^^^^^
Menu
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/loader_tags.py", line 157, in render
return compiled_parent.\_render(context)
~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 167, in \_render
return self.nodelist.render(context)
~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 966, in render_annotated
return self.render(context)
~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/loader_tags.py", line 63, in render
result = block.nodelist.render(context)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 966, in render_annotated
return self.render(context)
~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/defaulttags.py", line 194, in render
len_values = len(values)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 382, in **len**
self.\_fetch_all()
~~~~~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 1886, in \_fetch_all
self.\_result_cache = list(self.\_iterable_class(self))
~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 93, in **iter**
results = compiler.execute_sql(
chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size
)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/sql/compiler.py", line 1562, in execute_sql
cursor.execute(sql, params)
~~~~~~~~~~~~~~^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 102, in execute
return super().execute(sql, params)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 67, in execute
return self.\_execute_with_wrappers(
~~~~~~~~~~~~~~~~~~~~~~~~~~~^
sql, params, many=False, executor=self.\_execute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
)
^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 80, in \_execute_with_wrappers
return executor(sql, params, many, context)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 84, in \_execute
with self.db.wrap_database_errors:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/utils.py", line 91, in **exit**
raise dj_exc_value.with_traceback(traceback) from exc_value
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 89, in \_execute
return self.cursor.execute(sql, params)
~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py", line 328, in execute
return super().execute(query, params)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
django.db.utils.OperationalError: no such table: core_newsitem
127.0.0.1 - - [22/Feb/2026:17:12:39 +0000] "GET / HTTP/1.1" 500 201995 "https://the-silicon-citadel.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
Internal Server Error: /
Traceback (most recent call last):
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 89, in \_execute
return self.cursor.execute(sql, params)
~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py", line 328, in execute
return super().execute(query, params)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
sqlite3.OperationalError: no such table: core_newsitem
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/core/handlers/exception.py", line 55, in inner
response = get_response(request)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/core/handlers/base.py", line 197, in \_get_response
response = wrapped_callback(request, \*callback_args, \*\*callback_kwargs)
File "/opt/render/project/src/core/views.py", line 57, in index
return render(request, "index.html", context)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/shortcuts.py", line 24, in render
content = loader.render_to_string(template_name, context, request, using=using)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/loader.py", line 62, in render_to_string
return template.render(context, request)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/backends/django.py", line 61, in render
return self.template.render(context)
~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 175, in render
return self.\_render(context)
~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 167, in \_render
return self.nodelist.render(context)
~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 966, in render_annotated
return self.render(context)
~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/loader_tags.py", line 157, in render
return compiled_parent.\_render(context)
~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 167, in \_render
return self.nodelist.render(context)
~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 966, in render_annotated
return self.render(context)
~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/loader_tags.py", line 63, in render
result = block.nodelist.render(context)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 1005, in render
return SafeString("".join([node.render_annotated(context) for node in self]))
~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/base.py", line 966, in render_annotated
return self.render(context)
~~~~~~~~~~~^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/template/defaulttags.py", line 194, in render
len_values = len(values)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 382, in **len**
self.\_fetch_all()
~~~~~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 1886, in \_fetch_all
self.\_result_cache = list(self.\_iterable_class(self))
~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 93, in **iter**
results = compiler.execute_sql(
chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size
)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/models/sql/compiler.py", line 1562, in execute_sql
cursor.execute(sql, params)
~~~~~~~~~~~~~~^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 102, in execute
return super().execute(sql, params)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 67, in execute
return self.\_execute_with_wrappers(
~~~~~~~~~~~~~~~~~~~~~~~~~~~^
sql, params, many=False, executor=self.\_execute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
)
^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 80, in \_execute_with_wrappers
return executor(sql, params, many, context)
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 84, in \_execute
with self.db.wrap_database_errors:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/utils.py", line 91, in **exit**
raise dj_exc_value.with_traceback(traceback) from exc_value
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 89, in \_execute
return self.cursor.execute(sql, params)
~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py", line 328, in execute
return super().execute(query, params)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
django.db.utils.OperationalError: no such table: core_newsitem
127.0.0.1 - - [22/Feb/2026:17:15:22 +0000] "GET / HTTP/1.1" 500 202130 "https://the-silicon-citadel.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
