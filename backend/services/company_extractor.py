import re
import json # Add this import so we can print pretty JSON

COMMON_DOMAINS = {
    "gmail",
    "yahoo",
    "hotmail",
    "outlook",
    "icloud"
}

def extract_company(event):
    attendees = event.get("attendees", [])

    for attendee in attendees:
        email = attendee.get("email", "")

        if "@" not in email:
            continue

        domain = email.split("@")[1]
        company_name = domain.split(".")[0]

        if company_name.lower() not in COMMON_DOMAINS:
            return {
                "company": company_name.title(),
                "domain": domain,
                "source": "email"
            }

    title = event.get("summary", "")

    if "with" in title.lower():
        company = title.lower().split("with")[-1].strip()
        return {
            "company": company.title(),
            "domain": None,
            "source": "title"
        }

    return {
        "company": None,
        "domain": None,
        "source": "fallback"
    }


# --- ADD THIS MAIN EXECUTION BLOCK TO TEST IT ---
if __name__ == '__main__':
    # 1. Create a mock Google Calendar event (simulating what the API gives us)
    # test_event = {
    #     "summary": "Architecture Review with Vercel",
    #     "attendees": [
    #         {"email": "fearless.satyam@gmail.com"},
    #         {"email": "engineer@vercel.com"}
    #     ]
    # }

    # 2. Run your extraction logic
    result = extract_company(test_event)

    # 3. Print the result as Plain Text (Python Dictionary)
    print("📋 PLAIN TEXT DICTIONARY:")
    print(result)
    print("\n" + "-"*40 + "\n")

    # 4. Print the result as beautifully formatted JSON
    print("🧩 FORMATTED JSON OUTPUT:")
    print(json.dumps(result, indent=2))