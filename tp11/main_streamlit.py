import streamlit as st
from UserDAO import UserDAO


def main():
    st.set_page_config(layout="wide")
    dao = UserDAO('formation.db')
    users = dao.findAll()
        
    st.title('Users List')
    st.write('Bonjour')
    title = st.text_input('Movie title', '')
    print(title)

    if st.button('show Movie') and title:
        st.write('The current movie title is', title)    
        st.write('Why hello there')

    st.table(users)

if __name__=='__main__':
    main()
