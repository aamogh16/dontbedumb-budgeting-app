import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

st.session_state['authenticated'] = False

SideBarLinks(show_home=True)

logger.info("Loading the Home page")

st.title("Don't Be Dumb Budgeting")
st.write("### A smarter way to manage your finances")

st.write('')
st.write('#### Select a user persona to get started:')

# Alex Chen - College Student
if st.button("Alex Chen - College Student", 
            type='primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student'
    st.session_state['first_name'] = 'Alex'
    st.session_state['user_id'] = 1
    logger.info("Logging in as Alex Chen")
    st.switch_page('pages/00_User_Home.py')

# Jamie Rodriguez - Working Professional
if st.button('Jamie Rodriguez - Working Professional', 
            type='primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'professional'
    st.session_state['first_name'] = 'Jamie'
    st.session_state['user_id'] = 2
    logger.info("Logging in as Jamie Rodriguez")
    st.switch_page('pages/00_User_Home.py')

# Jordan Park - Club Treasurer
if st.button('Jordan Park - Club Treasurer', 
            type='primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'treasurer'
    st.session_state['first_name'] = 'Jordan'
    st.session_state['user_id'] = 3
    logger.info("Logging in as Jordan Park")
    st.switch_page('pages/00_User_Home.py')

# Sarah Kim - Family Budget Manager
if st.button('Sarah Kim - Family Budget Manager', 
            type='primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'family'
    st.session_state['first_name'] = 'Sarah'
    st.session_state['user_id'] = 4
    logger.info("Logging in as Sarah Kim")
    st.switch_page('pages/00_User_Home.py')