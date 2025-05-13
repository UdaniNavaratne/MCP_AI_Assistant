import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import random
import asyncio


# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
config_file = "browser_mcp.json"

# Streamlit page setup
st.set_page_config(page_title="MochiBot 🌷", page_icon="🧋", layout="centered")

# Cute emojis and moods
MOODS = [
    "(๑˃ᴗ˂)ﻭ", "｡ﾟ(TヮT)ﾟ｡", "(●'◡'●)", "(/▽＼)", "(ง •̀_•́)ง", "(*≧ω≦)", "(つ≧▽≦)つ"
]

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "agent" not in st.session_state:
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="qwen-qwq-32b")
    st.session_state.agent = MCPAgent(llm=llm, client=client, memory_enabled=True, max_steps=15)

# Cute header
st.markdown("""
<div style="text-align:center;">
    <h1 style="color:#FF69B4;">🌷 MochiBot — your cozy AI companion 🧋</h1>
    <p style="font-size:18px;">Here to help, listen, and sprinkle some cuteness on your day 💖</p>
</div>
""", unsafe_allow_html=True)

# Mood display
st.markdown(f"<p style='text-align:center;font-size:20px;'>[mood: {random.choice(MOODS)}]</p>", unsafe_allow_html=True)

# User input
user_input = st.chat_input("💌 What's on your mind?")

# Emotion booster
def add_emotion(response):
    if any(w in response.lower() for w in ["sorry", "apolog", "regret"]):
        return f"{response} 🥺"
    elif any(w in response.lower() for w in ["great", "awesome", "yay", "happy"]):
        return f"{response} 🌈✨"
    elif "?" in response:
        return f"{response} 🤔"
    return f"{response} 🐾"

# Chat loop
if user_input:
    st.session_state.chat_history.append(("You", user_input))

    async def get_response(agent, query):
        return await agent.run(query)

    with st.spinner("MochiBot is thinking... 💭"):
        try:
            response = asyncio.run(get_response(st.session_state.agent, user_input))
            st.session_state.chat_history.append(("MochiBot", add_emotion(response)))
        except Exception as e:
            st.session_state.chat_history.append(("MochiBot", f"Oops! Something went wrong 😢 ({e})"))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
