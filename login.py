import streamlit as st
import authlib
#from app import chat

IMAGE_ADDRESS = "https://www.shutterstock.com/image-photo/demo-text-message-magnifying-glass-space-2491336635"


if 'lang' not in st.session_state:
    st.session_state.lang = "en"

# Title and Image
st.title("Demo_Google_Log")
st.image(IMAGE_ADDRESS)

# Login pipeline
if not st.experimental_user.is_logged_in:
    if st.sidebar.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
else:
    if st.sidebar.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()
        st.stop()

