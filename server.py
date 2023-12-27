from fastapi import FastAPI
from pydantic import BaseModel
from PIL import Image
from io import BytesIO
import base64
from core.img_txt2params import Getparams
from core.process import Photogragh
from utils.pre_process import downscale
import json

# Create Instance
app = FastAPI()

# Data Model
class data(BaseModel):
    img: str
    prompt: str

# Route
@app.post("/v1/")
def post_process(item:data):
    try:
        # combine prompt
        with open('./config/prompt.txt') as prompt_file:
            prompt_dict = json.loads(prompt_file.readline())
            sys_prompt = prompt_dict['sys_prompt']
            prompt = sys_prompt + item.prompt

        # decode base64 to PIL Image
        img_data = base64.b64decode(item.img)
        origin_img = Image.open(BytesIO(img_data))

        # post_process
        img = downscale(origin_img, (150,150))
        param4img = Getparams(item.prompt, img)
        params = param4img.get_params(prompt, param4img.encode_image())
        Photogragher = Photogragh(config=params)
        Photogragher.params_process(img2process=origin_img)
        result_base64_str = Photogragher.return_base64_str_result()

        return {"res_img":f"{result_base64_str}"}
    except Exception as e:
        print(f"Failed to load server, {e}")