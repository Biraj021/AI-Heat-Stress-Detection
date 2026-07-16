import streamlit as st
import pandas as pd
import plotly.express as px
import os
import time


# =================================
# Page Configuration
# =================================

st.set_page_config(
    page_title="AI Heat Stress Detection",
    page_icon="🌡️",
    layout="wide"
)


# =================================
# Title
# =================================

st.title(
    "🌡️ AI Heat Stress Detection Dashboard"
)


st.write(
    "Real-time monitoring using ESP32 + DHT22 + Machine Learning"
)



# =================================
# Data Location
# =================================

DATA_FILE = "../backend/data/sensor_data.csv"



# =================================
# Auto Refresh
# =================================

refresh = st.sidebar.slider(
    "Refresh Time (seconds)",
    1,
    10,
    5
)



# =================================
# Load Data
# =================================

if os.path.exists(DATA_FILE):

    df = pd.read_csv(DATA_FILE)


    if len(df) > 0:


        latest = df.iloc[-1]



        # ==========================
        # Status Color
        # ==========================

        status = latest["HeatStress"]



        if status == "High":

            color = "🔴"

        elif status == "Medium":

            color = "🟡"

        else:

            color = "🟢"



        # ==========================
        # Cards
        # ==========================

        col1, col2, col3, col4 = st.columns(4)



        with col1:

            st.metric(
                "🌡 Temperature",
                str(
                    latest["AmbientTemp"]
                ) + " °C"
            )



        with col2:

            st.metric(
                "💧 Humidity",
                str(
                    latest["Humidity"]
                ) + " %"
            )



        with col3:

            st.metric(
                "AI Prediction",

                color +
                " " +
                status
            )



        with col4:

            st.metric(
                "Confidence",

                str(
                    latest["Confidence"]
                )
                +
                "%"
            )



        st.divider()



        # ==========================
        # Temperature Chart
        # ==========================

        st.subheader(
            "🌡 Temperature History"
        )


        fig1 = px.line(
            df,

            x="Timestamp",

            y="AmbientTemp",

            markers=True,

            title="Ambient Temperature"
        )


        st.plotly_chart(
            fig1,
            use_container_width=True
        )



        # ==========================
        # Humidity Chart
        # ==========================

        st.subheader(
            "💧 Humidity History"
        )


        fig2 = px.line(
            df,

            x="Timestamp",

            y="Humidity",

            markers=True,

            title="Humidity"
        )


        st.plotly_chart(
            fig2,
            use_container_width=True
        )



        # ==========================
        # Prediction Distribution
        # ==========================

        st.subheader(
            "AI Prediction History"
        )


        fig3 = px.histogram(
            df,

            x="HeatStress",

            color="HeatStress",

            title="Heat Stress Levels"
        )


        st.plotly_chart(
            fig3,
            use_container_width=True
        )



        # ==========================
        # Data Table
        # ==========================

        st.subheader(
            "Sensor Records"
        )


        st.dataframe(
            df.tail(20),
            use_container_width=True
        )



    else:

        st.warning(
            "Waiting for sensor data..."
        )



else:


    st.error(
        "sensor_data.csv not found"
    )



# Refresh page

time.sleep(refresh)

st.rerun()