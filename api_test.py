import requests

# 这是一个专门用来给新手练习接口测试的公开网站
url = "https://jsonplaceholder.typicode.com/todos/1"

print(f"正在请求接口: {url} ...")

try:
    # 1. 发送 GET 请求
    response = requests.get(url, timeout=5)
    
    # 2. 看看服务器返回的状态码
    #f允许你在字符串里直接嵌入变量
    print(f"HTTP 状态码: {response.status_code}")   
    
    # 3. 提取 JSON 数据
    data = response.json()
    print("返回的数据内容:", data)
    
    # 4. 提取具体字段
    print(f"提取的 title 是: {data.get('title')}")

    # 5. 断言：自动化测试的灵魂
    assert response.status_code == 200, f"预期状态码是200，实际是{response.status_code}"
    assert data.get("userId") == 1, f"预期 userId 是1，实际是{data.get('userId')}"
    
    print("🎉 接口测试通过！所有断言全部满足！")

except requests.exceptions.RequestException as e:
    print(f"请求出错了，网络可能有问题: {e}")