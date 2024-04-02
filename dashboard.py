import streamlit as st
import sqlite3
import plotly.graph_objects as go

def dashboard_fun():
    # st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")
    # conn = sqlite3.connect('car_data.db')
    # c = conn.cursor()

    # Function to plot metric with icon
    def plot_metric_with_icon(icon_path, label, value):
        st.image(icon_path, use_column_width=True)
        st.markdown(f"<p style='font-size:{40}px; text-align: center; font-family: Poppins;'>{value}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:{20}px; text-align: center; font-family: Roboto Mono;'>{label}</p>", unsafe_allow_html=True)

    # Function to create and display pie chart
    def plot_pie_chart(labels, values):
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        st.plotly_chart(fig, use_container_width=True) 


    # Create a container to center the columns
    container = st.container()

    # Define the content within the container

    with container:
        st.markdown(
            """
            <style>
            @font-face {
                font-family: 'BodoniModa';
                src: url('BodoniModa_9pt-Black.ttf') format('truetype');
            }
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'BodoniModa', sans-serif;
            }
            .plotly-container {
                display: flex;
                justify-content: center;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<h1 style='text-align: center;'>Dashboard</h1>", unsafe_allow_html=True)

        # Define the columns within the container
        with st.container():
            column_1, column_2, column_3, column_4 = st.columns(4)

            with column_1:
                icon_path = "images/car.png"
                plot_metric_with_icon(icon_path, "Total Vehicle Parked", 20)

            with column_2:
                icon_path = "images/carIn.png"
                plot_metric_with_icon(icon_path, "Vehicles In", 20)

            with column_3:
                icon_path = "images/carOut.png"
                plot_metric_with_icon(icon_path, "Vehicles Out", 20)

            with column_4:
                icon_path = "images/parkingDone.png"
                plot_metric_with_icon(icon_path, "Parking Done Within 24 Hrs", 20)
    
    # Create a new container for the pie chart
    pie_chart_container = st.container()

    # Define the content within the pie chart container
    with pie_chart_container:
        st.markdown("<h2 style='text-align: center; font-size: 40px;'>Vehicles In/Out Breakdown</h2>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)  # Add a horizontal line for separation
        # Create the pie chart showing the breakdown of vehicles in and out
        vehicles_labels = ['In', 'Out']
        vehicles_values = [15, 10]  # Sample data for demonstration
        plot_pie_chart(vehicles_labels, vehicles_values)