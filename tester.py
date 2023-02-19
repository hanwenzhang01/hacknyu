import streamlit as st
from PIL import Image
import requests
# Set the background image
st.set_page_config(
    page_title="My Streamlit",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded",
    #page_bg_color="#F0F8FF", # set background color
)
#st.set_page_config(page_title="My Website", page_icon="tada:", layout="wide")

#Set the background image
page_bg_img = '''
<style>
body {
background-image: url("mark-adriane-bO3S03I2Aw8-unsplash");
background-size: cover;
}
</style>
'''
#st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Style Quiz")

with st.container():
    # customize the style of the container
    st.write("Find your style")
    st.write("Is your closet looking boring? Or are you having trouble finding your aesthetic? We've all been there. This quiz is designed to find the right aesthetic that makes you feel comftorable, confident, and stylish. ")
    st.subheader("Do you wanna be drippy? Take this Quiz!")
    #st.write("[Learn More>](https://)")

st.write("---")

st.header("Find Your Style Quiz")
st.write("#")

##################################

with st.form("form"):
    st.subheader("Which of these describes your personality best?")
    box1 = st.radio("Question 1: ", ['Bold and confident', 'Easy-going and relaxed', 'Disciplined and well-groomed', 'Quiet and reserved'], label_visibility="collapsed")
    data={'a1': box1}

    st.subheader("Which colors do you prefer?")
    box2 = st.radio("Question 2: ", ['Red', 'Beige', 'Blue', 'Black/grey'], label_visibility="collapsed")
    data={'a2': box2}

    st.subheader("Number one thing you want to buy for your closet: ")
    box3 = st.radio("Question 3: ", ['Varsity jacket', 'A top or blouse', 'A tie or button-up', 'Leather pants'], label_visibility="collapsed")
    data={'a3': box3}

   # st.subheader("Q4")
   # box4 = st.radio("Question 4: ", ['answer 1', 'answer 2', 'answer 3', 'answer 4'], label_visibility="collapsed")
   # data={'a4': box4}

    responses = requests.post('http://localhost:8501/', data=data)

    #box2 = st.selectbox("Question 2: ", ['answer 1', 'answer 2', 'answer 3', 'answer 4'])
    #st.write("you chose: ", box2)
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("submitted!")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        if st.button('Click me'):
            st.write('Button clicked!') 
        #import requests
        #data={'a2': box2}
    with right_column:
        st.checkbox("checkbox")
        #import requests
        #data={'a1': box1}

if st.button("button", key=1): 
    #import requests
    st.write("clicked button")
    data = {'answer': 'value'}

st.write("---")
with st.container():
    st.write("## Checkbox")
    st.checkbox("My Checkbox", value=False)