import io
import numpy as np
from PIL import Image
import streamlit as st


uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
pixelsize = st.selectbox(
    'Pixel grid size',
    (256, 128, 64, 32), format_func=lambda x: f'{x}px')
colors = st.selectbox("Number of colors", (256, 128, 64, 32, 16, 8))

if uploaded_file:
    submit_button = st.button(label='Generate pixel art!')
    if uploaded_file and submit_button:
        img_raw = Image.open(uploaded_file)
        hsv_image = img_raw.convert("HSV")
        hue, saturation, value = hsv_image.split()
        threshold = 180
        saturation = saturation.point(lambda x: 255 if x > threshold else x)
        hsv_image = Image.merge("HSV", (hue, saturation, value))
        img = hsv_image.convert("RGB")
        size = img.size

        new_size = (size[0] * pixelsize // max(size), size[1] * pixelsize // max(size))

        img = img.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=colors)
        img = img.resize(new_size, resample=Image.NEAREST).quantize(colors=256, dither=Image.Dither.FLOYDSTEINBERG)

        img = img.resize(size, resample=Image.NEAREST)
        col1, col2 = st.columns(2)
        col1.image(img_raw)
        col2.image(img, channels='RGB')

        output = io.BytesIO()
        img.convert("RGB").save(output, format='JPEG')

        btn = st.download_button(
                label="Download image",
                data=output,
                file_name="pixel_art.png",
                mime="image/png"
            )
