# 💇‍♂️ Haircut Scheduler

Haircut Scheduler is a RESTful backend application for managing appointments in barbershops. It allows customers to book time slots, barbers to manage their schedules, and provides a solid API to integrate with a modern React frontend.

---

## 🚀 Features

- 🔐 JWT-based user authentication (Barbers & Customers)
- 📅 Appointment booking with time conflict prevention
- 👤 Barber profile management (services, working hours, etc.)
- 📊 Admin panel for managing users & bookings
- 🌐 Ready for frontend integration via clean JSON APIs
- 🐳 Dockerized for easy deployment

---

## 🛠️ Tech Stack

- **Backend:** Django + Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Auth:** JWT via SimpleJWT (planned)
- **Environment:** Python `venv` + `.env` config
- **Containerization:** Docker & Docker Compose

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/haircut-scheduler.git
cd haircut-scheduler
```

### 2. Create `.env` file inside `backend/`

```ini
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_NAME=haircut_db
DATABASE_USER=haircut_user
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=db
DATABASE_PORT=5432
```

### 3. Build and Run with Docker

```bash
docker-compose up --build
```

> The app will run at: [http://localhost:8000](http://localhost:8000)

---

## 📁 Project Structure

```
haircut-scheduler/
├── backend/
│   ├── accounts/         # User logic (barbers & customers)
│   ├── appointments/     # Appointment booking
│   ├── core/             # Project settings
│   ├── manage.py
│   ├── requirements.txt
│   └── .env              # Environment variables
├── docker/
│   └── docker-compose.yml
└── README.md
```

---

## 🔓 API Endpoints (Coming Soon)

| Endpoint                  | Method | Description                       |
|--------------------------|--------|-----------------------------------|
| `/api/auth/register/`    | POST   | User registration                 |
| `/api/auth/login/`       | POST   | JWT login                         |
| `/api/barbers/`          | GET    | List barbers                      |
| `/api/appointments/`     | POST   | Book appointment                  |
| `/api/appointments/my/`  | GET    | View user's bookings              |


---

## 📘 API Documentation

This project uses **Swagger UI** (via [`drf-yasg`](https://github.com/axnsan12/drf-yasg)) for interactive API documentation.

After running the backend server, visit the following URLs:

- 🌀 **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- 📘 **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- 📄 **Schema JSON:** [http://localhost:8000/swagger.json](http://localhost:8000/swagger.json)
- 📄 **Schema YAML:** [http://localhost:8000/swagger.yaml](http://localhost:8000/swagger.yaml)

---

## 🤝 Contributors

- Backend: [Amir](https://github.com/amiradmin/haircut-scheduler.git)
- Frontend: Hussein (React)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).