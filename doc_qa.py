import os
import requests

api_key = os.environ.get("ZHIPU_API_KEY")
url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

# 读取本地文档
with open("notes.txt", "r", encoding="utf-8") as f:
    document = f.read()

print("已读取文档，内容如下：")
print(document)
print("-" * 30)

while True:
    question = input("你：")
    if question == "退出":
        break

    # 把文档和问题一起发给模型
    prompt = "请根据以下文档回答问题：\n\n" + document + "\n\n问题：" + question

    data = {
        "model": "glm-4-flash",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if "error" in result:
        print("出错了：", result["error"]["message"])
        break

    reply = result["choices"][0]["message"]["content"]
    print("AI：" + reply)