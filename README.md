# gradio-image-generator
to make an Image generator using gradio - without cuda powered system.

# 🖼️ Image Generator using Gradio + Diffusers (CPU Compatible)

This project is a simple image generator built with [🤗 Hugging Face's Diffusers](https://github.com/huggingface/diffusers) and [Gradio](https://gradio.app/), designed to work on **CPU-only machines**.

> 🚫 No CUDA/GPU required — runs entirely on CPU (slower but compatible).

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2. **Install Dependencies**
pip install -r requirements.txt
--------------or---------------
2. **Install Manually**
pip install gradio diffusers transformers accelerate

🧠 Model Used: CompVis/stable-diffusion-v1-4 Loaded using the diffusers pipeline, Runs on CPU using PyTorch.
