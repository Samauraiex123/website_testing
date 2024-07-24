import streamlit as st
import test;
import video;
import streamlit as st

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main'

# Run the appropriate page based on session state
if st.session_state.current_page == 'main':
    test.main()
elif st.session_state.current_page == 'second':
    video.main()

