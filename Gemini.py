import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import base64
# API Key
GOOGLE_API_KEY ="AIzaSyCS3BW1hhPOSX6OmGqYu-tIMKj7UniLMZw" # use your gemini api here 

load_dotenv()

st.set_page_config(
    page_title='Chat with Gemini',
    page_icon='image\brain.png',
    layout='centered',

)
genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')

def get_image(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_image(r'image/5053309.jpg')
st.markdown(f"""
    <style>
    .stApp {{
    
        background-image: url('data:image/jpg;base64,{img}');
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        opacity: 0.9;
        height: 100vh;
    }}
    </style>
""", unsafe_allow_html=True)



def translate_role_streamlit(user_role):
    if user_role=='model':
        return 'assistant'
    else:
        return user_role
    
if 'chat_session' not in st.session_state:
    st.session_state.chat_session=model.start_chat(history=[])
st.markdown("""
    <style>
    .main {
        max-height: 100vh;
        overflow-y: scroll;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        padding-top: 20px;
    }

    /* Chat bubbles styling */
    .user-message {
        text-align: right;
        background-color: 	#008000;
        
        border-color: #c0c0c0;
        color: white;
        padding: 8px;
        border-radius: 10px;
        margin: 10px;
        width: fit-content;
        float: right;
        clear: both;
    }
    h1 {
        text-align: center;
        font-size: 2.5rem;
        color: white;
    }
    .ai-message {
        text-align: left;
        background-color: #282828;
        color: #FFFFFF;
        padding: 8px;
        border-radius: 10px;
        margin: 10px;
        width: fit-content;
        float: left;
        clear: both;
    }
    footer { 
        visibility: hidden;
    }
        .custom-footer {
        background-color: #f5f5f5;
        color: #000000;
        text-align: center;
        padding: 10px;
        position: fixed;
        bottom: 0;
        width: 100%;
        border-top: 2px solid #ccc;
    }

    </style>
""", unsafe_allow_html=True)


st.markdown("# Chat with Gemini 🤖")

for message in st.session_state.chat_session.history:
    if message.role=='user':
        user_html=f"<div class='user-message'>{message.parts[0].text}</div>"
        st.markdown(user_html,unsafe_allow_html=True)
    else:
        ai_html=f"<div class= 'ai-message'>{message.parts[0].text}</div>"
        st.markdown(ai_html,unsafe_allow_html=True)   
        
user_input=st.chat_input('Ask Gemini Pro')
if user_input:
    user_html=f"<div class='user-message'>{user_input}</div>"
    st.markdown(user_html,unsafe_allow_html=True)
    
    gemini_response=st.session_state.chat_session.send_message(user_input)
    
    ai_html=f"<div class= 'ai-message'>{gemini_response.text}</div>"
    st.markdown(ai_html,unsafe_allow_html=True)    