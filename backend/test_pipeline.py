# Note the updated import name here: google_calendar
from integrations.google_calendar import fetch_upcoming_meetings
from services.company_extractor import extract_company

if __name__ == '__main__':
    print("Fetching live meetings and extracting companies...\n")
    
    # 1. Get the live data from Google
    meetings = fetch_upcoming_meetings()

    if not meetings:
        print("No upcoming meetings found.")
    else:
        # 2. Loop through and process each one
        for meeting in meetings:
            # Skip automatic birthdays to keep the output clean
            if "birthday" in meeting.get('summary', '').lower():
                continue
                
            result = extract_company(meeting)

            print(f"Meeting: {meeting.get('summary', 'No Title')}")
            print(f"Extracted: {result}")
            print("-" * 50)