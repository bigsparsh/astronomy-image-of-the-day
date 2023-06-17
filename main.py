import requests
import streamlit as st

st.set_page_config(layout='wide')
api_key = 'X0Enn8vIo0CFnbPX4oymqtks9hxdnWyUVHY18VWB'
date = st.date_input("Which date's astronomy image do you want to see?: ")

if st.button("Search"):
    url = 'https://api.nasa.gov/planetary/apod?' \
        f'api_key={api_key}&' \
        f'date={date}'

    response = requests.get(url)
    content = response.json()
    st.title(content['title'])
    st.subheader(f'Date: {content["date"]}')
    if content['media_type'] == 'video':
      st.video(content['url'])
    else:
      st.image(content['url'])

    st.write(content['explanation'])