import tensorflow as tf
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

IMAGE_SHAPE = (224, 224)

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Dogs and Cats Predictor")

def load_and_prep_image(image):
    """
    Reads an image from filename, turns it into a tensor and reshapes it to (img_shape, img_shape,, color_channels)
    """
    # Read in the image
    # img = tf.io.read_file(filename)
    # Decode the read file into a tensor
    image = tf.image.decode_image(image)
    # Resize the image  
    image = tf.image.resize(image, size=IMAGE_SHAPE)
    #Grayscale
    if image.shape[2] == 1:
        image = tf.image.grayscale_to_rgb(image)
        # Rescale the image (getting all values between 0 & 1)
        # image = image/255

    return image

def url_uploader():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.text("Provide Url for animal detection")

    @st.cache(allow_output_mutation=True)
    def load_model():
        model = tf.keras.models.load_model("DOGvsCAT_Model")
        return model
    
    with st.spinner('Loading model into memmory...'):
        model = load_model()

    classes = ['CAT', 'DOG']
    
    path = st.text_input("Enter image Url to classify...", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfZi6q5elXyTE38nTQQnrAYl2Vrl5b_dcxOQ&usqp=CAU")
    if path is not None:
        content = requests.get(path).content

        st.write("Predicted Class :")
        with st.spinner("Classifying....."):
            img = load_and_prep_image(content)
            label = model.predict(tf.expand_dims(img, axis=0))
            st.write(classes[int(tf.argmax(tf.squeeze(label).numpy()))])

        st.write("")
        image = Image.open(BytesIO(content))
        st.image(image, caption="Classifying the animal", use_column_width=True)


def file_Uploader():
    file = st.file_uploader("Upload file", type=["png", "jpeg", "jpg"])
    show_file = st.empty()

    @st.cache(allow_output_mutation=True)
    def load_model():
        model = tf.keras.models.load_model("DOGvsCAT_Model")
        return model
    
    with st.spinner('Loading model into memmory...'):
        model = load_model()

    if not file:
        show_file.info("Upload a picture of an animal you want to be predicted.")
        return

    content = file.getvalue()

    classes = ['CAT', 'DOG']  

    st.write("Predicted Class :")
    with st.spinner("Classifying....."):
         img = load_and_prep_image(content)
         label = model.predict(tf.expand_dims(img, axis=0))
         st.write(classes[int(tf.argmax(tf.squeeze(label).numpy()))])
    st.write("")
    image = Image.open(BytesIO(content))
    st.image(image, caption="Classifying the animal", use_column_width=True)

st.sidebar.header('Choose how you want to upload a file')
# st.sidebar.write("URL - To predict from a link, \n File Upload - To predict from a file present on your device")
function = st.sidebar.selectbox('URL or File Upload',('URL','File Upload'))

if function == 'URL':
    url_uploader()
else :
    file_Uploader()