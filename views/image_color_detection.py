import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

def run():
    st.subheader("📁 Upload an Image")

    # Load color data
    index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
    df = pd.read_csv("data/colors.csv", header=None, names=index)

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open image and convert to RGB
        original_img = Image.open(uploaded_file).convert("RGB")

        # Resize if too large
        max_width = 600
        if original_img.width > max_width:
            w_percent = max_width / float(original_img.width)
            h_size = int((float(original_img.height) * w_percent))
            resized_img = original_img.resize((max_width, h_size), Image.Resampling.LANCZOS)
        else:
            resized_img = original_img

        img_np = np.array(resized_img)

        # Show image and get click coordinates
        coords = streamlit_image_coordinates(resized_img, key="image_picker")

        def get_color_name(R, G, B):
            min_dist = float('inf')
            closest = ""
            for i in range(len(df)):
                d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
                if d < min_dist:
                    min_dist = d
                    closest = f'{df.loc[i, "color_name"]} | Hex: {df.loc[i, "hex"]}'
            return closest

        if coords is not None:
            x = int(coords["x"])
            y = int(coords["y"])
            if 0 <= x < img_np.shape[1] and 0 <= y < img_np.shape[0]:
                r, g, b = img_np[y, x]
                color_name = get_color_name(r, g, b)

                st.markdown(f"### 🎨 Color Name: `{color_name}`")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f'<div style="width: 120px; height: 50px; background-color: rgb({r},{g},{b});'
                    f'border: 1px solid #000; margin-top: 10px"></div>',
                    unsafe_allow_html=True
                )
            else:
                st.warning("⚠️ Clicked coordinates are outside the image bounds.")
    else:
        st.info("📷 Please upload an image to begin.")
