import streamlit as st
import plotly.express as px
from weather_backend import get_data


st.title('Weather Forcast for the Next Days')
place = st.text_input("Place")
days = st.slider('Forcast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
options = st.selectbox("Select data to view", ['Temperature', 'Sky'])

st.subheader(f'{options} for the next {days} days in {place}')


if place:
    try:
        # call the data
        filtered_data = get_data(place, days)

        if options == 'Temperature':
            temperature = [dic['main']['temp'] / 10 for dic in filtered_data]
            date = [dic['dt_txt'] for dic in filtered_data]
            figure = px.line(x=date, y=temperature,
                             labels={"x": 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if options == 'Sky':
            images = {'Clouds': 'images/cloud.png', 'Clear': 'images/clear.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            sky_condition = [dic['weather'][0]['main'] for dic in filtered_data]

            image_paths = [images[condition] for condition in sky_condition]

            # Create columns for a grid-like display
            # I use 8 columns because we have 8 observations per day
            columns_per_row = 8

            # Split the list of images into chunks of columns_per_row
            rows = [image_paths[i:i + columns_per_row] for i in
                    range(0, len(image_paths), columns_per_row)]

            # Display images row by row
            for row in rows:
                cols = st.columns(columns_per_row)
                for col, image in zip(cols, row):
                    col.image(image, width=115)
    except KeyError:
        st.info("It looks like you've entered an invalid country name. ")