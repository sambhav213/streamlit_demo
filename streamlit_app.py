import streamlit as st
import cv2
from PIL import Image
import numpy as np

def main():
    st.title("OpenCV Streamlit App")
    st.write("Upload an image and choose an operation from the dropdown menu.")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Convert uploaded image to OpenCV format
        img = np.array(Image.open(uploaded_image))

        # Operations dropdown
        operations = st.sidebar.selectbox("Choose operation:", ["Grayscale", "Edge Detection"])

        if operations == "Grayscale":
            # Convert image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            st.image(gray, caption="Grayscale Image", use_column_width=True)

        elif operations == "Edge Detection":
            # Perform edge detection
            edges = cv2.Canny(img, 100, 200)
            st.image(edges, caption="Edge Detection", use_column_width=True)

if __name__ == "__main__":
    main()
