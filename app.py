import streamlit as st
import pytz
import requests
import datetime
from streamlit_lottie import st_lottie
from PIL import Image

def local_css(file_name):
    with open(file_name) as f:
        css = f.read()
        st.markdown("<style>{}</style>".format(css), unsafe_allow_html=True)



#st.image(img_f, width=width, height=height)


st.set_page_config(page_title="My portfolio", page_icon=":tada:", layout="wide")


def load_lottieur(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    else:
        return r.json()

animation=load_lottieur('https://assets8.lottiefiles.com/packages/lf20_x1ikbkcj.json')
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
if hour < 12:
    greet = " Good morning!"
elif hour < 18:
    greet = " Good afternoon!"
else:
    greet = " Good evening!"

st.subheader('hi visitor:wave:'+greet)
st.title('My name is Greyhack1999:')

with st.container():
    st.write('Hi im greyhack1999')
with st.container():
    st.write('---')
    left_column,right_column=st.columns(2)
    with left_column:
        st.header('What I love to do:')
        st.write('##')
        st.write(
            "Based on the things I like to do, they are very different from the courses I've taken:\n"
             "- I love to play and cover songs with my guitar\n"
            "- I love to play PUBG Mobile(action games etc.)\n"
            "- I love to watch action movies e.g('batman movies,tekken,word war movies')\n"
             "- I love to swim in the river\n"
             "- I love to bike along the high way\n"
             "- I love to fix tires\n"
             "- I love math and logic problems\n"

                 )
        st.write('[Learn more>](https://www.freecodecamp.org/learn/)')

with right_column:
    st_lottie(animation,height=300,key='coding')


with st.container():
    st.write('---')
    st.header('Original picture')
    st.write('##')
    image_column,text_column=st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_f)
    with text_column:
        st.subheader('This picture is from the pixel-bay website')
        st.write('##')
        st.write(
            "This is the picture that caught my interest to edit clothings for fashions:\n"
            "- It is a plain black cloths with the background a car\n"
            "- looking at the design  ,it makes no sense\n"
        )
        #st.write('[Learn more>](https://www.freecodecamp.org/learn/)')
with st.container():
    st.write('---')
    st.header('Edited picture')
    st.write('##')
    text_column,image_column=st.columns((1,2))
    with image_column:
        #insert image

        st.image(img_s)

    with text_column:
        st.subheader('Filipino Style Cloth')
        st.write('##')
        st.write(
            "Ive have no background in editing image and this is the first time I've created one :\n"
            "- This is base on the concept of Philipine National flag\n"
             "- The red color symbolize PRIDE\n"
             "- The blue color symbolize PEACE\n"
            "- The yellow color signifies HOPE\n"
             "- The concept of my design is about pride,peace and hope of the country\n"

        )
        #st.write('[Learn more>](https://www.freecodecamp.org/learn/)')





#__contact__FORM

with st.container():
    st.write('___')
    st.header('Get touch with me')
    st.write('##')


contact_form= """

<form action="https://formsubmit.co/6650288b2352759c4dd8c1fed161b127" method="POST">
     <input type='hidden' name='_captcha' value='false'>
     <input type="text" name="name" placeholder='Your name'required>
     <input type="email" name="email" placeholder='Your email' required>
     <textarea name='message' placeholder='Your messafe here' required></textarea>
     <button type="submit">Send</button>
</form>

"""
left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()
