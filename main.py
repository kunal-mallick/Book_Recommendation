import pickle
import numpy as np
import pandas as pd
import streamlit as st

# Adding Dataset
user = pd.read_csv('https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/Data%20Preprocessing%20%26%20EDA/User.csv')
book = pd.read_csv('https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/resources/Books.csv', encoding='latin-1')
area = pd.read_csv('https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/resources/Ratings.csv', encoding='latin-1')

# Adding Pickle File
adult = pd.read_pickle('age_adult.pkl')
child = pd.read_pickle('age_child.pkl')
young = pd.read_pickle('age_young.pkl')
other = pd.read_pickle('age_other.pkl')
elder = pd.read_pickle('age_elder.pkl')
teen = pd.read_pickle('age_teen.pkl')
usa = pd.read_pickle('area_usa.pkl')
canada = pd.read_pickle('area_canada.pkl')
uk = pd.read_pickle('area_uk.pkl')
australia = pd.read_pickle('area_australia.pkl')
germany = pd.read_pickle('area_germany.pkl')
others = pd.read_pickle('area_others.pkl')

# New
new_adult = pd.read_pickle('new_adult.pkl')
new_child = pd.read_pickle('new_children.pkl')
new_young = pd.read_pickle('new_youngster.pkl')
new_other = pd.read_pickle('new_other.pkl')
new_elder = pd.read_pickle('new_elder.pkl')
new_teen = pd.read_pickle('new_youngster.pkl')
new_usa = pd.read_pickle('new_usa.pkl')
new_canada = pd.read_pickle('new_canada.pkl')
new_uk = pd.read_pickle('new_uk.pkl')
new_spain = pd.read_pickle('new_spain.pkl')
new_germany = pd.read_pickle('new_germany.pkl')
new_others = pd.read_pickle('new_others.pkl')

# Changing Layout to wide
st.set_page_config(layout="wide")

# Predection Funtion
def create_result(s,x):
    ISBN = []
    rating = []

    for i in s[s['user-2'] == x].loc[:,'user-1']:
        for j in area[(area['User-ID'] == i)].index:
            k = area.loc[j,'ISBN']
            l = area.loc[j,'Book-Rating']
            ISBN.append(k)
            rating.append(l)

    result = pd.DataFrame(
        {
            'ISBN' : ISBN,
            'rating' : rating
        }
    )

    return result

def get_ISBN(x):
    d = []
    for i in area[(area['User-ID'] == x)].loc[:,'ISBN'].values:
        d.append(i)
    
    return d

def drop(a,b):

    drop = []

    for i in range(len(a)):
        for j in b:
            c = a.loc[i,'ISBN']
            if c == j:
                drop.append(i)

    return drop

def fillter_ISBN(x, y):

    x.drop(index=y, inplace= True)
    x.drop_duplicates(inplace=True)

    return x

def set_name(x):
    if book[book['ISBN'] == x].shape[0] == 0:
        return np.nan
    else:
        return book[book['ISBN'] == x].loc[:,'Book-Title'].values[0]

def set_Author(x):
    if book[book['ISBN'] == x].shape[0] == 0:
        return np.nan
    else:
        return book[book['ISBN'] == x].loc[:,'Book-Author'].values[0]

def set_Publisher(x):
    if book[book['ISBN'] == x].shape[0] == 0:
        return np.nan
    else:
        return book[book['ISBN'] == x].loc[:,'Publisher'].values[0]

def set_Image(x):
    if book[book['ISBN'] == x].shape[0] == 0:
        return np.nan
    else:
        return book[book['ISBN'] == x].loc[:,'Image-URL-L'].values[0]

def predect(similarity,ISBN):

    o = create_result(similarity,ISBN)
    k = get_ISBN(ISBN)
    n = drop(o,k)
    e = fillter_ISBN(o,n)
    e = e.sort_values(by='rating', ascending= False).head(75)
    e['Book-Title'] = e['ISBN'].apply(lambda x: set_name(x))
    e['auther'] = e['ISBN'].apply(lambda x: set_Author(x))
    e['publisher'] = e['ISBN'].apply(lambda x: set_Publisher(x))
    e['image'] = e['ISBN'].apply(lambda x: set_Image(x))
    e.dropna(inplace=True)

    return e.sort_values(by='rating', ascending= False).head(5)

def get_detail(x):
    area = user[user['User_Id'] == x].loc[:,'area'].values[0]
    age = user[user['User_Id'] == x].loc[:,'age'].values[0]
    u_type = user[user['User_Id'] == x].loc[:,'type'].values[0]

    return area,age,u_type

def pred_age(user_id):

    age = get_detail(user_id)[1]
    type = get_detail(user_id)[2]

    try:

        if type == 'old':
            if age == 'Adult':
                df_age = predect(adult,user_id)
            elif age == 'other':
                df_age = predect(other,user_id)
            elif age == 'Youngster':
                df_age = predect(young,user_id)
            elif age == 'Teenager':
                df_age = predect(teen,user_id)
            elif age == 'Elder':
                df_age = predect(elder,user_id)
            elif age == 'Children':
                df_age = predect(child,user_id)

        elif type == 'new':
            if age == 'Adult':
                df_age = new_adult
            elif age == 'other':
                df_age = new_other
            elif age == 'Youngster':
                df_age = new_young
            elif age == 'Teenager':
                df_age = new_teen
            elif age == 'Elder':
                df_age = new_elder
            elif age == 'Children':
                df_age = new_child

    except:
        if age == 'Adult':
            df_age = new_adult
        elif age == 'other':
            df_age = new_other
        elif age == 'Youngster':
            df_age = new_young
        elif age == 'Teenager':
            df_age = new_teen
        elif age == 'Elder':
            df_age = new_elder
        elif age == 'Children':
            df_age = new_child

    if df_age.shape[0] == 0:
        if age == 'Adult':
            df_age = new_adult
        elif age == 'other':
            df_age = new_other
        elif age == 'Youngster':
            df_age = new_young
        elif age == 'Teenager':
            df_age = new_teen
        elif age == 'Elder':
            df_age = new_elder
        elif age == 'Children':
            df_age = new_child
    return df_age

