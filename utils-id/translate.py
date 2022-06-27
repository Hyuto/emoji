import json
import time
from tqdm import tqdm
from googletrans import Translator
from emoji.unicode_codes.data_dict import *

if __name__ == "__main__":
    translator = Translator()
    with open("result.json") as reader:
        result = json.load(reader)

    for emoji in tqdm(list(EMOJI_DATA.keys())[len(result.keys()):]):
        english = EMOJI_DATA[emoji]["en"]
        english = english.replace(":", "")
        english = english.replace("_", " ")
        try:
            temp = translator.translate(english, dest="id")
            indo = f':{temp.text.replace(" ", "_")}:'
            EMOJI_DATA[emoji]["id"] = indo
            result[emoji] = EMOJI_DATA[emoji]
            time.sleep(0.1)
        except:
            break

    with open("result.json", "w") as writer:
        writer.write(json.dumps(result))