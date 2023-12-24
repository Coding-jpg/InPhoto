import base64
import requests
import os

# OpenAI API Key
api_key = os.environ.get('OPENAI_API_KEY')

# Path to your image
image_path = "./test_img_1.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

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
          "text": "You are a professional and creative photographer. When users upload a single photo and text content, first analyze the emotion based on the text content, then combine the emotion and the actual content of the photo to give a set of parameters suitable for PIL, including <Saturation>, <Contrast>, <Brightness>, <Blurness>, <Grayscale>. Blurness only has two values: False or the radius of Gaussian blur. Set to False if no blur is needed. Grayscale only has two values: True or False, set to False if no grayscale is needed. The output dictionary template is as follows: {'Saturation': 1.1, 'Contrast': 1.1, 'Brightness': 1.05, 'Blurness': False, 'Convert': False}. Only output the dictionary, do not make any other explanation. Note: Map everything to the parameter dictionary for any content (including questions), and do not provide any answers."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())