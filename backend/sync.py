from backend.services.company_extractor import extract_company
from backend.integrations.google_calendar import (
    fetch_upcoming_meetings
)

from backend.services.company_extractor import (
    extract_company
)

from backend.services.db_service import save_meeting
from backend.services.research_service import (
    gather_company_research
)

from backend.services.brief_generator import (
    generate_brief
)


meetings = fetch_upcoming_meetings()

for meeting in meetings:

    info = extract_company(meeting)

    company = info["company"]

    domain = info["domain"]

    title = meeting.get("summary")

    attendees = meeting.get("attendees", [])

    meeting_time = (
        meeting["start"]
        .get("dateTime")
    )

    print(f"\nProcessing {title}")

    if not company:

        save_meeting(
            title,
            "Unknown",
            None,
            attendees,
            meeting_time,
            {
                "company_overview":
                "Company could not be identified."
            }
        )

        continue

    research = gather_company_research(
        company
    )

    brief = generate_brief(
        company,
        research
    )

    save_meeting(
        title,
        company,
        domain,
        attendees,
        meeting_time,
        brief
    )