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
    st.subheader("Edit or Duplicate an Existing Insertion Order")

    # Dropdown to select an existing IO
    io_options = [f"{i} - {d['Name']}" for i, d in enumerate(st.session_state.io_data)]
    selected_index = st.selectbox("Select an IO to Edit/Duplicate", ["-- None --"] + io_options)

    edit_data = {}
    idx = None
    if selected_index != "-- None --":
        idx = int(selected_index.split(" - ")[0])
        edit_data = st.session_state.io_data[idx]

    duplicate_mode = st.checkbox("Save as new (duplicate entry)")

    with st.form("io_form"):
        st.subheader("Insertion Order (Full SDF Structure)")

        # BASIC INFO
        io_id = st.text_input("Io Id", value=edit_data.get("Io Id", ""))
        campaign_id = st.text_input("Campaign Id", value=edit_data.get("Campaign Id", ""))
        name = st.text_input("Name", value=edit_data.get("Name", ""))
        timestamp = st.text_input("Timestamp", value=edit_data.get("Timestamp", ""))
        status = st.selectbox("Status", ["Active", "Paused", "Draft"], index=["Active", "Paused", "Draft"].index(edit_data.get("Status", "Paused")))
        io_type = st.text_input("Io Type", value=edit_data.get("Io Type", ""))
        io_subtype = st.text_input("Io Subtype", value=edit_data.get("Io Subtype", ""))
        io_objective = st.text_input("Io Objective", value=edit_data.get("Io Objective", ""))

        # FEES / INTEGRATION
        fees = st.text_area("Fees", value=edit_data.get("Fees", ""))
        integration_code = st.text_input("Integration Code", value=edit_data.get("Integration Code", ""))
        details = st.text_area("Details", value=edit_data.get("Details", ""))

        # PACING & FREQUENCY
        pacing = st.selectbox("Pacing", ["ASAP", "Even", "Flight", "Ahead"], index=["ASAP", "Even", "Flight", "Ahead"].index(edit_data.get("Pacing", "Flight")))
        pacing_rate = st.text_input("Pacing Rate", value=edit_data.get("Pacing Rate", ""))
        pacing_amount = st.text_input("Pacing Amount", value=edit_data.get("Pacing Amount", ""))
        freq_enabled = st.checkbox("Frequency Enabled", value=edit_data.get("Frequency Enabled", False))
        freq_exposures = st.text_input("Frequency Exposures", value=edit_data.get("Frequency Exposures", "")) if freq_enabled else ""
        freq_period = st.text_input("Frequency Period", value=edit_data.get("Frequency Period", "")) if freq_enabled else ""
        freq_amount = st.text_input("Frequency Amount", value=edit_data.get("Frequency Amount", "")) if freq_enabled else ""

        # KPI
        kpi_type = st.text_input("Kpi Type", value=edit_data.get("Kpi Type", ""))
        kpi_value = st.text_input("Kpi Value", value=edit_data.get("Kpi Value", ""))
        kpi_algorithm_id = st.text_input("Kpi Algorithm Id", value=edit_data.get("Kpi Algorithm Id", ""))

        # DAR
        measure_dar = st.checkbox("Measure DAR", value=edit_data.get("Measure DAR", False))
        measure_dar_channel = st.text_input("Measure DAR Channel", value=edit_data.get("Measure DAR Channel", ""))

        # BUDGET
        budget_type = st.selectbox("Budget Type", ["Amount", "Unlimited"], index=["Amount", "Unlimited"].index(edit_data.get("Budget Type", "Amount")))
        budget_segments_raw = st.text_area("Budget Segments", value=edit_data.get("Budget Segments", ""))
        auto_budget_allocation = st.checkbox("Auto Budget Allocation", value=edit_data.get("Auto Budget Allocation", False))

        # TARGETING - COMMON
        geo_include = st.text_area("Geography Targeting - Include", value=edit_data.get("Geography Targeting - Include", ""))
        geo_exclude = st.text_area("Geography Targeting - Exclude", value=edit_data.get("Geography Targeting - Exclude", ""))
        proximity_targeting = st.text_input("Proximity Targeting", value=edit_data.get("Proximity Targeting", ""))
        proximity_location_list = st.text_input("Proximity Location List Targeting", value=edit_data.get("Proximity Location List Targeting", ""))
        language_include = st.text_area("Language Targeting - Include", value=edit_data.get("Language Targeting - Include", ""))
        language_exclude = st.text_area("Language Targeting - Exclude", value=edit_data.get("Language Targeting - Exclude", ""))
        device_include = st.text_area("Device Targeting - Include", value=edit_data.get("Device Targeting - Include", ""))
        device_exclude = st.text_area("Device Targeting - Exclude", value=edit_data.get("Device Targeting - Exclude", ""))

        # BRAND SAFETY
        digital_content_exclude = st.text_area("Digital Content Labels - Exclude", value=edit_data.get("Digital Content Labels - Exclude", ""))
        brand_safety_sensitivity = st.text_input("Brand Safety Sensitivity Setting", value=edit_data.get("Brand Safety Sensitivity Setting", ""))
        brand_safety_custom = st.text_area("Brand Safety Custom Settings", value=edit_data.get("Brand Safety Custom Settings", ""))

        # VERIFICATION
        third_party_verification = st.text_input("Third Party Verification Services", value=edit_data.get("Third Party Verification Services", ""))
        third_party_labels = st.text_area("Third Party Verification Labels", value=edit_data.get("Third Party Verification Labels", ""))

        # AUDIENCE & INVENTORY
        audience_include = st.text_area("Audience Targeting - Include", value=edit_data.get("Audience Targeting - Include", ""))
        audience_exclude = st.text_area("Audience Targeting - Exclude", value=edit_data.get("Audience Targeting - Exclude", ""))
        affinity_include = st.text_area("Affinity & In Market Targeting - Include", value=edit_data.get("Affinity & In Market Targeting - Include", ""))
        affinity_exclude = st.text_area("Affinity & In Market Targeting - Exclude", value=edit_data.get("Affinity & In Market Targeting - Exclude", ""))
        custom_list = st.text_input("Custom List Targeting", value=edit_data.get("Custom List Targeting", ""))
        inventory_auth_sellers = st.selectbox(
            "Inventory Source Targeting - Authorized Seller Options",
            ["All", "Authorized Direct Sellers Only", "Authorized Direct Sellers And Resellers"],
            index=["All", "Authorized Direct Sellers Only", "Authorized Direct Sellers And Resellers"].index(
                edit_data.get("Inventory Source Targeting - Authorized Seller Options", "Authorized Direct Sellers And Resellers")
            )
        )
        inventory_include = st.text_area("Inventory Source Targeting - Include", value=edit_data.get("Inventory Source Targeting - Include", ""))
        inventory_exclude = st.text_area("Inventory Source Targeting - Exclude", value=edit_data.get("Inventory Source Targeting - Exclude", ""))
        inventory_target_new_exchanges = st.checkbox("Inventory Source Targeting - Target New Exchanges", value=edit_data.get("Inventory Source Targeting - Target New Exchanges", False))

        # FLOOR PRICE
        apply_floor_price = st.checkbox("Apply Floor Price For Deals", value=edit_data.get("Apply Floor Price For Deals", False))
        bid_strategy_unit = st.text_input("Bid Strategy Unit", value=edit_data.get("Bid Strategy Unit", ""))
        bid_strategy_cap = st.text_input("Bid Strategy Do Not Exceed", value=edit_data.get("Bid Strategy Do Not Exceed", ""))
        algorithm_id = st.text_input("Algorithm Id", value=edit_data.get("Algorithm Id", ""))

        submitted = st.form_submit_button("Save Insertion Order")

        if submitted:
            new_entry = {
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
            }

            if selected_index != "-- None --" and not duplicate_mode:
                st.session_state.io_data[idx] = new_entry
                st.success("Insertion Order updated.")
            else:
                st.session_state.io_data.append(new_entry)
                st.success("Insertion Order added.")

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
