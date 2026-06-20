import json

from streamlit import title

from backend.database import SessionLocal
from backend.models import Meeting


def save_meeting(
    title,
    company,
    domain,
    attendees,
    meeting_time,
    brief
):

    print("Saving meeting...")
    print(title)
    print(company)

    db = SessionLocal()

    if isinstance(brief, str):

        try:
            brief = json.loads(brief)
        except:
            pass

    existing = db.query(Meeting).filter(
        Meeting.title == title,
        Meeting.meeting_time == meeting_time
    ).first()

    if existing:

        existing.brief = json.dumps(brief)

        db.commit()

        db.close()

        return

    meeting = Meeting(
        title=title,
        company=company,
        domain=domain,
        attendees=json.dumps(attendees),
        meeting_time=meeting_time,
        brief=json.dumps(brief)
    )

    db.add(meeting)

    db.commit()

    db.close()