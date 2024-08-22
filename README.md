# Python-
Python 100% 
## Proyecto 16 
## Configuración de `settings.py` en Django

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mi_app',  # Reemplaza 'mi_app' con tu aplicación personalizada
]

LANGUAGE_CODE = 'es'  # Código de idioma para español

TIME_ZONE = 'America/Mexico_City'  # Zona horaria de la Ciudad de México

USE_I18N = True  # Habilitar internacionalización
USE_L10N = True  # Habilitar localización
USE_TZ = True    # Usar Tiempo Universal Coordinado (UTC)
