import gradio as gr
from diffusers import StableDiffusionPipeline
import torch

# Load the model and move to CPU
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cpu")  # Use CPU instead of GPU

def generate(prompt):
    image = pipe(prompt).images[0]
    return image

gr.Interface(fn=generate, inputs=gr.Textbox(label="Prompt"), outputs=gr.Image()).launch()
