import streamlit as st
import plotly.express as px


st.title('Weather Forcast for the Next Days')
place = st.text_input("Place")
days = st.slider('Forcast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days' )
options = st.selectbox("Select data to view", ['Temperature', 'Sky'])

st.subheader(f'{options} for the next {days} days in {place}')

date = ['2024-07-01', '2024-07-02', '2024-07-03']

temperature = [16, 19, 21]

figure = px.line(x=date, y=temperature, labels={"x": 'Date', 'y': 'Temperature (C)'})

st.plotly_chart(figure)