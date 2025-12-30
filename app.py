import streamlit as st
import streamlit as st

PASSWORD = "how you feeling"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    entered = st.text_input("For Kanmani ", type="password")


    if entered == PASSWORD:
        st.session_state.authenticated = True
        st.rerun()
    else:
        st.stop()


# --- Data ---
solutions = {
    "headache": "Try resting and using a warm compress. If needed, a mild painkiller can help.",
    "stomach-ache": "Drink warm water and avoid spicy food",
    "migraine": "Stay in a dark room and hydrate",
    "overthinking": "Play this(https://www.youtube.com/watch?v=7wAb8_STOs4) , If doesnt work then Contact chinnu",
    "fever": "Take rest and drink fluids",
    "anxiety": "Immediately contact chinnu",
    "scared": "Immediately contact chinnu",
    "anxious": "Immediately contact chinnu",
    "period": "Apply heat , drink something warm , If any moodswings contact chin",
    "stress": "Try slowing down, deep breathing, and taking short breaks.",
"low mood": "Be kind to yourself today. Talking to someone you trust can help.",
"lonely": "You’re not alone. Reach out to someone(me) or do something comforting(also me do me).",
"panic": "Slow breathing can help. Try inhaling for 4 seconds, exhaling for 6.",
"burnout": "You may need rest. Try stepping away and recharging.",
    "bored": "Try this https://www.clickastro.com/?ref=logo",
    "back pain": "Gentle stretching and rest may help. Avoid heavy lifting.",
"neck pain": "Try light stretches and check your posture.",
"body ache": "Rest, fluids, and light movement may reduce discomfort.",
"muscle pain": "Gentle stretching and rest can help recovery.",
"nausea": "Small sips of water and rest may help.",
"indigestion": "Avoid heavy food and eat slowly. Stop trying to eat fast fast slowwwwly bite everything for 30 bites at start",
"acidity": "Try avoiding spicy food and lying down immediately after eating.",
"constipation": "Hydration and fiber-rich foods may help. Eat banana or orange",
    "cold": "Rest, fluids, and warmth can help recovery.",
"cough": "Warm fluids and rest may soothe irritation.",
"sore throat": "Warm drinks and rest may help.",
"dizziness": "Sit or lie down and hydrate. Seek help if it persists.",
"lazy": "It’s okay to rest. Start with one small task. Use the 3 2 1 GO GO  GO !!!!! ",
"unmotivated": "Do one tiny thing — momentum follows.",
"confused": "Pause, write things down, and take it step by step.",
"opika ledu": "Lie down take rest shut all devices and try to sleep for a while (inform chin before doing this mf will lose his mind without u.",
"overwhelmed": "Slow down and handle one thing at a time. Stop multitasking yes even listening to music STOP just do one thing at a time or go out get a cup of tea or coffee."
}

st.set_page_config(page_title="Therapist Bot", page_icon="🩺")

st.title("🩺 Therapist Bot")
st.write("Type how you feel (sentences are fine). I’ll pick up keywords like **headache**, **fever**, **anxiety**, etc.")

text = st.text_input("Describe what you're feeling:", placeholder="e.g. I'm bored and I have a headache...").strip().lower()

col1, col2 = st.columns(2)

with col1:
    check = st.button("Get Advice")

with col2:
    clear = st.button("Clear")

if clear:
    st.rerun()

if check:
    if not text:
        st.warning("Please type something first.")
    else:
        found = False

        st.write("relax cutie baby chin made me precisely for this 💖")

        for key, advice in solutions.items():
            if key in text:
                st.markdown(f"• **{key.capitalize()}** — {advice}")
                found = True

        if not found:
            st.info("I couldn’t understand that. If you want emotional support contact Chin OR Try saying things like headache, fever, anxiety, bored…")

st.caption("Cutie ma I miss you come talk to me 🥺🥺.")














