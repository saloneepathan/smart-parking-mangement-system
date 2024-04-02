import streamlit as st
import dashboard;
import home;
import parking_slots;

def main():
    st.title("Smart Parking System Management")

    st.sidebar.title("Navigation")
    page_options = ["Home", "Parking Slots", "Dashboard"]
    selected_page = st.sidebar.radio("Go to", page_options)

    if selected_page == "Home":
        home.home_fun()
    elif selected_page == "Parking Slots":
        parking_slots.parking_slot_fun()
    elif selected_page == "Dashboard":
        dashboard.dashboard_fun()


if __name__ == "__main__":
    main()
