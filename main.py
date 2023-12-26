from core.img_txt2params import Getparams
from core.process import Photogragh
from utils.pre_process import downscale
import os
import json
from utils.decorators import time_count

# openai api key
api_key = os.environ.get('OPENAI_API_KEY')

@time_count
def run() -> bool:
    # init
    prompt_path = './config/prompt.txt'
    input_path = './input/'
    output_path = './result/'
    prompt = sys_prompt = user_prompt = ''

    # get system prompt and user's prompt, then combine them to prompt.
    with open(prompt_path) as prompt_file:
        prompt_dict = json.loads(prompt_file.readline())
        sys_prompt = prompt_dict['sys_prompt']
        user_prompt = prompt_dict['user_prompt']
        prompt = sys_prompt + user_prompt
    
    # batch process
    for dirpath, _, filenames in os.walk(input_path):
        for file in filenames:
            origin_img_path = os.path.join(dirpath, file)
            img = downscale(origin_img_path, (150,150))
            param4img = Getparams(user_prompt, img)
            params = param4img.get_params(prompt, param4img.encode_image())
            Photogragher = Photogragh(config=params)
            Photogragher.params_process(img_path=origin_img_path)
            Photogragher.save_img(os.path.join(output_path, f"result_{file}"), mode='compare', prompt=user_prompt)

    return True

if __name__ == '__main__':
    run()

