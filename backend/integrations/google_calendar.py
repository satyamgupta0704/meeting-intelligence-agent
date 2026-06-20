import json
import os
from datetime import datetime, UTC
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_service():
    creds = None
    
    # Dynamically find the backend/ folder where credentials.json lives
    script_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.dirname(script_dir)
    
    credentials_path = os.path.join(backend_dir, "credentials.json")
    token_path = os.path.join(backend_dir, "token.json")

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(
            token_path,
            SCOPES
        )

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_path, 
            SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open(token_path, "w") as token:
            token.write(creds.to_json())

    return build(
        "calendar",
        "v3",
        credentials=creds
    )

def fetch_upcoming_meetings():

    service = get_calendar_service()

    now = datetime.now(UTC).isoformat()

    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=50,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    meetings = []

    for event in events:

        # Skip birthdays
        if event.get("eventType") == "birthday":
            continue

        meetings.append(event)

    return meetings


# --- THE MAIN EXECUTION BLOCK ---
# if __name__ == '__main__':
#     print("Fetching your upcoming meetings...")
#     meetings = fetch_upcoming_meetings()
    
#     if not meetings:
#         print("No upcoming meetings found.")
#     else:
#         for event in meetings:
#             # Handle both timed events (dateTime) and all-day events (date)
#             start = event['start'].get('dateTime', event['start'].get('date'))
#             print(f"[{start}] {event['summary']}")

# if __name__ == '__main__':
#     print("Fetching your raw upcoming meetings JSON...")
#     meetings = fetch_upcoming_meetings()
    
#     if not meetings:
#         print("No upcoming meetings found.")
#     else:
#         # This will print the raw list of meetings as clean JSON
#         print(json.dumps(meetings[:2], indent=2))