# 💼 BTG Pactual - Plataforma de Suscripción a Fondos

Este es un proyecto **backend** desarrollado como parte de una prueba técnica para **BTG Pactual**, que permite a los usuarios gestionar sus fondos de inversión. Incluye funcionalidades como la suscripción a fondos, cancelación, historial de transacciones y notificaciones por email o SMS.

---

## 🧩 Funcionalidades Implementadas

-  **Suscribirse a un fondo**: Validación de saldo suficiente y deducción del monto.
-  **Cancelar una suscripción**: Reembolso del monto al usuario.
-  **Ver historial de transacciones**: Listado de todas las operaciones realizadas.
-  **Notificaciones**: Email o SMS según preferencia del usuario.

---

## 🛠️ Tecnologías Utilizadas

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) (Python)

### Base de Datos
- MongoDB (NoSQL)

### Notificaciones
- Simulación con `print()` (se puede integrar con Twilio/SendGrid)

### Despliegue
- Docker
- AWS CloudFormation

### Pruebas
- `pytest`

### Seguridad
- JWT (básico)

---

## 🗂️ Estructura del Proyecto

```
btg_pactual/
├── app/                # Código fuente
│   ├── main.py         # Punto de entrada de FastAPI
│   ├── models/         # Modelos de datos
│   ├── routes/         # Rutas de la API
│   ├── services/       # Lógica de negocio
│   ├── database/       # Configuración de conexión a DB
│   └── utils/          # Utilidades (notificaciones)
├── tests/              # Pruebas unitarias
├── requirements.txt    # Dependencias
├── Dockerfile          # Contenerización
├── README.md           # Este archivo
└── template.yaml       # Plantilla de CloudFormation
```

---

## 🚀 Cómo Ejecutar el Proyecto Localmente

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/btg-pactual.git
cd btg-pactual
```

### 2. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 3. Levanta el servidor local

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Cómo Ejecutar con Docker

```bash
docker build -t btg-pactual .
docker run -d -p 8000:80 btg-pactual
```

---

## 📤 Despliegue en AWS (CloudFormation)

Puedes desplegar este proyecto usando la plantilla `template.yaml` con AWS SAM CLI:

```bash
sam build
sam deploy --guided
```

---

## ✅ Ejemplo de Uso de la API

### Suscribirse a un fondo

```http
POST /subscribe/1?user_id=123
```

### Cancelar una suscripción

```http
POST /unsubscribe/{subscription_id}?user_id=123
```

---

## 🧪 Pruebas Unitarias

Ejecuta las pruebas con:

```bash
pytest tests/
```

---

## 🔐 Autenticación (JWT Básico)

Incluye un ejemplo básico de autenticación JWT. Puede extenderse fácilmente para proteger endpoints.

---

## 📬 Notificaciones Personalizadas

Actualmente se simulan con `print()`, pero pueden integrarse con servicios reales como:

- **Email**: [SendGrid](https://sendgrid.com/)
- **SMS**: [Twilio](https://www.twilio.com/)

---

## 📁 Base de Datos (MongoDB)

Asegúrate de tener MongoDB instalado localmente o usar un contenedor:

```bash
docker run -d -p 27017:27017 mongo
```

Configura la URL de conexión en `app/database/db.py`.

---

## 📎 Pendientes y Mejoras Futuras

- Integración real con email/SMS.
- Logs estructurados y monitoreo.
- CI/CD con GitHub Actions.
- Pruebas de estrés y seguridad.
- Soporte multi-tenant y más roles.

---

## 👥 Autor

**Tu Nombre**  
📧 mapacv26@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mariapaulacanas/)
