# Explorador Cósmico

Una aplicación web educativa en español sobre el origen del universo con autenticación de usuarios, base de datos PostgreSQL y contenido multimedia construida con Flask.

## Descripción

El Explorador Cósmico es una plataforma educativa interactiva diseñada para explorar los misterios del origen del universo. Esta aplicación ofrece contenido detallado sobre el Big Bang, teorías científicas alternativas y perspectivas cosmológicas diversas.

### Características principales

- **Autenticación completa**: Sistema de registro e inicio de sesión de usuarios
- **Diseño responsivo**: Experiencia optimizada en dispositivos móviles y de escritorio
- **Contenido multimedia**: Videos, imágenes y líneas de tiempo interactivas
- **Animaciones**: Efectos visuales como fondos de estrellas y elementos flotantes
- **Base de datos**: Almacenamiento seguro de datos de usuarios

## Tecnologías utilizadas

- **Backend**: Flask (Python)
- **Base de datos**: SQLite (en producción) / PostgreSQL (opcional para desarrollo)
- **Autenticación**: Flask-Login
- **Formularios**: Flask-WTF
- **Frontend**: HTML, CSS, JavaScript
- **Estilos**: Tailwind CSS
- **Iconos**: Font Awesome

## Estructura del proyecto

```
explorador-cosmico/
├── app.py                # Configuración principal de la aplicación
├── main.py               # Punto de entrada
├── models.py             # Modelos de datos (SQLAlchemy)
├── forms.py              # Formularios de la aplicación
├── routes.py             # Rutas y controladores
├── static/               # Archivos estáticos
│   ├── css/              # Hojas de estilo
│   └── js/               # Scripts JavaScript
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página principal
│   ├── login.html        # Página de inicio de sesión
│   ├── register.html     # Página de registro
│   ├── dashboard.html    # Panel principal
│   └── sections/         # Secciones de contenido
├── render.yaml           # Configuración de despliegue para Render
├── Procfile              # Comandos de inicio para servidores
└── runtime.txt           # Versión de Python especificada
```

## Secciones de contenido

1. **El Big Bang**: Explicación detallada del modelo cosmológico estándar
2. **Teorías Científicas**: Exploración de teorías alternativas y complementarias
3. **Conspiraciones Cósmicas**: Análisis de perspectivas no convencionales

## Despliegue en Render.com

Esta aplicación está configurada para ser desplegada fácilmente en Render.com a través del sistema Blueprint.

### Requisitos previos

- Cuenta en [Render.com](https://render.com)
- Repositorio de código en GitHub, GitLab o Bitbucket

### Pasos para el despliegue

1. **Clona este repositorio** y súbelo a tu cuenta de GitHub/GitLab/Bitbucket.

2. **Accede a Render.com** y crea una cuenta o inicia sesión.

3. **Método con Web Services (recomendado para plan gratuito)**:
   - En el dashboard de Render, selecciona "New" → "Web Service".
   - Conecta tu repositorio de GitHub/GitLab.
   - Configura el nombre como "explorador-cosmico" (o el que prefieras).
   - Asegúrate de que el entorno sea "Python".
   - En la sección de Build Command, ingresa: `pip install .`.
   - En Start Command, ingresa: `gunicorn --bind 0.0.0.0:$PORT --reuse-port main:app`.
   - Selecciona el plan "Free".
   - Haz clic en "Create Web Service".

4. **Espera a que se complete el despliegue** (puede tomar unos minutos).

5. **Accede a tu aplicación** mediante la URL proporcionada por Render:
   - `https://explorador-cosmico.onrender.com` (o la URL asignada)

### Variables de entorno importantes

Cuando se despliega en Render, es recomendable configurar estas variables de entorno:

- `SESSION_SECRET`: Clave secreta para las sesiones (Render puede generar una automáticamente)
- `PYTHON_VERSION`: Establecida a "3.11.3" (o la versión que prefieras)

La aplicación está configurada para usar SQLite por defecto, por lo que no se requiere configuración adicional de base de datos.

## Desarrollo local

### Requisitos previos

- Python 3.11 o superior

### Configuración

1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd explorador-cosmico
   ```

2. Instala las dependencias:
   ```
   pip install .
   ```

3. Variables de entorno (opcionales):
   - `SESSION_SECRET`: Clave secreta para la sesión
   - Por defecto, la aplicación usará SQLite sin necesidad de configuración adicional

4. Inicia la aplicación:
   ```
   gunicorn --bind 0.0.0.0:5000 --reuse-port main:app
   ```

5. Accede a la aplicación en tu navegador:
   ```
   http://localhost:5000
   ```

## Licencia

Este proyecto está bajo licencia MIT - consulta el archivo LICENSE para más detalles.
