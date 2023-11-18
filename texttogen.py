import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}
st.title("image Generation")
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
prompt=st.text_input("Enter")
bt=st.button("Enter")
if bt:
	
    image_bytes = query({
        "inputs": prompt,
    })
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    images = Image.open(io.BytesIO(image_bytes))
    st.image(images)