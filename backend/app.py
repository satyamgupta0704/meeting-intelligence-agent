from fastapi import FastAPI

from database import SessionLocal
from models import Meeting

app = FastAPI()


@app.get("/meetings")
def get_meetings():

    db = SessionLocal()

    meetings = db.query(Meeting).all()

    result = []

    for m in meetings:

        result.append(
            {
                "id": m.id,
                "title": m.title,
                "company": m.company,
                "time": m.meeting_time,
                "brief": m.brief
            }
        )

    db.close()

    return result