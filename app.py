import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Color Detection App", layout="centered")

# ✅ Corrected module import (from 'modules', not 'pages')
from views import image_color_detection, webcam_color_detection

# App title
st.title("🎨 Color Detection App")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Image Color Picker", "Webcam Color Picker"],
        icons=["house-fill", "image-fill", "camera-fill"],
        default_index=0,
    )

# Page routing
if selected == "Home":
    st.markdown(
        """
        ## Welcome to the **Color Detection App**!  
        
        This simple yet powerful tool helps you identify and understand colors in any image. Whether you're a designer, developer, artist, or just curious about colors — this app is for you!

        ### 🔍 What can you do here?

        - 📁 **Upload an image** from your device and click anywhere to get the color name, RGB values, and Hex code.
        - 📷 **Capture a photo** using your webcam and analyze colors in real-time.
        - 🖱️ Interact with the image to **detect color at any pixel**.
        - 🧠 Leverage our intelligent algorithm to match the pixel color to the **closest known color name**.

        ### 💡 How to Use

        1. Use the **sidebar** to select either:
            - **Upload Image**
            - **Capture from Webcam**
        2. Follow the on-screen instructions to load your image.
        3. Click anywhere on the image to reveal detailed color information.

        ### 🧰 Applications

        - UI/UX Design
        - Graphic Design
        - Painting & Fine Art
        - Photography Editing
        - Web Development

        > ⚠️ **Note:** The color detection may slightly vary depending on image lighting and resolution.

        ---
        👈 Use the **sidebar** to get started. Have fun exploring colors!
        """
    )

elif selected == "Image Color Picker":
    image_color_detection.run()

elif selected == "Webcam Color Picker":
    webcam_color_detection.run()
