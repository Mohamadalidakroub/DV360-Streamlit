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
        st.subheader("Insertion Order (Full SDF Structure)")

        # BASIC INFO
        io_id = st.text_input("Io Id")
        campaign_id = st.text_input("Campaign Id")
        name = st.text_input("Name")
        timestamp = st.text_input("Timestamp", placeholder="2025-05-23T05:45:51.986000")
        status = st.selectbox("Status", ["Active", "Paused", "Draft"])
        io_type = st.text_input("Io Type", placeholder="Standard")
        io_subtype = st.text_input("Io Subtype", placeholder="Default")
        io_objective = st.text_input("Io Objective")

        # FEES / INTEGRATION
        fees = st.text_area("Fees")
        integration_code = st.text_input("Integration Code")
        details = st.text_area("Details")

        # PACING & FREQUENCY
        pacing = st.selectbox("Pacing", ["ASAP", "Even", "Flight", "Ahead"])
        pacing_rate = st.text_input("Pacing Rate")
        pacing_amount = st.text_input("Pacing Amount")
        freq_enabled = st.checkbox("Frequency Enabled")
        freq_exposures = st.text_input("Frequency Exposures") if freq_enabled else ""
        freq_period = st.text_input("Frequency Period") if freq_enabled else ""
        freq_amount = st.text_input("Frequency Amount") if freq_enabled else ""

        # KPI
        kpi_type = st.text_input("Kpi Type")
        kpi_value = st.text_input("Kpi Value")
        kpi_algorithm_id = st.text_input("Kpi Algorithm Id")

        # DAR
        measure_dar = st.checkbox("Measure DAR")
        measure_dar_channel = st.text_input("Measure DAR Channel")

        # BUDGET
        budget_type = st.selectbox("Budget Type", ["Amount", "Unlimited"])
        budget_segments_raw = st.text_area("Budget Segments", placeholder="(9308.0; 05/05/2025; 06/30/2025; ; ;)")

        auto_budget_allocation = st.checkbox("Auto Budget Allocation")

        # TARGETING - COMMON
        geo_include = st.text_area("Geography Targeting - Include", placeholder="DMA codes separated by ;")
        geo_exclude = st.text_area("Geography Targeting - Exclude")
        proximity_targeting = st.text_input("Proximity Targeting")
        proximity_location_list = st.text_input("Proximity Location List Targeting")
        language_include = st.text_area("Language Targeting - Include")
        language_exclude = st.text_area("Language Targeting - Exclude")
        device_include = st.text_area("Device Targeting - Include")
        device_exclude = st.text_area("Device Targeting - Exclude")

        # BRAND SAFETY
        digital_content_exclude = st.text_area("Digital Content Labels - Exclude")
        brand_safety_sensitivity = st.text_input("Brand Safety Sensitivity Setting")
        brand_safety_custom = st.text_area("Brand Safety Custom Settings")

        # VERIFICATION
        third_party_verification = st.text_input("Third Party Verification Services")
        third_party_labels = st.text_area("Third Party Verification Labels")

        # AUDIENCE & INVENTORY
        audience_include = st.text_area("Audience Targeting - Include")
        audience_exclude = st.text_area("Audience Targeting - Exclude")
        affinity_include = st.text_area("Affinity & In Market Targeting - Include")
        affinity_exclude = st.text_area("Affinity & In Market Targeting - Exclude")
        custom_list = st.text_input("Custom List Targeting")
        inventory_auth_sellers = st.selectbox("Inventory Source Targeting - Authorized Seller Options", [
            "All", "Authorized Direct Sellers Only", "Authorized Direct Sellers And Resellers"
        ])
        inventory_include = st.text_area("Inventory Source Targeting - Include")
        inventory_exclude = st.text_area("Inventory Source Targeting - Exclude")
        inventory_target_new_exchanges = st.checkbox("Inventory Source Targeting - Target New Exchanges")

        # FLOOR PRICE
        apply_floor_price = st.checkbox("Apply Floor Price For Deals")
        bid_strategy_unit = st.text_input("Bid Strategy Unit")
        bid_strategy_cap = st.text_input("Bid Strategy Do Not Exceed")
        algorithm_id = st.text_input("Algorithm Id")

        submitted = st.form_submit_button("Add Insertion Order")
        if submitted:
            st.session_state.io_data.append({
                "Io Id": io_id,
                "Campaign Id": campaign_id,
                "Name": name,
                "Timestamp": timestamp,
                "Status": status,
                "Io Type": io_type,
                "Io Subtype": io_subtype,
                "Io Objective": io_objective,
                "Fees": fees,
                "Integration Code": integration_code,
                "Details": details,
                "Pacing": pacing,
                "Pacing Rate": pacing_rate,
                "Pacing Amount": pacing_amount,
                "Frequency Enabled": freq_enabled,
                "Frequency Exposures": freq_exposures,
                "Frequency Period": freq_period,
                "Frequency Amount": freq_amount,
                "Kpi Type": kpi_type,
                "Kpi Value": kpi_value,
                "Kpi Algorithm Id": kpi_algorithm_id,
                "Measure DAR": measure_dar,
                "Measure DAR Channel": measure_dar_channel,
                "Budget Type": budget_type,
                "Budget Segments": budget_segments_raw,
                "Auto Budget Allocation": auto_budget_allocation,
                "Geography Targeting - Include": geo_include,
                "Geography Targeting - Exclude": geo_exclude,
                "Proximity Targeting": proximity_targeting,
                "Proximity Location List Targeting": proximity_location_list,
                "Language Targeting - Include": language_include,
                "Language Targeting - Exclude": language_exclude,
                "Device Targeting - Include": device_include,
                "Device Targeting - Exclude": device_exclude,
                "Digital Content Labels - Exclude": digital_content_exclude,
                "Brand Safety Sensitivity Setting": brand_safety_sensitivity,
                "Brand Safety Custom Settings": brand_safety_custom,
                "Third Party Verification Services": third_party_verification,
                "Third Party Verification Labels": third_party_labels,
                "Audience Targeting - Include": audience_include,
                "Audience Targeting - Exclude": audience_exclude,
                "Affinity & In Market Targeting - Include": affinity_include,
                "Affinity & In Market Targeting - Exclude": affinity_exclude,
                "Custom List Targeting": custom_list,
                "Inventory Source Targeting - Authorized Seller Options": inventory_auth_sellers,
                "Inventory Source Targeting - Include": inventory_include,
                "Inventory Source Targeting - Exclude": inventory_exclude,
                "Inventory Source Targeting - Target New Exchanges": inventory_target_new_exchanges,
                "Apply Floor Price For Deals": apply_floor_price,
                "Bid Strategy Unit": bid_strategy_unit,
                "Bid Strategy Do Not Exceed": bid_strategy_cap,
                "Algorithm Id": algorithm_id
            })
            st.success("Insertion Order added!")

    if st.session_state.io_data:
        st.subheader("Preview IO Sheet")
        io_df = pd.DataFrame(st.session_state.io_data)
        st.dataframe(io_df)
        csv = io_df.to_csv(index=False).encode('utf-8')
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
