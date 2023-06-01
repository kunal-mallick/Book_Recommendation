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

    t1,t2,t3,t4,t5 = st.columns(5)

    with t1:
        
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.text("book 1")
            st.markdown("<p class='big-font'>  book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>  book 4 publisher</p>", unsafe_allow_html=True)

    with t2:
        
        t21 = st.container()

        with t21:
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    with t3:

        t31 = st.container()

        with t31:
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    with t4:
        
        t41 = st.container()

        with t41:
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    with t5:

        t51 = st.container()

        with t51:
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    st.markdown("<p style = 'padding-top:10px'></p>", unsafe_allow_html=True)
    st.image('https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/img/top5.png')
    
    t1,t2,t3,t4,t5 = st.columns(5)

    with t1:
        
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>  book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>  book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>  book 4 publisher</p>", unsafe_allow_html=True)

    with t2:
        
        t21 = st.container()

        with t21:
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    with t3:

        t31 = st.container()

        with t31:
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    #st.markdown("<p style='padding-top:10px', class='big-font'></p>", unsafe_allow_html=True)

    with t4:
        
        t41 = st.container()

        with t41:
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    with t5:

        t51 = st.container()

        with t51:
            st.image('http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg', width=200)
            st.markdown("<p class='big-font'>book 4 name</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 auther</p>", unsafe_allow_html=True)
            st.markdown("<p class='big-font'>book 4 publisher</p>", unsafe_allow_html=True)

    st.columns(2)
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

    uid = st.columns([1,3])
    uid[0].markdown("<p style='padding-top:20px', class='big-font'> Enter Your User-ID</p>", unsafe_allow_html=True)
    user_id = uid[1].text_input('')
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    body()


if __name__ == '__main__':

    main()
