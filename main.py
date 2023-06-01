import pickle
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

# Headder
def Headder():

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/img/heading.jpg");
        background-size: 100%;
        background-position: top;
        background-repeat: no-repeat;
        background-attachment: local;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Main

def main():
    Headder()

    st.markdown("""
    <style>
    .big-font {
    font-size:40px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<p style='padding-top:20px', class='big-font'> Enter Your User-ID</p>", unsafe_allow_html=True)
    uid = st.columns(3)
    user_id = uid[0].text_input(' ')
    #body()
    #Water_Checker()


if __name__ == '__main__':

    main()