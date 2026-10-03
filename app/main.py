from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import Base, engine
from app.models.user import User
from app.api.users import router as users_router


# =========================================================
# CREATE DATABASE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="Legal Learning Platform API",
    description="Backend API for legal education and judiciary awareness",
    version="1.0.0"
)


# =========================================================
# USERS ROUTER
# =========================================================

app.include_router(users_router)


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():

    return {
        "message": "Legal Learning Platform Backend is running"
    }


# =========================================================
# DATABASE TEST
# =========================================================

@app.get("/db-test")
def db_test():

    try:

        with engine.connect() as connection:

            connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "message": "Database connection successful!"
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }