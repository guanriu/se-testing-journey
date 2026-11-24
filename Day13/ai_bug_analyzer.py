import requests as rq
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ZHIPU_API_KEY")

def analyze_bug_log(error_log):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    # resp = rq.get(url)
    headers = {
        "Content":"application/json",
        "Authorization":f"Bearer {API_KEY}"
    }
 # 今天的 Prompt 变了：让它当 Bug 分析师，并规定输出格式
    prompt = """
    你是一个拥有10年经验的资深测试开发工程师
    请分析我提供的自动化测试报错日志，输出一份专业的Markdown格式Bug报告
    报告必须包含以下结构
    ### bug标题
    ### 严重程度（P0/P1/P2）
    ### 根因分析（为什么报错）
    ### 修复建议（开发应该怎么改）
    """
    payload = {
        "model":"glm-4-flash",
        "messages":[
            {"role":"system","content":prompt},
            {"role":"user","content":f"报错日志如下：\n{error_log}"}
        ],
        "temperature":0.2 #温度调低，让AI更严谨
    }

      # 🚨 加上这行，把你即将发送给服务器的 JSON 打印出来看看！
    print("==== 准备发送给服务器的数据 ====")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    print("==============================")
    print("正在呼叫AI分析bug")
    response = rq.post(url,headers=headers,json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"🚨 详细报错内容: {response.text}")
        return f"AI分析失败，状态码:{response.status_code}"
if __name__ == "__main__":
    # 模拟你从终端里复制下来的报错日志（这里我们把上面的错报截取一段）
    crash_log = """
    E       assert 404 == 200
    E        +  where 404 = <Response [404]>.status_code
    test_crash.py:10: AssertionError
    """
    
    print(f"接收到的报错日志：\n{crash_log}")
    print("-" * 30)
    
    # 让 AI 分析
    bug_report = analyze_bug_log(crash_log)
    
    # 保存结果
    print(bug_report)
    with open("bug_report.md", "w", encoding="utf-8") as f:
        f.write(bug_report)
    print("\n✅ 已成功自动生成 Bug 报告：bug_report.md")


# import requests
# import json
# import os
# from dotenv import load_dotenv

# load_dotenv()
# API_KEY = os.getenv("ZHIPU_API_KEY")

# def analyze_bug_log(error_log):
#     url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {API_KEY}"
#     }
    
#     # 今天的 Prompt 变了：让它当 Bug 分析师，并规定输出格式
#     prompt = """
#     你是一个拥有10年经验的资深测试开发工程师。
#     请分析我提供的自动化测试报错日志，输出一份专业的 Markdown 格式 Bug 报告。
    
#     报告必须包含以下结构：
#     ### 🐞 Bug 标题
#     ### 🚨 严重程度 (P0/P1/P2)
#     ### 🔍 根因分析 (为什么会报错)
#     ### 💡 修复建议 (开发应该怎么改)
#     """
    
#     payload = {
#         "model": "glm-4-flash",
#         "messages": [
#             {"role": "system", "content": prompt},
#             {"role": "user", "content": f"报错日志如下：\n{error_log}"}
#         ],
#         "temperature": 0.2 # 温度调低，让 AI 更加严谨
#     }

#     print("正在呼叫 AI 分析 Bug...")
#     response = requests.post(url, headers=headers, json=payload)
    
#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"]
#     else:
#         return f"AI 分析失败，状态码：{response.status_code}"

# if __name__ == "__main__":
#     # 模拟你从终端里复制下来的报错日志（这里我们把上面的错报截取一段）
#     crash_log = """
#     E       assert 404 == 200
#     E        +  where 404 = <Response [404]>.status_code
#     test_crash.py:10: AssertionError
#     """
    
#     print(f"接收到的报错日志：\n{crash_log}")
#     print("-" * 30)
    
#     # 让 AI 分析
#     bug_report = analyze_bug_log(crash_log)
    
#     # 保存结果
#     print(bug_report)
#     with open("bug_report.md", "w", encoding="utf-8") as f:
#         f.write(bug_report)
#     print("\n✅ 已成功自动生成 Bug 报告：bug_report.md")