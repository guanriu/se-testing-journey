import requests

# 注意：pytest 规定，测试函数必须以 test_ 开头
def test_get_todo_positive():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url, timeout=5)
    data = response.json()
    
    # 依然是咱们的断言，但这次不需要 try...except 了，pytest 会自动帮你捕获
    assert response.status_code == 200, f"预期状态码200，实际{response.status_code}"
    assert data.get("userId") == 1, f"预期userId=1，实际{data.get('userId')}"

def test_get_todo_negative():
    # 这是一个故意写错的接口，用来测试异常
    url = "https://jsonplaceholder.typicode.com/todos/1_error"
    response = requests.get(url, timeout=5)
    
    # 我们断言它返回 404（找不到页面）
    assert response.status_code == 404, f"预期状态码404，实际{response.status_code}"