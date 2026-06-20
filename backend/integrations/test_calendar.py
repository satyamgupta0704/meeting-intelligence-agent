from integrations.google_calendar import fetch_upcoming_meetings
import json

meetings = fetch_upcoming_meetings()

print(
    json.dumps(
        meetings,
        indent=2
    )
)