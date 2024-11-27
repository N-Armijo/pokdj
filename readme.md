
# Proyecto de Gestión de Pokémon
## Norma Armijo

## **Descripción**

Este proyecto en Django es una aplicación de gestión de Pokémon que incluye funcionalidades de CRUD (Crear, Leer, Actualizar, Eliminar) y autenticación de usuarios. A continuación, encontrarás instrucciones para configurar el entorno y ejecutar la aplicación.

---

## **Configuración del Entorno Virtual**

### En Linux/Mac:
1. Crear el entorno virtual:
   ```bash
   python3 -m venv env
   ```
2. Activar el entorno virtual:
   ```bash
   source env/bin/activate
   ```

### En Windows CMD:
1. Crear el entorno virtual:
   ```cmd
   python -m venv env
   ```
2. Activar el entorno virtual:
   ```cmd
   env\Scripts\activate
   ```

### En Windows PowerShell:
1. Crear el entorno virtual:
   ```powershell
   python -m venv env
   ```
2. Activar permisos de ejecución de scripts:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   ```
3. Activar el entorno virtual:
   ```powershell
   ./env/Scripts/activate
   ```

---

## **Instalación de Dependencias**

El archivo **`requirements.txt`** contiene las dependencias necesarias para el proyecto.

1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Ejecutar el Proyecto en Django**

### En Linux/Mac:
1. Ejecutar el servidor:
   ```bash
   python3 manage.py runserver
   ```

### En Windows CMD:
1. Ejecutar el servidor:
   ```cmd
   python manage.py runserver
   ```

### En Windows PowerShell:
1. Ejecutar el servidor:
   ```powershell
   python manage.py runserver
   ```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

---

## **Funcionalidades Principales**

1. **Lista de Pokémon**: Visualiza todos los Pokémon disponibles con sus nombres, niveles y tipos.
2. **Creación de Pokémon**: Completa un formulario para agregar nuevos Pokémon (requiere autenticación).
3. **Edición de Pokémon**: Modifica la información de un Pokémon existente.
4. **Eliminación de Pokémon**: Borra un Pokémon de la lista.
5. **Autenticación de Usuarios**: Accede a funcionalidades avanzadas solo si estás autenticado.
6. **Paginación**: Navega entre las páginas de la lista de Pokémon.

---

## **Detener el Servidor**

### En Linux/Mac o Windows (CMD/PowerShell):
Para detener el servidor, usa **CTRL+C** en la terminal.

---

## **Desactivar el Entorno Virtual**

### En Linux/Mac o Windows (CMD/PowerShell):
```bash
deactivate
```

---

## **Notas Finales**
- Asegúrate de que el entorno virtual esté activo antes de realizar operaciones.
- Para agregar nuevas dependencias, actualiza **`requirements.txt`** con:
  ```bash
  pip freeze > requirements.txt
  ```

