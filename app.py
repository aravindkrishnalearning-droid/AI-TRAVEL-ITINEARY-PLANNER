import streamlit as st
from src.core.planner import TravelPlanner  
from  dotenv import load_dotenv

st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itinerary Planner")
st.write("Plan your day trip itineary by entering the city and your interests.")
load_dotenv()  # Load environment variables from .env file

with st.form("planner form"):
    city = st.text_input("Enter the city you want to visit:")
    interests = st.text_input("Enter your interests (comma-separated):")
    submitted = st.form_submit_button("Generate Itinerary")

    if submitted:
        # try:
            if city and interests:
                planner = TravelPlanner()
                planner.set_city(city)
                planner.set_interests(interests)
                itinerary = planner.create_itineary()
                st.subheader("Your Itinerary:")
                st.markdown(itinerary)
            else:
                st.warning("Please enter both city and interests to generate an itinerary.")