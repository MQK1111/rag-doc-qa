# 基于向量检索的本地文档问答助手

## 项目简介

这是一个基于 RAG（检索增强生成）的本地文档问答系统。用户可以针对本地文档提问，系统会从文档中检索最相关的片段，结合大模型生成回答。

项目实现了两种检索方式：
- 关键词匹配检索（rag_simple.py）
- 向量检索（rag_vector.py，基于 chromadb）

通过对比，向量检索在语义匹配上明显优于关键词匹配，能有效减少模型编造答案的情况。

## 技术栈

- Python 3.14
- requests：发送 HTTP 请求调用大模型 API
- chromadb：本地向量数据库
- 智谱 GLM-4-Flash：大模型 API

## 如何运行

1. 安装依赖：
   pip install requests chromadb

2. 设置环境变量：
   setx ZHIPU_API_KEY "你的key"

3. 准备文档：
   将待查询的文档保存为 notes.txt，放在项目根目录

4. 运行向量检索版：
   python rag_vector.py

## 项目结构

- rag_simple.py：关键词匹配版 RAG
- rag_vector.py：向量检索版 RAG
- notes.txt：示例文档
- README.md：项目说明

## 效果对比

以问题“我大后天要学什么”为例：

- 关键词匹配版：检索到不相关片段，模型编造答案
- 向量检索版：未检索到相关内容，模型如实回答“没有明确提及”