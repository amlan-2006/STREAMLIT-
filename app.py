import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
image_1=Image.open("C:\\Users\\AMLANJYOTI BORAH\\code amlan\\Screenshot 2025-12-23 234219.png")
image_2 =Image.open("C:\\Users\\AMLANJYOTI BORAH\\code amlan\\Screenshot 2025-12-23 234431.png")
image_3 = Image.open("C:\\Users\\AMLANJYOTI BORAH\\code amlan\\105381-OMRNIP-573.jpg")
st.set_page_config(layout="wide")
st.write("##")
st.subheader("Hi All :wave:")
st.title("MY PORTFOLIO WEBSITE")
st.write("This is a small test site built while learning more into softwares and hardwares & all the other cool stuffs :smile:")
st.write("[Learn More](https://www.linkedin.com/in/amlanjyoti-borah-552942364/)")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Achievements', 'Contact'],
        icons = ['person', 'code-slash', 'trophy-fill','chat-left-text-fill'],
        orientation = 'horizontal'
    )
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Amlanjyoti Borah")
            st.title("Undergrad at Assam Engineering College")
    st.write("---")

    with st.container():
        col2,col3 = st.columns(2)
        with col2:
            st.subheader("""
            Education 
            Assam Engineering College - 2025-2029\n
                 Bachelor of Technology: Mechanical Engineering\n
                 Grade: Still Continuing :)\n
            Sandipani Vidyamandir - 2025\n
                PCM + CS\n
                Grade: 85.8% AISSCE\n
            Bimala Academy - 2023\n
                AISSE\n
                Grade: 97%\n
            """)
        with col3:
            st.subheader("""
            Laboratory Visits to :\n
                Indian Institute of Science, Bangalore\n
                U.R Rao Satellite Center, ISRO\n
                JNCASR, Bengaluru
                Hindustan Aeronautics Limited
                Indian Institute of Technology, Guwahati
            """)
if selected == 'Projects':
    with  st.container():
        st.header("My Projects")
        st.write("##")
        col4, col5, col6, col7=st.columns((1,2,3,4))
        with col4:
            st.image(image_1)
        with col5:
            st.subheader("Smart Obstacle Alert Glasses")
            st.write("""
            Ultrasonic Sensor & Arduino Enabled Obstacle Alert Glasses for Visually Impaired People
                     """)
            st.markdown("[Visit Github Repo](https://github.com/amlan-2006/SMART-OBSTACLE-ALERT-GLASSES-FOR-VISUALLY-IMPAIRED-using-Arduino-UNO/blob/main/final_code.ino)")
        with col6:
            st.image(image_2)
        with col7:
            st.subheader("Machine-Learning based Helmet Detection of Riders")
            st.write("""
            YOLO based helmet detection of riders. The YOLO11 model has been trained on dataset obtained from Roboflow, in Colab Notebook
""")
            st.markdown("[Visit Colab Notebook](https://colab.research.google.com/drive/1uwKeaYLYg0sEK4-_eB4Z8wxNl8kfjDOx)")
if selected== "Achievements":
    with st.container():
        col8,col9 = st.columns(2)
        with col8:
            st.subheader("""
            JEE Mains 2025: 93 %ile """)
        with col9:
            st.subheader("""Assam CEE 2025: Rank 231""")
if selected == "Contact":
    st.header("Get in touch!")
    st.write('##')
    st.write('##')
    contact_form = """<form action="https://formsubmit.co/amlanjyotiborah03@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form> 


"""

    left_col, right_col = st.columns((2,1))
    with left_col:
        st.write("Enter your name &               email id")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col :
        st.image(image_3)
