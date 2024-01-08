image_path = "sunlit_lounge.png"
mask_path = "mask.png"
prompt_text = "A sunlit indoor lounge area with a pool containing a flamingo"

edit_params = {
    "image": open(image_path, "rb"),
    "mask": open(mask_path, "rb"),
    "prompt": prompt_text,
    "n": 1,
    "size": "1024x1024"
}

response = openai.Image.create_edit(**edit_params)

image_url = response['data'][0]['url']
