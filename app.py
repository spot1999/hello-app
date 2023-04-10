import streamlit as st
import pytz
import requests
import datetime
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="My portfolio", page_icon=":tada:", layout="wide")
# page_bg_img = """
# <style>
# body {
#     background-image: url("https://your-image-url-here");
#     background-size: cover;
# }
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)

# Your Streamlit app code here...
#background-color:#9933ff;
page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background-color: #9933ff;
background-blend-mode: normal;
opacity:0.9;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

# def local_css(file_name):
#     with open(file_name) as f:
#         css = f.read()
#         #st.markdown("<style>{}</style>".format(css), unsafe_allow_html=True)
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#st.set_page_config(page_title="My portfolio", page_icon=":tada:", layout="wide")

# import streamlit as st
#
# st.set_page_config(
#     page_title="My Page Title",
#     page_icon=":smiley:",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     page_bg_color="#0E1117",
#     )

# Your Streamlit app code here

st.write("")

def load_lottieur(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    else:
        return r.json()


#style1 filipino_style
img_f=Image.open('images/sepehr-safari-sajiam-n8bZJpA0hig-unsplash.jpg')
width, height = img_f.size
new_size = (500, 300) # Set the new width and height
resized_img = img_f.resize(new_size)
resized_img.save('images/sepehr-safari-sajiam-n8bZJpA0hig-unsplash.jpg')

img_s=Image.open('images/filipino_style.jpg')
#,width=500, height=300
# Set the timezone to 'Asia/Manila'
tz = pytz.timezone('Asia/Manila')
now = datetime.datetime.now(tz)
hour = now.hour
greet = None
if hour < 12:greet = " Good Morning!!! :sun_with_face: :kissing_heart: :kissing_heart: :kissing_heart:"
elif hour < 18:greet = " Good afternoon!!! 🌤️😘😘😘"
else:greet = " Good Evening!!! :night_with_stars: :kissing_heart: :kissing_heart: :kissing_heart:"
st.subheader('Hi visitor:wave:      '+greet)

with st.container():
    st.write("<h1 style='color:yellow;'>Hi im greyhack1999</h1>",unsafe_allow_html=True)
    #st.write("<h1 style='color: red;'>Hello</h1>", unsafe_allow_html=True)
with st.container():
    st.write('---')
    left_column,right_column=st.columns(2)
    with left_column:
        ##cc6699
        st.markdown("<h1 style='color:#cc6699;'> What I love to do: </h1>", unsafe_allow_html=True)
        #st.header('What I love to do:')
        st.write('##')
        # st.markdown("<div style='text-align: center;'><h1 style='color:#cc6699;'>Original Picture</h1></div>", unsafe_allow_html=True)
        st.write("<ul>"
                 "<li><span style='color:#ff9966'>I love to play and cover songs with my guitar</span></li>"
                 "<li><span style='color:#ff9966'>I love to play PUBG Mobile (action games etc.)</span></li>"
                 "<li><span style='color:#ff9966'>I love to watch action movies e.g. (batman movies, tekken, word war movies)</span></li>"
                 "<li><span style='color:#ff9966'>I love to swim in the river</span></li>"
                 "<li><span style='color:#ff9966'>I love to bike along the highway</span></li>"
                 "<li><span style='color:#ff9966'>I love to fix tires</span></li>"
                 "<li><span style='color:#ff9966'>I love math and logic problems</span></li>"
                 "</ul>",
                 unsafe_allow_html=True)

        st.write("<span style='color:#ff9966'>[Learn more>](https://www.freecodecamp.org/learn/)</span>",
                 unsafe_allow_html=True)

with right_column:
    animation = load_lottieur('https://assets8.lottiefiles.com/packages/lf20_x1ikbkcj.json')
    st_lottie(animation,height=300,key='coding')


with st.container():
    st.write('---')
    st.markdown("<div style='text-align: center;'><h1 style='color:#cc6699;'>Original Picture</h1></div>",
                unsafe_allow_html=True)
    st.write('##')
    image_column,text_column=st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_f)
    with text_column:
        st.subheader('This picture is from the pixel-bay website')
        st.write('##')
        st.write(
            "<p style='color:#ff9966;'>This is the picture that caught my interest to edit clothings for fashions:</p>"
            "<ul>"
            "<li style='color:#ff9966;'>It is a plain black cloths with the background a car</li>"
            "<li style='color:#ff9966;'>Looking at the design, it makes no sense</li>"
            "</ul>", unsafe_allow_html=True)

        #st.write('[Learn more>](https://www.freecodecamp.org/learn/)')
with st.container():
    st.write('---')
    st.markdown("<h1 style='color:#cc6699;'> Edited Picture </h1>", unsafe_allow_html=True)
    st.write('##')
    text_column,image_column=st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_s)
    with text_column:
        st.subheader('Filipino Style Cloth')
        ##ff9966
        st.write('##')
        st.write(
            "<p style='color:#ff9966;'>I have no background in editing image and this is the first time I've created one :</p>"
            "<ul>"
            "<li style='color:#ff9966;'>This is based on the concept of Philippine National flag</li>"
            "<li style='color:#ff9966;'>The red color symbolizes PRIDE</li>"
            "<li style='color:#ff9966;'>The blue color symbolizes PEACE</li>"
            "<li style='color:#ff9966;'>The yellow color signifies HOPE</li>"
            "<li style='color:#ff9966;'>The concept of my design is about pride, peace, and hope of the country</li>"
            "</ul>", unsafe_allow_html=True)
        #st.write('[Learn more>](https://www.freecodecamp.org/learn/)')




    url = load_lottieur('https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json')

    st_lottie(url,
              # change the direction of our animation
              reverse=True,
              # height and width of animation
              height=400,
              width=400,
              # speed of animation
              speed=1,
              # means the animation will run forever like a gif, and not as a still image
              loop=True,
              # quality of elements used in the animation, other values are "low" and "medium"
              quality='high',
              # THis is just to uniquely identify the animation
              key='Car'
              )

    with st.container():
        st.write('---')





