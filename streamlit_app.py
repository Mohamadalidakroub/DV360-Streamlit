import streamlit as st
import pandas as pd

# Initialize session state
if "io_data" not in st.session_state: st.session_state.io_data = []
if "li_data" not in st.session_state: st.session_state.li_data = []
if "adgroup_data" not in st.session_state: st.session_state.adgroup_data = []
if "ad_data" not in st.session_state: st.session_state.ad_data = []

st.title("DV360 SDF Builder")

tabs = st.tabs(["Insertion Order", "Line Item", "Ad Group", "Ad"])

# --- Insertion Order Tab ---
with tabs[0]:
    with st.form("io_form"):
        st.subheader("Insertion Order")
        io_id = st.text_input("IO ID (Leave blank for new)")
        campaign_id = st.text_input("Campaign ID")
        name = st.text_input("Insertion Order Name")
        status = st.selectbox("Status", ["Active", "Paused", "Draft"])
        pacing = st.selectbox("Pacing", ["ASAP", "Even"])
        budget_type = st.selectbox("Budget Type", ["Fixed", "Unlimited"])
        pacing_rate = st.text_input("Pacing Rate")
        pacing_amount = st.text_input("Pacing Amount")

        submitted = st.form_submit_button("Add Insertion Order")
        if submitted:
            st.session_state.io_data.append({
                "Io Id": io_id,
                "Campaign Id": campaign_id,
                "Name": name,
                "Status": status,
                "Pacing": pacing,
                "Budget Type": budget_type,
                "Pacing Rate": pacing_rate,
                "Pacing Amount": pacing_amount
            })
            st.success("Insertion Order added!")

    if st.session_state.io_data:
        st.dataframe(pd.DataFrame(st.session_state.io_data))
        csv = pd.DataFrame(st.session_state.io_data).to_csv(index=False).encode('utf-8')
        st.download_button("Download IO CSV", csv, "InsertionOrder.csv", "text/csv")

# --- Line Item Tab ---
with tabs[1]:
    with st.form("li_form"):
        st.subheader("Line Item")
        li_id = st.text_input("Line Item ID")
        io_id = st.text_input("IO ID")
        li_name = st.text_input("Line Item Name")
        li_type = st.selectbox("Line Item Type", ["TrueView In-Stream", "Display", "Bumper", "App Install"])
        bid_strategy = st.text_input("Bid Strategy")
        budget = st.text_input("Budget")

        submitted = st.form_submit_button("Add Line Item")
        if submitted:
            st.session_state.li_data.append({
                "Line Item Id": li_id,
                "IO Id": io_id,
                "Line Item Name": li_name,
                "Type": li_type,
                "Bid Strategy": bid_strategy,
                "Budget": budget
            })
            st.success("Line Item added!")

    if st.session_state.li_data:
        st.dataframe(pd.DataFrame(st.session_state.li_data))
        csv = pd.DataFrame(st.session_state.li_data).to_csv(index=False).encode('utf-8')
        st.download_button("Download LI CSV", csv, "LineItem.csv", "text/csv")

# --- Ad Group Tab ---
with tabs[2]:
    with st.form("adgroup_form"):
        st.subheader("Ad Group")
        adgroup_id = st.text_input("Ad Group ID")
        li_id = st.text_input("Line Item ID")
        adgroup_name = st.text_input("Ad Group Name")
        rotation_type = st.selectbox("Rotation Type", ["Even", "Weighted", "Sequential"])

        submitted = st.form_submit_button("Add Ad Group")
        if submitted:
            st.session_state.adgroup_data.append({
                "Ad Group Id": adgroup_id,
                "Line Item Id": li_id,
                "Ad Group Name": adgroup_name,
                "Rotation Type": rotation_type
            })
            st.success("Ad Group added!")

    if st.session_state.adgroup_data:
        st.dataframe(pd.DataFrame(st.session_state.adgroup_data))
        csv = pd.DataFrame(st.session_state.adgroup_data).to_csv(index=False).encode('utf-8')
        st.download_button("Download Ad Group CSV", csv, "AdGroup.csv", "text/csv")

# --- Ad Tab ---
with tabs[3]:
    with st.form("ad_form"):
        st.subheader("Ad")
        ad_id = st.text_input("Ad ID")
        adgroup_id = st.text_input("Ad Group ID")
        ad_name = st.text_input("Ad Name")
        creative_id = st.text_input("Creative ID")
        final_url = st.text_input("Final URL")

        submitted = st.form_submit_button("Add Ad")
        if submitted:
            st.session_state.ad_data.append({
                "Ad Id": ad_id,
                "Ad Group Id": adgroup_id,
                "Ad Name": ad_name,
                "Creative Id": creative_id,
                "Final URL": final_url
            })
            st.success("Ad added!")

    if st.session_state.ad_data:
        st.dataframe(pd.DataFrame(st.session_state.ad_data))
        csv = pd.DataFrame(st.session_state.ad_data).to_csv(index=False).encode('utf-8')
        st.download_button("Download Ad CSV", csv, "Ad.csv", "text/csv")
