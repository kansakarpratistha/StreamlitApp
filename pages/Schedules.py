import streamlit as st

class Schedule:
    def fetch_schedule(self, track_id):
        st.set_page_config(
        page_title="Speedy Delivers | Schedule",
        page_icon="👋",
        )
        st.markdown("# Schedules")
        st.markdown("""<style>
        .st-emotion-cache-18ni7ap{
            background-color: rgb(75,171,151)
        }
        [data-testid=stSidebar]{
            background-color: rgba(75,171,151, 0.8)
        }
        </style>""", unsafe_allow_html=True)

        st.write("Track your shipment!")
        st.write("tracking_id:")
        st.write("button")

Schedule = Schedule()
Schedule.fetch_schedule(123)