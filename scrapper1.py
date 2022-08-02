import requests
from bs4 import BeautifulSoup
import re
import streamlit as st


st.set_page_config(page_title="App1", page_icon="🧟 🧟‍♂️")
st.title("Purplle Rating App")

txt_input = st.text_input("Enter list of all Purplle SKU's: ")
if txt_input:
    txt_input = txt_input.split(" ")
    session=requests.session()
    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'}
    url = 'https://www.purplle.com/pd/'+str(txt_input[0])
    print(url)
    soupR=session.get(url,headers=header,allow_redirects=False)
    print(soupR.headers)
#     loc=soupR.headers['location']
#     print(loc)
    
#     productId = re.findall(';product_id=(\d+)', str(soupR))[0]
#     r = session.get(

#         f'https://www.purplle.com/neo/catalog/reviews?productId={productId}&page=1&sortBy=mh',headers=header).json()
#     rating_count = r['reviewStats']['countRating']
#     rating_avg = r['reviewStats']['avgRating']
#     count_reviews = r['reviewStats']['countReviews']
#     st.write('Rating Count:', rating_count)
#     st.write('avg Rating:', rating_avg)
#     st.write('Count reviews:', count_reviews)
