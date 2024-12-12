import streamlit as st
import folium
import pandas as pd

st.title("Interactive Folium Map Generator")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if st.button("Generate Map"):
        # Check if 'latitude' and 'longitude' columns exist
        if 'latitude' not in df.columns or 'longitude' not in df.columns:
            st.error("CSV must have 'latitude' and 'longitude' columns.")
        else:
            # Create Folium map
            map_center = [df['latitude'].mean(), df['longitude'].mean()]
            m = folium.Map(location=map_center, zoom_start=10)

            # Add markers to the map
            for _, row in df.iterrows():
                folium.Marker([row['latitude'], row['longitude']], popup=row.get('name', 'Location')).add_to(m)

            # Display the map
            st.components.v1.html(m._repr_html_(), height=600)

            # Export HTML file
            m.save("map.html")
            st.success("Map generated and saved as map.html")
