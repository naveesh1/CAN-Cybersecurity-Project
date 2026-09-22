import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="CAN Security Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Real-Time CAN Security Dashboard")
st.write("CAN traffic monitoring and anomaly detection overview")

st.divider()

detection_file = "data/detection_results.csv"
alert_file = "data/realtime_security_alerts.txt"

# ==============================
# LOAD DETECTION RESULTS
# ==============================

if os.path.exists(detection_file):
    df = pd.read_csv(detection_file)

    total_messages = len(df)
    normal_messages = len(df[df["status"] == "NORMAL"])
    anomaly_messages = len(df[df["status"] == "ANOMALY"])

else:
    df = pd.DataFrame()
    total_messages = 0
    normal_messages = 0
    anomaly_messages = 0


# ==============================
# SECURITY METRICS
# ==============================

if total_messages > 0:
    anomaly_rate = (anomaly_messages / total_messages) * 100
else:
    anomaly_rate = 0


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Messages",
        total_messages
    )

with col2:
    st.metric(
        "Normal Messages",
        normal_messages
    )

with col3:
    st.metric(
        "Anomalous Messages",
        anomaly_messages
    )

with col4:
    st.metric(
        "Anomaly Rate",
        f"{anomaly_rate:.2f}%"
    )


st.divider()


# ==============================
# SECURITY STATUS
# ==============================

st.subheader("🔐 Security Status")

if anomaly_messages > 0:
    st.error(
        f"⚠️ SECURITY ALERT: {anomaly_messages} anomalous CAN messages detected."
    )
else:
    st.success(
        "✅ CAN network traffic is currently normal."
    )


st.divider()


# ==============================
# TRAFFIC OVERVIEW
# ==============================

st.subheader("📊 Traffic Overview")

if total_messages > 0:

    chart_data = pd.DataFrame({
        "Message Type": [
            "Normal",
            "Anomalous"
        ],
        "Count": [
            normal_messages,
            anomaly_messages
        ]
    })

    st.bar_chart(
        chart_data.set_index("Message Type")
    )

else:
    st.info("No traffic data available.")


st.divider()


# ==============================
# ANOMALY REASONS
# ==============================

st.subheader("🚨 Anomaly Reasons")

if anomaly_messages > 0:

    anomaly_df = df[df["status"] == "ANOMALY"]

    reason_counts = (
        anomaly_df["reason"]
        .value_counts()
        .rename_axis("Reason")
        .reset_index(name="Count")
    )

    st.bar_chart(
        reason_counts.set_index("Reason")
    )

else:
    st.info("No anomalies detected.")


st.divider()


# ==============================
# DETECTION RESULTS TABLE
# ==============================

st.subheader("📋 Detection Results")

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )

else:
    st.info("No detection results available.")


st.divider()


# ==============================
# SECURITY ALERT LOG
# ==============================

st.subheader("🚨 Security Alerts")

if os.path.exists(alert_file):

    with open(alert_file, "r") as file:
        alerts = file.read()

    if alerts.strip():

        st.code(
            alerts,
            language="text"
        )

    else:
        st.info("No security alerts recorded.")

else:
    st.info("Real-time security alert log not found.")


st.divider()

st.caption(
    "CAN Cybersecurity Project | "
    "Virtual CAN Network Security Monitoring"
)