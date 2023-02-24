# Pixel Art Generator

In this project @piEsposito and I developed a simple code that can transform any image in pixel art. We were inspired by [pixelicious](https://www.pixelicious.xyz/) and our main idea is not to create a concurrent solution, but just explain how it works behind the scenes and have fun 😜.

## How it works?

We don't use AI here, only classical computer vision to make everything work.
The pipeline that we proposed was inspired in this excellent [article](https://dev.to/miguelmj/make-it-pixel-make-pixel-art-from-any-image-2o4n). To perform the trasnformation we applied the following steps:

- Preprocess the image to make it slightly better to become a pixel art. For this, we add more weight to strong color (pixel value > 180);
- Downscale the image to a choosen pixel grid size;
- Convert the image to a pallete mode;
- Apply color quantization and dithering;
- Upscale the image to the original size.

## How can you test?

You can run by yourself if you want, just using the following two commands:

`pip install streamlit Pillow numpy`

`streamlit run pixel_art_app.py`

Or you can test it on [Hugging Face Space](https://huggingface.co/spaces/pedrogengo/pixel_art).