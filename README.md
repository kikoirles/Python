# Python-
Python 100% 
-- Apuntes de Python hasta el tema 9 

### Instalación Paquetes pyhton
```shell
pip install -r requirements.txt
```

```shell
pip install --upgrade pip
```
Si usas Pycharm como editor de texto importar Modolos de python como interpretes
setting > Project:() Python interpreter> 

### Proyecto 10 Juego Marcianos
### Proyecto 11 Extrator de datos web
### Proyecto 12 Gestor de restaurante
### Proyecto 13 Asistente de voz
### Proyecto 14 Controlador Facial Scaner
### Proyecto 15 Machine learnig introduccion (Graficos) 
### Proyecto 16 Django 
Configuración de `settings.py` en Django

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
