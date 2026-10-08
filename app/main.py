from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import Base, engine

# Models
from app.models.user import User
from app.models.category import Category
from app.models.topic import Topic

# Routers
from app.api.routes.users import router as users_router
from app.api.routes.categories import router as categories_router
from app.api.routes.topics import router as topics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Legal Learning Platform API",
    description="Backend API for legal education and judiciary awareness",
    version="1.0.0"
)

app.include_router(users_router)

app.include_router(categories_router)


app.include_router(topics_router)

@app.get("/")
def root():

    return {
        "message": "Legal Learning Platform Backend is running"
    }


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