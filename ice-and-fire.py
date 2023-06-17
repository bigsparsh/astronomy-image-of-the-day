import requests
import streamlit as st
import json

st.title('A Song of ice and fire')
types_of_media = ['Books', 'Characters', 'Houses']
with st.form(key='my_form'):
    selected_media = st.selectbox('Select a type of media', options=types_of_media)
    srch = st.form_submit_button('Search for this media')
    books = {}
    if srch:
        match selected_media:
            case 'Books':
                url = 'https://anapioficeandfire.com/api/books'
                books = requests.get(url).json()
                list_of_books = [books[i]['name'].title() for i in range(0, len(books))]
                book_selection = st.selectbox('Select book to get info:', options=list_of_books)
            case 'Characters':
                url = 'https://anapioficeandfire.com/api/characters/823'
                books = requests.get(url).json()
                list_of_books = [books[i]['name'].title() for i in range(0, len(books))]
                book_selection = st.selectbox('Select book to get info:', options=list_of_books)
            case 'Houses':
                url = 'https://anapioficeandfire.com/api/houses'
                books = requests.get(url).json()
                list_of_books = [books[i]['name'].title() for i in range(0, len(books))]
                book_selection = st.selectbox('Select book to get info:', options=list_of_books)
                index = ''
                for i in range(0, len(books)):
                    if book_selection == books[i]['name'].title():
                        index = i
                        break
                selected = books[index]

    if st.form_submit_button('Search'):
        match selected_media:
            case 'Books':
                message = f'Authors: {selected["authors"][0]}\n' \
                          f'Number of pages: {selected["numberOfPages"]}\n' \
                          f'Publisher: {selected["publisher"]}\n' \
                          f'Country: {selected["country"]}\n' \
                          f'Media Type: {selected["mediaType"]}\n' \
                          f'Released: {selected["released"]}\n'
                st.info(message)
            case 'Characters':
                message = f'Culture: {selected["culture"][0]}\n' \
                          f'Born: {selected["born"]}\n' \
                          f'Died: {selected["died"]}\n' \
                          f'Titles: {selected["titles"][0]}\n' \
                          f'Aliases: {selected["aliases"]}\n' \
                          f'Played By: {selected["playedBy"]}\n' \
                          f'Mother: {selected["mother"]}\n' \
                          f'Father: {selected["father"]}\n'
                st.info(message)
            case 'Books':
                message = f'Region: {selected["region"][0]}\n' \
                          f'Coat Of Arms: {selected["coatOfArms"]}\n' \
                          f'Words: {selected["words"]}\n' \
                          f'Titles: {selected["titles"][0]}\n' \
                          f'Seats: {selected["seats"][0]}\n' \
                          f'Heir: {selected["heir"][0]}\n' \
                          f'Died Out: {selected["diedOut"][0]}\n' \
                          f'Founded: {selected["founded"]}\n'
                st.info(message)
