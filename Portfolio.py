import streamlit as st
import info

#About Me
def aboutMeSection():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me) #this is a printing function
    st.write("---")
aboutMeSection