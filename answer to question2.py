import streamlit as st
import random

st.set_page_config(page_title="විස්මිත පුවරුව 36", layout="wide")

# CSS - පෙනුම සහ Animation (Flip Effect)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%); }
    
    /* කොටු වල පෙනුම */
    .stButton > button {
        width: 100%; height: 90px;
        background: white !important;
        color: #4834d4 !important;
        font-size: 28px !important;
        font-weight: bold;
        border-radius: 15px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.6s;
    }

    /* මූසිකය ගෙන ගිය විට කැරකීම */
    .stButton > button:hover {
        transform: rotateY(180deg) scale(1.05);
        background: #6c5ce7 !important;
        color: white !important;
    }

    .card {
        background: white; padding: 30px; border-radius: 25px;
        text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 20px; border-top: 8px solid #6c5ce7;
    }
    </style>
""", unsafe_allow_html=True)

# ප්‍රශ්න සහ නිවැරදි පිළිතුරු බැංකුව (මෙහි පිළිතුරත් ඇතුළත් කර ඇත)
def get_q_and_a(n):
    data = {
        4: {"q": "16 හි වර්ගමූලය කීයද?", "a": "4"},
        7: {"q": "සතියකට ඇති දින ගණන කීයද?", "a": "7"},
        12: {"q": "අවුරුද්දකට ඇති මාස ගණන කීයද?", "a": "12"},
        32: {"q": f"අංක 32 ට අදාළ රහස් ගැටලුව: {n} x 2 කීයද?", "a": "64"},
        36: {"q": "6 වරක් 6 කීයද?", "a": "36"}
    }
    # ලැයිස්තුවේ නැති අංක සඳහා ස්වයංක්‍රීය පිළිතුරක්
    if n in data:
        return data[n]
    else:
        return {"q": f"අංක {n} ට අදාළ ප්‍රශ්නය: {n} + 10 කීයද?", "a": str(n + 10)}

if 'active_n' not in st.session_state:
    st.session_state.active_n = None
    st.session_state.secret_code = None

st.markdown("<h1 style='text-align:center;'>🧩 අංක 36ක විස්මිත කැරකෙන පුවරුව</h1>", unsafe_allow_html=True)

# Grid එක
cols = st.columns(6)
for i in range(1, 37):
    with cols[(i-1) % 6]:
        if st.button(f"{i}", key=f"t_{i}"):
            st.session_state.active_n = i
            st.session_state.secret_code = random.randint(100, 999)

# ක්‍රියාවලිය
if st.session_state.active_n:
    st.markdown("---")
    st.markdown(f"<div class='card'><h2>තේරූ අංකය: {st.session_state.active_n}</h2><h1 style='color:#d63031;'>රහස් කේතය: {st.session_state.secret_code}</h1></div>", unsafe_allow_html=True)
    
    code_in = st.text_input("රහස් කේතය මෙහි ලියන්න:", key="code_in")
    
    if code_in == str(st.session_state.secret_code):
        q_data = get_q_and_a(st.session_state.active_n)
        st.markdown(f"<div class='card' style='border-color:#00b894;'><h3>💡 ප්‍රශ්නය:</h3><h1>{q_data['q']}</h1></div>", unsafe_allow_html=True)
        
        ans_in = st.text_input("ඔබේ පිළිතුර මෙහි ලියන්න:", key="ans_in")
        
        # පිළිතුර පරීක්ෂා කරන කොටස (මෙහිදී තමයි හරි/වැරදි කියන්නේ)
        if ans_in:
            if ans_in.strip() == q_data['a']:
                st.balloons()
                st.success("නියමයි! පිළිතුර නිවැරදියි. 🎉")
            else:
                st.error("පිළිතුර වැරදියි, නැවත උත්සාහ කරන්න! ❌")
