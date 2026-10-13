todos =["上网","抽烟","打游戏"]
print(todos)
todos.append("学习ai")
print(todos)
person = {"姓名": "马启凯", "年龄": 24, "城市": "重庆"}
print(person["姓名"])
for item in todos:
    if item == "学习ai":
        print(item + "：这个最重要")
    else:
        print(item + "：普通任务")
def greet(name):
    print("你好，" + name)

greet("马启凯")
greet("张三")
def check_score(score):
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")
        check_score(95)
check_score(75)
check_score(50)
with open("notes.txt", "w", encoding="utf-8") as f:
     f.write("今天学习了函数\n")
     f.write("明天学文件读写\n")

with open("notes.txt", "r", encoding="utf-8") as f:
     content = f.read()
     print(content)
try:
         result = 10 / 0
         print(result)
except Exception as e:
            print("出错了："+ str(e))