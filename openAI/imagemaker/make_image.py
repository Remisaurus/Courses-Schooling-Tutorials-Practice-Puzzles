import openai
from base64 import b64decode
from pathlib import Path

IMAGE_DIR = Path.cwd() / "images" 
PROMPT = "Cartoony character shivering while sleeping in a bed with a pitch black background"

IMAGE_DIR.mkdir(exist_ok=True)

openai.api_key_path = 'C:\Temp\OpenAI_API_KEY_.txt'

response = openai.Image.create(
    prompt=PROMPT,
    n=1, # number of images created.
    size="1024x1024", # either "256x256", "512x512", or "1024x1024" in string
    response_format="b64_json",
)

print('Image created')

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = IMAGE_DIR / f"{PROMPT[:5]}-{response['created']}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)