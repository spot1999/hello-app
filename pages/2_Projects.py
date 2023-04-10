import streamlit as st

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

st.title('Contact')
#st.write("Im looking for",st.session_state['my_input'])

#__contact__FORM
with st.container():
    st.write('---')
    st.markdown("<div style='text-align: center;'><h1 style='color:#cc6699;'>Please Get in Touch</h1></div>",
                unsafe_allow_html=True)
    left_column, right_column, _ = st.columns([1, 2, 1])

    with left_column:
        st.write('')
    with right_column:
        contact_form = """
        <form action="https://formsubmit.co/6650288b2352759c4dd8c1fed161b127" method="POST">
            <input type='hidden' name='_captcha' value='True'>
            <div style='display: flex; flex-direction: column; gap: 10px;'>
                <label for="name">Your name:</label>
                <input type="text" id="name" name="name" placeholder="Enter your name" required>
                <label for="email">Your email:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
                <label for="message">Your message:</label>
                <textarea id="message" name="message" placeholder="Enter your message" required></textarea>
                <button type="submit">Send</button>
            </div>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

    with _:
        st.write('')

with st.container():
    st.write('---')

    if 'y_input' not in st.session_state:
        st.session_state['my_input'] = ''
    my_input = st.text_input('Input a text here', st.session_state['my_input'])
    submit = st.button('Submit')
    if submit:
        st.session_state['my_input'] = my_input
        st.write('You have entered:', my_input)

    st.write('---')
    # <input type='hidden' name='_captcha' value='false'>


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
