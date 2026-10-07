# Legal Study Learning Platform – Backend

Backend API for a Legal Study Learning Platform built using **Python and FastAPI**.

The backend provides APIs for user authentication, legal categories, legal topics, database operations, and secure user access using JWT authentication.

---

## 🚀 Technologies Used

- **Python**
- **FastAPI** – Backend API framework
- **Uvicorn** – ASGI server
- **SQLAlchemy** – ORM for database operations
- **SQLite** – Database
- **Pydantic** – Data validation and schemas
- **JWT (JSON Web Token)** – Authentication
- **Password Hashing** – Secure password storage
- **python-dotenv** – Environment variable management
- **Git & GitHub** – Version control and project management
- **Swagger UI** – API testing and documentation

---

## 🔐 Authentication

The backend includes a complete basic authentication system.

Implemented features:

- User registration
- Email duplication checking
- Password hashing
- User login
- Password verification
- JWT access token generation
- JWT token verification
- Protected current-user endpoint
- Get user by ID
- Get all users

### Authentication Flow

```text
Register
   ↓
Password Hashing
   ↓
Database
   ↓
Login
   ↓
Password Verification
   ↓
JWT Access Token
   ↓
Authenticated API Requests
