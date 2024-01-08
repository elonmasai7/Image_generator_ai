input_image_path = "sunlit_lounge.png"
mask_image_path = "mask.png"
prompt_description = "A sunlit indoor lounge area with a pool containing a flamingo"

response = openai.Image.create_edit(
    image=open(input_image_path, "rb"),
    mask=open(mask_image_path, "rb"),
    prompt=prompt_description,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
