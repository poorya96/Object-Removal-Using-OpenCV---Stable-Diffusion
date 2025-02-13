from diffusers import StableDiffusionInpaintPipeline
import torch
from PIL import Image
import numpy as np

#Inpainting Stable Diffusion
pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting",
    torch_dtype=torch.float16,
)
pipe.to("cuda")  # GPU

# load image and mask
img = Image.open("fox-R.jpg").convert("RGB")  
mask = Image.open("fox-M.png").convert("L")  

#inpainting
result = pipe(
    prompt="background with no object", 
    image=img,
    mask_image=mask,
).images[0]

#save inpainted image
result.save("Stable Diffusion Inpainting/output.jpg")
