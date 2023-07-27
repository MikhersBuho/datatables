import os
import django
import json

# Ajusta la ruta al archivo settings.py de tu proyecto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings.py')  
django.setup()

# Importa el modelo User después de configurar Django
from django.contrib.auth.models import User

def almacenar_desde_json():
    with open('database.json', encoding='utf-8') as file:
        data = json.load(file)
    return data
        
data = almacenar_desde_json()
for registro in data:
    print(registro)
    password = registro["password"]
    username = registro["username"]
    is_active = registro["is_active"]
    nombre = registro["nombre"]
    edad = str(registro["edad"])
    correo = registro["correo"]

    # Crea un nuevo objeto User y lo guarda en la base de datos
    usuario = User(
        password=password,
        username=username,
        is_active=is_active,
        first_name=nombre,
        phone=edad,
        email=correo,
    )
    usuario.save()
