import streamlit as st
import requests
from PIL import Image
import base64
import io
import os

# FastAPI Endpoints
PORT = os.getenv("PORT", "8000")
API_URL = "https://enviroclass-605755972351.europe-west1.run.app"
WILDFIRE_API_URL = f"{API_URL}/predict-wildfire"
ENVIRONMENT_API_URL = f"{API_URL}/predict-environment"


# Setting Page Config
st.set_page_config(page_title="🔥 Wildfire Detection Service",
                   page_icon="🔥",
                   layout="wide")

# Title & Subtitle
st.title("Wildfire Detection Service")

st.markdown("""
### 🔥 WELCOME TO YOUR WILDFIRE & AREA DETECTION SERVICE 🔥


#### Stay Alert. Stay Safe. Protect Our Planet. 🌍
Are you concerned about wildfires? Do you want to **quickly analyze satellite images** to detect potential wildfire hazards?

This service allows you to **upload satellite images**, and our AI model will **instantly classify** them as:

- `WILDFIRE` or `NO WILDFIRE`

If a **Wildfire** is predicted, determine in which **Area** it has been detected:

- `Agriculture`
- `Airport`
- `Beach`
- `City`
- `Desert`
- `Forest`
- `Grassland`
- `Highway`
- `Lake`
- `Mountain`
- `Parking`
- `Port`
- `Railway`
- `River`


---

### **HOW DOES IT WORK? 🛰️**


1️⃣ **Upload or select a satellite image** (JPG or PNG)

2️⃣ **Click 'Analyze Image'** to start the detection

3️⃣ **Get AI results:** `"No wildfire"` or e.g. `"Wildfire in River Area"`


""")

# image selection
st.markdown("### 📸 Choose an Image for Analysis")
option = st.radio("Select an option:", ("Upload your own image", "Choose a sample image"))

image = None
if option == "Upload your own image":
    uploaded_image = st.file_uploader("Choose an image file...", type=["jpg", "png", "jpeg"])
    if uploaded_image:
        image = Image.open(uploaded_image)

elif option == "Choose a sample image":
    sample_image = [f"media/image{i}.jpg" for i in range(1, 11)]
    selected_image = st.selectbox("Select a sample image:", sample_image)
    if selected_image:
        image = Image.open(selected_image)

# Prediction
if image:
    st.image(image, caption="Selected Image", use_container_width=True)

    if st.button("🔥 Analyze Image"):
        with st.spinner("⏳ Processing your image... Please wait."):

            # Convering image
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="JPEG")
            img_bytes = img_bytes.getvalue()
            files = {"file": img_bytes}

            # STEP 1: Sending image --> Wildfire API
            try:
                wildfire_response = requests.post(WILDFIRE_API_URL, files=files)
                wildfire_response.raise_for_status()
                wildfire_result = wildfire_response.json()

                # Extracting wildfire prediction
                wildfire_prediction = wildfire_result["wildfire_prediction"]
                wildfire_confidence = wildfire_result["wildfire_confidence"]


                st.success(f"🔥 Prediction: **{wildfire_prediction.upper()}**")
                st.info(f"✅ Confidence Score: **{wildfire_confidence * 100:.2f}%**")

                if wildfire_prediction == "wildfire":
                    st.error("⚠️ ALERT! This image shows signs of a wildfire.")


            # STEP 2: Sending image --> Environment API
                    try:
                        environment_response = requests.post(ENVIRONMENT_API_URL, files=files)
                        environment_response.raise_for_status()
                        environment_result = environment_response.json()

                        # Extracting environment prediction
                        detected_objects = environment_result.get("environment_prediction", [])

                        # Displaying environment prediction
                        if detected_objects:
                            st.warning("🌍 **Detected Environment Areas:**")

                            # Extracting class names
                            area_names = [obj["class"] for obj in detected_objects]
                            formatted_areas = ", ".join(area_names)

                            for obj in detected_objects:
                                st.write(f"🔎 **{obj['class'].upper()}** (Confidence: {obj['confidence'] * 100:.2f}%)")

            # STEP 3: Final prediction  + image
                            st.success(f"🔎 Final Prediction: **Wildfire in {formatted_areas} Area**")

                        # Retrieveing + displaying annotated image
                        if "annotated_image" in environment_result:
                            image_data = base64.b64decode(environment_result["annotated_image"])
                            detected_image = Image.open(io.BytesIO(image_data))
                            st.image(detected_image, caption="📸 Image with Detected Objects", use_container_width=True)
                        else:
                            st.warning("📍 No detected objects found.")

                    except requests.exceptions.RequestException as e:
                        st.error(f"⚠️ Error fetching environment classification: {str(e)}")

                else:
                    st.success("✅ No wildfire detected. Stay safe!")

            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Error connecting to wildfire prediction API: {str(e)}")
