import streamlit as st
from datetime import date, datetime
import json

st.set_page_config(page_title="DV360 Campaign Builder", layout="centered")
st.title("🎯 DV360 Campaign Builder - Mock (Offline)")

# Partner & Advertiser
st.header("1️⃣ Partner & Advertiser Setup")
partner_id = st.text_input("Partner ID", placeholder="e.g. 123456")
advertiser_name = st.text_input("Advertiser Name", placeholder="e.g. Coca-Cola MENA")
advertiser_status = st.selectbox("Advertiser Status", ["ENTITY_STATUS_ACTIVE", "ENTITY_STATUS_INACTIVE"])

# Campaign
st.header("2️⃣ Campaign Setup")
campaign_name = st.text_input("Campaign Name", placeholder="e.g. Awareness Ramadan")
campaign_status = st.selectbox("Campaign Status", ["ENTITY_STATUS_ACTIVE", "ENTITY_STATUS_PAUSED", "ENTITY_STATUS_DRAFT"])
goal_type = st.selectbox("Campaign Goal Type", ["BRAND_AWARENESS", "INCREASE_REACH", "DRIVE_ONLINE_ACTIONS"])
start_date = st.date_input("Campaign Start Date", value=date.today())
end_date = st.date_input("Campaign End Date", value=date.today())
frequency_cap = st.number_input("Max Impressions per Day", min_value=1, value=3)
campaign_budget_usd = st.number_input("Total Campaign Budget (USD)", step=100.0)
campaign_budget_micros = int(campaign_budget_usd * 1_000_000)

# Insertion Order
st.header("3️⃣ Insertion Order Setup")
io_name = st.text_input("Insertion Order Name", placeholder="e.g. IO - May Flight")
io_status = st.selectbox("Insertion Order Status", ["ENTITY_STATUS_ACTIVE", "ENTITY_STATUS_PAUSED", "ENTITY_STATUS_DRAFT"])
io_start_date = st.date_input("IO Start Date", value=start_date)
io_end_date = st.date_input("IO End Date", value=end_date)
io_budget_usd = st.number_input("IO Budget (USD)", step=100.0)
io_budget_micros = int(io_budget_usd * 1_000_000)
pacing_type = st.selectbox("Pacing Type", ["PACING_TYPE_EVEN", "PACING_TYPE_AHEAD", "PACING_TYPE_AS_FAST_AS_POSSIBLE"])
daily_pacing_usd = st.number_input("Daily Max Spend (USD)", step=10.0)
daily_pacing_micros = int(daily_pacing_usd * 1_000_000)

# Line Item
st.header("4️⃣ Line Item Setup")
li_name = st.text_input("Line Item Name", placeholder="e.g. Video Line Item 1")
li_type = st.selectbox("Line Item Type", ["LINE_ITEM_TYPE_DISPLAY_DEFAULT", "LINE_ITEM_TYPE_VIDEO_DEFAULT"])
li_status = st.selectbox("Line Item Status", ["ENTITY_STATUS_ACTIVE", "ENTITY_STATUS_PAUSED", "ENTITY_STATUS_DRAFT"])
li_start_date = st.date_input("Line Item Start Date", value=io_start_date)
li_end_date = st.date_input("Line Item End Date", value=io_end_date)
li_budget_usd = st.number_input("Line Item Budget (USD)", step=100.0)
li_budget_micros = int(li_budget_usd * 1_000_000)
bid_usd = st.number_input("Bid Amount (USD)", step=0.1)
bid_micros = int(bid_usd * 1_000_000)

# Targeting
st.header("5️⃣ Targeting Options")
geo = st.text_input("Geo Locations (comma-separated country codes)", "SA,AE")
device = st.text_input("Devices (comma-separated)", "Mobile,Desktop")
language = st.text_input("Languages (comma-separated)", "en,ar")

# Creative
st.header("6️⃣ Creative Info")
creative_name = st.text_input("Creative Name")
youtube_video_id = st.text_input("YouTube Video ID (e.g. dQw4w9WgXcQ)")
landing_page_url = st.text_input("Landing Page URL (e.g. https://www.brand.com)")

# Submit
if st.button("✅ Simulate Full DV360 Payload"):
    payload = {
        "partner_id": partner_id.strip(),
        "advertiser": {
            "displayName": advertiser_name.strip(),
            "entityStatus": advertiser_status
        },
        "campaign": {
            "displayName": campaign_name.strip(),
            "entityStatus": campaign_status,
            "campaignGoal": {
                "campaignGoalType": goal_type
            },
            "flight": {
                "plannedStartDate": str(start_date),
                "plannedEndDate": str(end_date)
            },
            "frequencyCap": {
                "maxImpressions": int(frequency_cap),
                "timeUnit": "TIME_UNIT_DAYS",
                "timeUnitCount": 1
            },
            "budget": {
                "budgetAmountMicros": campaign_budget_micros,
                "budgetUnit": "BUDGET_UNIT_CURRENCY"
            }
        },
        "insertion_order": {
            "displayName": io_name.strip(),
            "entityStatus": io_status,
            "budget": {
                "budgetSegments": [
                    {
                        "budgetAmountMicros": io_budget_micros,
                        "dateRange": {
                            "startDate": str(io_start_date),
                            "endDate": str(io_end_date)
                        }
                    }
                ]
            },
            "pacing": {
                "pacingPeriod": "PACING_PERIOD_DAILY",
                "pacingType": pacing_type,
                "dailyMaxMicros": daily_pacing_micros
            }
        },
        "line_item": {
            "displayName": li_name.strip(),
            "lineItemType": li_type,
            "entityStatus": li_status,
            "flight": {
                "flightDateType": "LINE_ITEM_FLIGHT_DATE_TYPE_CUSTOM",
                "dateRange": {
                    "startDate": str(li_start_date),
                    "endDate": str(li_end_date)
                }
            },
            "budget": {
                "budgetAllocationType": "BUDGET_ALLOCATION_TYPE_FIXED",
                "budgetUnit": "BUDGET_UNIT_CURRENCY",
                "budgetAmountMicros": li_budget_micros
            },
            "bidStrategy": {
                "fixedBid": {
                    "bidAmountMicros": bid_micros
                }
            },
            "targeting": {
                "geo": [g.strip() for g in geo.split(',')],
                "device": [d.strip() for d in device.split(',')],
                "language": [l.strip() for l in language.split(',')]
            }
        },
        "creative": {
            "displayName": creative_name.strip(),
            "youtubeVideoId": youtube_video_id.strip(),
            "landingPageUrl": landing_page_url.strip()
        }
    }

    filename = f"dv360_full_payload_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(filename, 'w') as f:
        json.dump(payload, f, indent=2)

    st.success("✅ Payload created and saved successfully!")
    st.subheader("Simulated DV360 API Payload")
    st.json(payload)
    st.caption(f"📁 Saved to file: `{filename}`")
