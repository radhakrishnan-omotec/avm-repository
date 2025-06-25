import streamlit as st
import random
import re
import uuid

st.set_page_config(page_title="Authentication Basics Quiz", layout="centered")

st.title("🛡️ Cybersecurity Fundamentals: Authentication Basics Quiz")
st.subheader("Test your understanding of authentication methods and how they protect data from unauthorized access.")

# --- QUIZ QUESTION 1 ---
st.markdown("### 1. What does multi-factor authentication (MFA) use to improve security?")
q1 = st.radio("Choose one:", [
    "Only passwords",
    "Only biometrics",
    "Two or more independent verification factors",
    "Random token without login"
])
if q1 == "Two or more independent verification factors":
    st.success("✅ Correct! MFA uses different factor types like passwords + fingerprints.")
else:
    st.error("❌ Not quite. MFA uses more than one verification method.")

# --- QUIZ QUESTION 2: Password Strength ---
st.markdown("### 2. Try entering a strong password (simulate how systems test strength):")
password = st.text_input("Enter a sample password:")
if password:
    if len(password) < 8 or not re.search("[A-Z]", password) or not re.search("[0-9]", password) or not re.search("[!@#$%^&*()]", password):
        st.warning("⚠️ This password could be stronger. Try adding uppercase, numbers, and symbols.")
    else:
        st.success("✅ Strong password!")

# --- QUIZ QUESTION 3: OTP Simulation ---
st.markdown("### 3. Simulate MFA Login (Password + OTP)")
show_login = st.checkbox("Try MFA Login Simulation")
if show_login:
    username = st.text_input("Username:")
    user_pwd = st.text_input("Password:", type="password")
    if username == "student" and user_pwd == "Cyber123!":
        otp = random.randint(100000, 999999)
        st.info(f"📲 OTP sent: {otp} (simulated)")
        entered_otp = st.text_input("Enter OTP:")
        if entered_otp == str(otp):
            st.success("✅ Access granted!")
        elif entered_otp:
            st.error("❌ Incorrect OTP. Try again.")
    elif username or user_pwd:
        st.error("❌ Incorrect credentials.")

# --- QUIZ QUESTION 4: Match the Authentication Type ---
st.markdown("### 4. Match each authentication type with an example")
matches = {
    "Password": "Something you know",
    "Fingerprint": "Something you are",
    "Security token": "Something you have"
}
options = list(matches.keys())
user_matches = {}
for item in options:
    user_input = st.selectbox(f"What is '{item}'?", ["Select", "Something you know", "Something you are", "Something you have"], key=item)
    user_matches[item] = user_input

if all(user_matches[k] == v for k, v in matches.items()):
    st.success("✅ All matches correct!")
elif all(val != "Select" for val in user_matches.values()):
    st.warning("⚠️ Some answers are incorrect. Recheck the definitions.")

# --- QUIZ QUESTION 5: Token Authentication ---
st.markdown("### 5. Token Authentication: Generate your secure session token")
if st.button("Generate Token"):
    token = str(uuid.uuid4())
    st.code(f"Your token: {token}")
    st.success("✅ This token can now be used to access protected resources.")

# --- Score Feedback ---
st.markdown("---")
st.subheader("🎉 Great job!")
st.write("By completing this quiz, you've explored how authentication helps protect against unauthorized access, and how different methods work.")
st.markdown("> 💡 **Tip:** Try combining these techniques (like MFA + tokens) in your projects for added security!")

