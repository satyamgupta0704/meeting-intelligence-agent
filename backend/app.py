from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.database import SessionLocal, engine
from backend.models import Base, Meeting


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database ready.")

    yield


app = FastAPI(
    title="Meeting Intelligence Agent",
    lifespan=lifespan
)


@app.get("/")
def root():

    return {
        "status": "running",
        "message": "Meeting Intelligence Agent API"
    }


@app.get("/meetings")
def get_meetings():

    db = SessionLocal()

    try:

        meetings = db.query(Meeting).all()

        result = []

        for m in meetings:

            result.append(
                {
                    "id": m.id,
                    "title": m.title,
                    "company": m.company,
                    "domain": m.domain,
                    "attendees": m.attendees,
                    "time": m.meeting_time,
                    "brief": m.brief
                }
            )

        return result

    finally:

        db.close()


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }