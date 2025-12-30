import streamlit as st
import random

st.set_page_config(page_title="විස්මිත පුවරුව 36 - Sound Edition", layout="wide")

# JavaScript මගින් ශබ්ද පාලනය (Sound Effects)
def play_sound(url):
    st.components.v1.html(f"""
        <audio autoplay>
            <source src="{url}" type="audio/mp3">
        </audio>
    """, height=0)

# CSS - Animation සහ පෙනුම
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .stButton > button {
        width: 100%; height: 90px;
        background: white !important;
        color: #4834d4 !important;
        font-size: 28px !important;
        font-weight: bold;
        border-radius: 15px;
        transition: all 0.4s ease;
        border: none;
    }
    .stButton > button:hover {
        transform: rotateY(180deg) scale(1.1);
        background: #00b894 !important;
        color: white !important;
    }
    .card {
        background: rgba(255, 255, 255, 0.9);
        padding: 30px; border-radius: 25px;
        text-align: center; margin-top: 20px;
        border-bottom: 8px solid #6c5ce7;
    }
    </style>
""", unsafe_allow_html=True)

# ප්‍රශ්න සහ පිළිතුරු බැංකුව
def get_q_and_a(n):
    data = {
        4: {"q": "16 හි වර්ගමූලය කීයද?", "a": "4"},
        7: {"q": "සතියකට ඇති දින ගණන කීයද?", "a": "7"},
        12: {"q": "අවුරුද්දකට ඇති මාස ගණන කීයද?", "a": "12"},
        32: {"q": "32 x 2 කීයද?", "a": "64"}
    }
    if n in data: return data[n]
    return {"q": f"{n} + 10 කීයද?", "a": str(n+10)}

if 'active_n' not in st.session_state:
    st.session_state.active_n = None
    st.session_state.secret_code = None

st.markdown("<h1 style='text-align:center; color:white;'>🧩 විස්මිත ශබ්ද පුවරුව 36</h1>", unsafe_allow_html=True)

# Grid එක
cols = st.columns(6)
for i in range(1, 37):
    with cols[(i-1) % 6]:
        if st.button(f"{i}", key=f"t_{i}"):
            st.session_state.active_n = i
            st.session_state.secret_code = random.randint(100, 999)
            # Click කරන විට ඇසෙන ශබ්දය
            play_sound("https://www.soundjay.com/buttons/button-3.mp3")

if st.session_state.active_n:
    st.markdown(f"<div class='card'><h2>තේරූ අංකය: {st.session_state.active_n}</h2><h1 style='color:#d63031;'>කේතය: {st.session_state.secret_code}</h1></div>", unsafe_allow_html=True)
    
    code_in = st.text_input("රහස් කේතය ටයිප් කරන්න:", key="code_in")
    
    if code_in == str(st.session_state.secret_code):
        q_data = get_q_and_a(st.session_state.active_n)
        st.markdown(f"<div class='card' style='border-color:#00b894;'><h3>💡 ප්‍රශ්නය:</h3><h1>{q_data['q']}</h1></div>", unsafe_allow_html=True)
        
        ans_in = st.text_input("ඔබේ පිළිතුර:", key="ans_in")
        
        if ans_in:
            if ans_in.strip() == q_data['a']:
                st.balloons()
                st.success("නිවැරදියි! 🎉")
                # ජයග්‍රහණය කළ විට ඇසෙන ශබ්දය
                play_sound("https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3")
            else:
                st.error("වැරදියි! ❌")
                # වැරදුණු විට ඇසෙන ශබ්දය
                play_sound("https://www.soundjay.com/buttons/button-10.mp3")
