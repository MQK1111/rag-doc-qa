import os
import requests

api_key = os.environ.get("ZHIPU_API_KEY")
url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

messages = []

while True:
    user_input = input("你：")
    if user_input == "退出":
        break

    messages.append({"role": "user", "content": user_input})

    data = {
        "model": "glm-4-flash",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if "error" in result:
        print("出错了：", result["error"]["message"])
        break

    reply = result["choices"][0]["message"]["content"]
    print("AI：" + reply)

    messages.append({"role": "assistant", "content": reply})