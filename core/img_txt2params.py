import base64
import requests
import os
import json
from utils.decorators import log

# OpenAI API Key
api_key = os.environ.get('OPENAI_API_KEY')

class Getparams():
  '''get params from image and text content.'''
  def __init__(self, user_prompt:str, img_path:str) -> None:
    self.user_prompt = user_prompt
    self.img_path = img_path

  def encode_image(self) -> base64:
    with open(self.img_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')
  
  @log
  def get_params(self, prompt:str, img:base64) -> dict:

    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
      "model": "gpt-4-vision-preview",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{img}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
    }

    try:
      response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    except Exception as req_e:
      print(f"Faild to request, {req_e}")

    params = response.json()['choices'][0]['message']['content'].replace("'",'"')
    params = json.loads(params)
    
    return params
  

if __name__ == '__main__':
  image_path = "./small_img_2.jpg"
  sys_prompt_path = "./config/sys_prompt.txt"
  user_prompt_path = "./config/user_prompt.txt"

  param4img = Getparams(user_prompt_path, image_path)

  params = param4img.get_params(param4img.combine_prompt(sys_prompt_path), param4img.encode_image())
 
  