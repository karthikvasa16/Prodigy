import streamlit as st
import re

def check_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r'\d', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Feedback messages
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, $, etc.).")

    # Overall strength
    strength = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria])
    
    return strength, feedback

# Streamlit app
st.title("Password Complexity Checker")

password = st.text_input("Enter a password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    if strength == 5:
        st.success("Your password is strong!")
    else:
        st.warning("Your password needs improvement.")
        for message in feedback:
            st.write(f"- {message}")
