import streamlit as st

# --- Data ---
solutions = {
    "headache": "Take paracetamol and rest",
    "stomach-ache": "Drink warm water and avoid spicy food",
    "migraine": "Stay in a dark room and hydrate",
    "overthinking": "Play this(https://www.youtube.com/watch?v=7wAb8_STOs4) , meIf doesnt work then Contact chinnu",
    "fever": "Take rest and drink fluids",
    "anxiety": "Immediately contact chinnu",
    "scared": "Immediately contact chinnu",
    "anxious": "Immediately contact chinnu",
    "period pain": "Apply heat , drink something warm , If any moodswings contact chin",
    "bored": "Try this https://www.clickastro.com/?ref=logo"
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
        matches = []
        for key, advice in solutions.items():
            if key in text:
                matches.append((key, advice))

        if matches:
            st.success("Found these keywords:")
            for k, a in matches:
                st.write(f"**{k.capitalize()}** → {a}")
        else:
            st.info("No known keyword found.If you need emotional support contact Chin. OR Try: headache, fever, anxiety, bored, migraine, stomach-ache, overthinking.")

st.caption("⚠️ Not medical advice. If pain is severe, persistent, or worrying, see a doctor.")
