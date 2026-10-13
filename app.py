import os
import requests
import chromadb
import streamlit as st

# ========== 配置 ==========
api_key = os.environ.get("ZHIPU_API_KEY")
url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

# ========== 页面标题 ==========
st.title("本地文档问答助手")
st.write("基于向量检索的 RAG 系统，可以针对本地文档提问。")

# ========== 初始化向量库 ==========
def init_collection():
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="my_docs")

    # 清空旧数据
    existing = collection.get()
    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    with open("notes.txt", "r", encoding="utf-8") as f:
        document = f.read()
    chunks = document.split("\n")
    chunks = [c.strip() for c in chunks if c.strip()]
    print("读到的片段：", chunks)
    collection.add(
        documents=chunks,
        ids=[str(i) for i in range(len(chunks))]
    )
    return collection

collection = init_collection()

# ========== 检索函数 ==========
def retrieve(question, top_k=5):
    results = collection.query(
        query_texts=[question],
        n_results=top_k
    )
    return results["documents"][0]

# ========== 界面 ==========
question = st.text_input("请输入你的问题：")

if st.button("提问"):
    if question:
        relevant = retrieve(question)
        context = "\n".join(relevant)

        prompt = "请严格根据以下资料回答问题。如果资料中没有相关信息，请直接回答“资料中没有提到”，不要编造。\n\n资料：\n" + context + "\n\n问题：" + question

        data = {
            "model": "glm-4-flash",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "error" in result:
            st.error("出错了：" + result["error"]["message"])
        else:
            reply = result["choices"][0]["message"]["content"]
            st.write("**回答：**")
            st.write(reply)
            st.write("**检索到的片段：**")
            st.write(context)