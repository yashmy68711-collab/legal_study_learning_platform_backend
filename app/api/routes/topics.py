from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.topic import Topic
from app.models.category import Category
from app.schemas.topic import TopicCreate, TopicResponse


router = APIRouter(
    prefix="/topics",
    tags=["Topics"]
)


# =========================================================
# CREATE TOPIC
# =========================================================

@router.post("/", response_model=TopicResponse, status_code=201)
def create_topic(
    topic: TopicCreate,
    db: Session = Depends(get_db)
):

    # Check whether category exists
    category = db.query(Category).filter(
        Category.id == topic.category_id
    ).first()

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    new_topic = Topic(
        title=topic.title,
        description=topic.description,
        category_id=topic.category_id
    )

    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)

    return new_topic


# =========================================================
# GET ALL TOPICS
# =========================================================

@router.get("/", response_model=list[TopicResponse])
def get_topics(
    db: Session = Depends(get_db)
):

    topics = db.query(Topic).all()

    return topics


# =========================================================
# GET TOPIC BY ID
# =========================================================

@router.get("/{topic_id}", response_model=TopicResponse)
def get_topic(
    topic_id: int,
    db: Session = Depends(get_db)
):

    topic = db.query(Topic).filter(
        Topic.id == topic_id
    ).first()

    if not topic:
        raise HTTPException(
            status_code=404,
            detail="Topic not found"
        )

    return topic