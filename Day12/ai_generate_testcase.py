import requests
import json
import os
from dotenv import load_dotenv


# 加载.env文件里的环境变量
load_dotenv()

# 从环境变量里偷偷读取key，不是写死

API_KEY = os.getenv("ZHIPU_API_KEY")

def generate_test_cases(requirement_text):
    # 智谱的请求地址
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    prompt = """
    你是一位拥有10年经验的资深软件测试开发工程师。请根据以下需求，输出测试用例。
    输出格式要求：请直接用 Markdown 表格输出，表头为：用例编号、测试场景、操作步骤、预期结果、优先级。不要输出任何多余的解释。
    """
    
    payload = {
        "model": "glm-4-flash",  # 智谱免费的神级模型
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"需求如下：{requirement_text}"}
        ],
        "temperature": 0.3
    }

    print("正在呼叫智谱 AI 生成测试用例...")
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        ai_content = data["choices"][0]["message"]["content"]
        return ai_content
    else:
        print(f"请求失败，状态码：{response.status_code}，错误信息：{response.text}")
        return None

if __name__ == "__main__":
    my_requirement = "用户登录功能。需求是：账号输入框只能输入 11 位手机号，密码框只能输入 6-16 位字母或数字。登录成功进入首页，失败提示密码错误。"
    
    result = generate_test_cases(my_requirement)
    
    if result:
        print("\n====== AI 生成的测试用例 ======\n")
        print(result)
        
        with open("ai_test_cases.md", "w", encoding="utf-8") as f:
            f.write(result)
        print("\n✅ 已成功保存到文件 ai_test_cases.md")