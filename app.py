import streamlit as st
import tensorflow as tf
import numpy as np
from huggingface_hub import hf_hub_download

@st.cache_resource  # Cache model download and load
def load_model():
    model_path = hf_hub_download(repo_id="dhr-uuu34/trained_model", filename="trained_model.keras")
    model = tf.keras.models.load_model(model_path)
    return model

model = load_model()

# Tensorflow Model Prediction
def model_prediction(test_image):
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# Home Page
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "home_page.jpeg"
    st.image(image_path, use_column_width=True)  # changed from use_column_width
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍
    ...
    """)

# About Page
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Dataset
    ...
    """)

# Prediction Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if st.button("Show Image") and test_image is not None:
        st.image(test_image, use_container_width=True)
    if st.button("Predict") and test_image is not None:
        with st.spinner("Please Wait..."):
            st.write("Our Prediction")
            result_index = model_prediction(test_image)
            # Define Class
            class_name = ['Apple___Apple_scab',
                          'Apple___Black_rot',
                          'Apple___Cedar_apple_rust',
                          'Apple___healthy',
                          'Blueberry___healthy',
                          'Cherry_(including_sour)___Powdery_mildew',
                          'Cherry_(including_sour)___healthy',
                          'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                          'Corn_(maize)___Common_rust_',
                          'Corn_(maize)___Northern_Leaf_Blight',
                          'Corn_(maize)___healthy',
                          'Grape___Black_rot',
                          'Grape___Esca_(Black_Measles)',
                          'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                          'Grape___healthy',
                          'Orange___Haunglongbing_(Citrus_greening)',
                          'Peach___Bacterial_spot',
                          'Peach___healthy',
                          'Pepper,_bell___Bacterial_spot',
                          'Pepper,_bell___healthy',
                          'Potato___Early_blight',
                          'Potato___Late_blight',
                          'Potato___healthy',
                          'Raspberry___healthy',
                          'Soybean___healthy',
                          'Squash___Powdery_mildew',
                          'Strawberry___Leaf_scorch',
                          'Strawberry___healthy',
                          'Tomato___Bacterial_spot',
                          'Tomato___Early_blight',
                          'Tomato___Late_blight',
                          'Tomato___Leaf_Mold',
                          'Tomato___Septoria_leaf_spot',
                          'Tomato___Spider_mites Two-spotted_spider_mite',
                          'Tomato___Target_Spot',
                          'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                          'Tomato___Tomato_mosaic_virus',
                          'Tomato___healthy']
            st.success("Model is Predicting it's a **{}**".format(class_name[result_index]))