def pred_area(user_id):

    area = get_detail(user_id)[0]
    type = get_detail(user_id)[2]

    try:
        if type == 'old':
            if area == 'usa':
                df_area = predect(usa,user_id)
            elif area == 'other':
                df_area = predect(others,user_id)
            elif area == 'canada':
                df_area = predect(canada,user_id)
            elif area == 'unitedkingdom':
                df_area = predect(uk,user_id)
            elif area == 'germany':
                df_area = predect(germany,user_id)
            elif area == 'australia':
                df_area = predect(australia,user_id)

        elif type == 'new':
            if area == 'usa':
                df_area = new_usa
            elif area == 'canada':
                df_area = new_canada
            elif area == 'unitedkingdom':
                df_area = new_uk
            elif area == 'germany':
                df_area = new_germany
            elif area == 'australia':
                df_area = new_spain
            elif area == 'other':
                df_area = new_others

    except:
        if area == 'usa':
            df_area = new_usa
        elif area == 'canada':
            df_area = new_canada
        elif area == 'unitedkingdom':
            df_area = new_uk
        elif area == 'germany':
            df_area = new_germany
        elif area == 'australia':
            df_area = new_spain
        elif area == 'other':
            df_area = new_others

    if df_area.shape[0] == 0:
        if area == 'usa':
            df_area = new_usa
        elif area == 'canada':
            df_area = new_canada
        elif area == 'unitedkingdom':
            df_area = new_uk
        elif area == 'germany':
            df_area = new_germany
        elif area == 'australia':
            df_area = new_spain
        elif area == 'other':
            df_area = new_others

    return df_area


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

    uid = st.columns([1,3])
    uid[0].markdown("<p style='padding-top:20px', class='big-font'> Enter Your User-ID</p>", unsafe_allow_html=True)
    user_id = uid[1].number_input('',1)
    

    ar = pred_area(user_id)
    ag = pred_age(user_id)
    
    ar.reset_index(inplace=True)
    ar.drop(columns='index',inplace=True)
    ag.reset_index(inplace=True)
    ag.drop(columns='index',inplace=True)


    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.image('https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/img/trending.jpg')

    t1,t2,t3,t4,t5 = st.columns(5)

    with t1:
        
        st.image(ar.loc[0,'image'], width=200)
        st.text(ar.loc[0,'Book-Title'])
        st.text(ar.loc[0,'auther'])
        st.text(ar.loc[0,'publisher'])

    with t2:

        st.image(ar.loc[1,'image'], width=200)
        st.text(ar.loc[1,'Book-Title'])
        st.text(ar.loc[1,'auther'])
        st.text(ar.loc[1,'publisher'])

    with t3:

        st.image(ar.loc[2,'image'], width=200)
        st.text(ar.loc[2,'Book-Title'])
        st.text(ar.loc[2,'auther'])
        st.text(ar.loc[2,'publisher'])

    with t4:
        
        st.image(ar.loc[3,'image'], width=200)
        st.text(ar.loc[3,'Book-Title'])
        st.text(ar.loc[3,'auther'])
        st.text(ar.loc[3,'publisher'])

    with t5:

        st.image(ar.loc[4,'image'], width=200)
        st.text(ar.loc[4,'Book-Title'])
        st.text(ar.loc[4,'auther'])
        st.text(ar.loc[4,'publisher'])

    st.markdown("<p style = 'padding-top:10px'></p>", unsafe_allow_html=True)
    st.image('https://raw.githubusercontent.com/kunal-mallick/Book_Recommendation/main/img/top5.png')
    
    t1,t2,t3,t4,t5 = st.columns(5)

    with t1:
        
        st.image(ag.loc[0,'image'], width=200)
        st.text(ag.loc[0,'Book-Title'])
        st.text(ag.loc[0,'auther'])
        st.text(ag.loc[0,'publisher'])

    with t2:

        st.image(ag.loc[1,'image'], width=200)
        st.text(ag.loc[1,'Book-Title'])
        st.text(ag.loc[1,'auther'])
        st.text(ag.loc[1,'publisher'])

    with t3:

        st.image(ag.loc[2,'image'], width=200)
        st.text(ag.loc[2,'Book-Title'])
        st.text(ag.loc[2,'auther'])
        st.text(ag.loc[2,'publisher'])

    with t4:
        
        st.image(ag.loc[3,'image'], width=200)
        st.text(ag.loc[3,'Book-Title'])
        st.text(ag.loc[3,'auther'])
        st.text(ag.loc[3,'publisher'])

    with t5:

        st.image(ag.loc[4,'image'], width=200)
        st.text(ag.loc[4,'Book-Title'])
        st.text(ag.loc[4,'auther'])
        st.text(ag.loc[4,'publisher'])

    st.columns(2)
# Main

def main():
    Headder()
    body()


if __name__ == '__main__':

    main()
