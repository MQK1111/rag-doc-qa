import os
import requests

api_key = os.environ.get("ZHIPU_API_KEY")
print("读到的key：", api_key)

url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

data = {
    "model": "glm-4-flash",
    "messages": [
        {"role": "user", "content": "用一句话介绍你自己"}
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)
import os
import requests

api_key = os.environ.get("ZHIPU_API_KEY")

url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

data = {
    "model": "glm-4-flash",
    "messages": [
        {"role": "user", "content": "重庆有哪里好玩的地方？"}
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
if "error" in result:
    print("出错了：", result["error"]["message"])
else:
    print(result["choices"][0]["message"]["content"])