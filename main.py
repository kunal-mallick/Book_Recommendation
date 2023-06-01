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

# Body

def body():

    st.markdown("""
    <style>
    .big-font {
    font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.image('https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/img/trending.jpg')

    t3 = st.columns(3)

    with t3[0]:
        
        t31 = st.columns(2)

        t31[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t31[1]:
            st.markdown("<p class='big-font'>book 1 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 1 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 1 publisher</p>", unsafe_allow_html=True)

    with t3[1]:
        
        t32 = st.columns(2)

        t32[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t32[1]:
            st.markdown("<p class='big-font'>book 2 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 2 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 2 publisher</p>", unsafe_allow_html=True)

    with t3[2]:
        
        t33 = st.columns(2)

        t33[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t33[1]:
            st.markdown("<p class='big-font'>book 3 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 3 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 3 publisher</p>", unsafe_allow_html=True)

    st.markdown("<p style='padding-top:10px', class='big-font'></p>", unsafe_allow_html=True)

    t2 = st.columns(3)

    with t2[0]:
        
        t21 = st.columns(2)

        t21[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t21[1]:
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    with t2[1]:
        
        t22 = st.columns(2)

        t22[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t22[1]:
            st.markdown("<p class='big-font'>book 5 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 5 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 5 publisher</p>", unsafe_allow_html=True)

    st.markdown("<p style = 'padding-top:10px'></p>", unsafe_allow_html=True)
    st.image('https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/img/top5.png')
    
    t3 = st.columns(3)

    with t3[0]:
        
        t31 = st.columns(2)

        t31[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t31[1]:
            st.markdown("<p class='big-font'>book 1 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 1 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 1 publisher</p>", unsafe_allow_html=True)

    with t3[1]:
        
        t32 = st.columns(2)

        t32[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t32[1]:
            st.markdown("<p class='big-font'>book 2 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 2 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 2 publisher</p>", unsafe_allow_html=True)

    with t3[2]:
        
        t33 = st.columns(2)

        t33[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t33[1]:
            st.markdown("<p class='big-font'>book 3 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 3 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 3 publisher</p>", unsafe_allow_html=True)

    st.markdown("<p style='padding-top:10px', class='big-font'></p>", unsafe_allow_html=True)

    t2 = st.columns(3)

    with t2[0]:
        
        t21 = st.columns(2)

        t21[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t21[1]:
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    with t2[1]:
        
        t22 = st.columns(2)

        t22[0].image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg')
        with t22[1]:
            st.markdown("<p class='big-font'>book 5 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 5 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 5 publisher</p>", unsafe_allow_html=True)
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
    body()


if __name__ == '__main__':

    main()