import streamlit as st
from PIL import Image
import numpy as np

def encrypt(image, key):
    image_data = np.array(image)
    for index, values in enumerate(image_data):
        image_data[index] = values ^ key
    encrypted_image = Image.fromarray(image_data)
    return encrypted_image

def decrypt(image, key):
    image_data = np.array(image)
    for index, values in enumerate(image_data):
        image_data[index] = values ^ key
    decrypted_image = Image.fromarray(image_data)
    return decrypted_image

# Streamlit app
st.title("Image Encryption and Decryption")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    key = 123

    # Load the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Encrypt'):
        encrypted_image = encrypt(image, key)
        encrypted_image.save('encrypted_image.png')
        st.success('Image Encrypted Successfully.')
    st.image('encrypted_image.png')
    if st.button('Decrypt'):
        encrypted_image = Image.open('encrypted_image.png')
        decrypted_image = decrypt(encrypted_image, key)
        decrypted_image.save('decrypted_image.png')
        st.success('Image Decrypted Successfully.')
    st.image('decrypted_image.png')
