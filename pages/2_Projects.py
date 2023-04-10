# #https://www.youtube.com/watch?v=hEPoto5xp3k
# import streamlit as st
# from streamlit_option_menu import option_menu
#
# st.set_page_config(page_title="Projects", page_icon=":tada:", layout="wide", initial_sidebar_state="expanded")
# page_bg_img="""
# <style>
# [data-testid="stAppViewContainer"]{
# background-color: #9933ff;
# background-blend-mode: normal;
# opacity:0.9;
# background-image: url("https://wallpaperboat.com/wp-content/uploads/2019/10/cool-vector-03.jpg");
# background-size: cover;
# }
# </style>
# """
# st.markdown(page_bg_img,unsafe_allow_html=True)
#
#
# with st.sidebar:
#     selected=option_menu(
#         menu_title='Main Menu',
#         options=['Home','Projects','Contact'],
#         icons=['house','book','envelope'],
#         menu_icon='cast',
#         default_index=0,
#         orientation='horizontal',
#
#     )
# if selected=="Home":st.title("Selected: "+selected)
# if selected=="Projects":st.title("Selected: " +selected)
# if selected=="Contact":st.title("Selected: " +selected)
#
#
#
# # st.title('Projects')




import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Projects", page_icon=":tada:", layout="wide", initial_sidebar_state="auto")
page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background-color: #9933ff;
background-blend-mode: normal;
opacity:0.9;
background-image: url("https://wallpaperboat.com/wp-content/uploads/2019/10/cool-vector-03.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


with st.sidebar:
    selected=option_menu(
        menu_title='Main Menu',
        options=['Home','Projects','Contact'],
        icons=['house','book','envelope'],
        menu_icon='cast',
        default_index=0,
        orientation='vertical', # set orientation to vertical

    )
if selected=="Home":st.title("Selected: "+selected)
if selected=="Projects":st.title("Selected: " +selected)
if selected=="Contact":st.title("Selected: " +selected)
