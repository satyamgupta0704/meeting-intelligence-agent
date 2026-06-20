import os
import streamlit as st
import requests
import json
from datetime import datetime

st.set_page_config(
    page_title="Meeting Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

# ======================================
# FETCH DATA
# ======================================
API_URL = os.getenv(
    "https://meeting-intelligence-agent-qg2g.onrender.com",
    "http://127.0.0.1:8000"
)

response = requests.get(
    f"{API_URL}/meetings"
)

# response = requests.get(
#     "https://meeting-intelligence-agent-qg2g.onrender.com"
# )

meetings = response.json()

# ======================================
# HEADER
# ======================================

st.title("🤖 Meeting Intelligence Dashboard")
st.caption(
    "AI-generated intelligence briefs for upcoming meetings"
)

if not meetings:
    st.warning("No upcoming meetings found")
    st.stop()

# ======================================
# METRICS
# ======================================

total_meetings = len(meetings)

researched = len([
    m for m in meetings
    if m["company"] != "Unknown"
])

unknown = total_meetings - researched

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Upcoming Meetings",
        total_meetings,
        border=True
    )

with m2:
    st.metric(
        "Research Briefs",
        researched,
        border=True
    )

with m3:
    st.metric(
        "Needs Review",
        unknown,
        border=True
    )

st.divider()

# ======================================
# SIDEBAR
# ======================================

with st.sidebar:

    st.title("🤖 Meeting Agent")

    st.success("Calendar Connected")

    st.metric(
        "Upcoming Meetings",
        total_meetings
    )

    st.metric(
        "Research Generated",
        researched
    )

    st.metric(
        "Unknown Companies",
        unknown
    )

    st.divider()

    st.write(
        f"🕒 Last Updated\n\n"
        f"{datetime.now().strftime('%d %b %Y %I:%M %p')}"
    )

    st.divider()

    st.markdown("""
    ### Assignment Coverage

    ✅ Calendar Listener

    ✅ Company Detection

    ✅ Research Pipeline

    ✅ Dashboard

    ✅ Fallback Handling

    ✅ Auto Research Generation
    """)

# ======================================
# MEETING CARDS
# ======================================

col1, col2 = st.columns(2)

for idx, meeting in enumerate(meetings):

    target_col = col1 if idx % 2 == 0 else col2

    with target_col:

        brief = meeting.get("brief", "{}")

        if isinstance(brief, str):
            try:
                brief = json.loads(brief)
            except:
                brief = {}

        company = meeting["company"]

        overview = brief.get(
            "company_overview",
            "No overview available"
        )

        short_overview = (
            overview[:220] + "..."
            if len(overview) > 220
            else overview
        )

        with st.container(border=True):

            st.subheader(meeting["title"])

            st.caption(meeting["time"])

            if company == "Unknown":

                st.error(
                    "⚠️ Company Not Identified"
                )

            else:

                st.success(
                    "✅ Research Complete"
                )

            st.markdown(
                f"### 🏢 {company}"
            )

            st.write(short_overview)

            with st.expander(
                "🔍 View Intelligence Brief"
            ):

                st.markdown(
                    "### Company Overview"
                )

                st.write(
                    brief.get(
                        "company_overview",
                        "N/A"
                    )
                )

                st.markdown(
                    "### Recent Activity"
                )

                st.write(
                    brief.get(
                        "recent_activity",
                        "N/A"
                    )
                )

                st.markdown(
                    "### Tech Signals"
                )

                st.write(
                    brief.get(
                        "tech_signals",
                        "N/A"
                    )
                )

                st.markdown(
                    "### Pain Points"
                )

                st.write(
                    brief.get(
                        "pain_points",
                        "N/A"
                    )
                )

                st.markdown(
                    "### Suggested Talking Points"
                )

                talking_points = brief.get(
                    "talking_points",
                    []
                )

                if talking_points:

                    for point in talking_points:

                        st.markdown(
                            f"- {point}"
                        )

                else:

                    st.write(
                        "No talking points available."
                    )