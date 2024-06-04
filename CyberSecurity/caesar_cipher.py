import streamlit as st

def encrypt(text, s):
    res = ""
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            res += " "
            continue
        new_char = chr(ord(char) + s)
        if char.isupper():
            if ord(new_char) > ord('Z'):
                new_char = chr(ord('A') + (ord(new_char) - ord('Z')) - 1)
        else:
            if ord(new_char) > ord('z'):
                new_char = chr(ord('a') + (ord(new_char) - ord('z')) - 1)
        res += new_char
    return res

def decrypt(text, s):
    res = ""
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            res += " "
            continue
        new_char = chr(ord(char) - s)
        if char.isupper():
            if ord(new_char) < ord('A'):
                new_char = chr(ord('Z') - abs((ord(new_char) - ord('A'))) + 1)
        else:
            if ord(new_char) < ord('a'):
                new_char = chr(ord('z') - abs((ord(new_char) - ord('a'))) + 1)
        res += new_char
    return res

# Streamlit interface
st.title("Caesar Cipher Encryption and Decryption")

# Get user input
text = st.text_input("Enter the string:")
s = st.text_input("Enter shift value:")

if st.button("Encrypt"):
    encrypted_text = encrypt(text, int(s))
    st.write("Encrypted text:", encrypted_text)

if st.button("Decrypt"):
    decrypted_text = decrypt(text, int(s))
    st.write("Decrypted text:", decrypted_text)
