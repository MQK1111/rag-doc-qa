import os
import requests

# ========== 配置 ==========
api_key = os.environ.get("ZHIPU_API_KEY")
url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

# ========== 读取并切分文档 ==========
with open("notes.txt", "r", encoding="utf-8") as f:
    document = f.read()

chunks = document.split("\n")
chunks = [c.strip() for c in chunks if c.strip()]

print("文档已切分为", len(chunks), "个片段")
for i, c in enumerate(chunks):
    print(f"片段{i+1}: {c}")
print("-" * 30)

# ========== 检索函数 ==========
def retrieve(question, chunks, top_k=2):
    scored = []
    for chunk in chunks:
        score = 0
        for word in question:
            if word in chunk:
                score += 1
        scored.append((score, chunk))
    scored.sort(reverse=True)
    return [chunk for score, chunk in scored[:top_k]]

# ========== 主循环 ==========
while True:
    question = input("你：")
    if question == "退出":
        break

    relevant = retrieve(question, chunks)
    context = "\n".join(relevant)

    print("【检索到的片段】")
    print(context)
    print("-" * 30)

    prompt = "请根据以下资料回答问题：\n\n" + context + "\n\n问题：" + question

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
    print("=" * 30)