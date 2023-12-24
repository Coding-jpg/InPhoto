from core.img_txt2params import Getparams
from core.process import Photogragh
from utils.pre_process import downscale
import os
import json
import time

# openai api key
api_key = os.environ.get('OPENAI_API_KEY')

def run():
    # init
    sys_prompt_path = './config/sys_prompt.txt'
    input_path = './input/'
    output_path = './result/'
    sys_prompt = user_prompt = ''

    # get system prompt and user's prompt, then combine them to prompt.
    with open(sys_prompt_path) as sys_file:
        prompt_dict = json.loads(sys_file.readline())
        sys_prompt = prompt_dict['sys_prompt']
        user_prompt = prompt_dict['user_prompt']
        prompt = sys_prompt + user_prompt
    
    # batch process
    for dirpath, dirnames, filenames in os.walk(input_path):
        for file in filenames:
            origin_img_path = os.path.join(dirpath, file)
            img_path = downscale(origin_img_path, (150,150), output_path)
            param4img = Getparams(user_prompt, img_path)
            params = param4img.get_params(prompt, param4img.encode_image())
            os.remove(img_path)
            Photogragher = Photogragh(config=params)
            Photogragher.params_process(img_path=origin_img_path)
            Photogragher.save_img(os.path.join(output_path, f"result_{file}"))
        
    # image_path = "./small_img_2.jpg"
    # prompt_path = "./config/sys_prompt.txt"
    # user_prompt = "so lonely"
    # param4img = Getparams(user_prompt, image_path)
    # params = param4img.get_params(param4img.combine_prompt(prompt_path), param4img.encode_image())
    

if __name__ == '__main__':
    run()

