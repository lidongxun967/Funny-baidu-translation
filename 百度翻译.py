import requests,hashlib,random,json
from tqdm import tqdm

with open("opt.json","r") as t:
    tz = json.loads(t.read())



APPID = tz["APPID"]
SECRET_KEY = tz["SECRET_KEY"]
LANGUAGES = ["en", "jp", "fra", "de", "ru", "kor", "th", "spa", "pt", "it", "el", "nl", "pl", "bul", "est", "ar", "he", "hi", "id", "ms", "fa", "tr", "vi", "th"]

def translate(text, target_language="en", source_language="auto"):
    url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
    salt = str(random.randint(32768, 65536))
    sign = hashlib.md5((APPID + text + salt + SECRET_KEY).encode("utf-8")).hexdigest()
    params = {
        "q": text,
        "from": source_language,
        "to": target_language,
        "appid": APPID,
        "salt": salt,
        "sign": sign
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return json.loads(response.text)["trans_result"][0]["dst"]
    else:
        return "翻译失败！"

text = input("请输入中文：")
n = int(input("请输入循环次数："))
target_language = random.choice(LANGUAGES)
for i in tqdm(range(n)):
    en_text = translate(text, target_language)
    text = translate(en_text, "zh")
print(f"{target_language.upper()}翻译为中文：{text}")
input()
