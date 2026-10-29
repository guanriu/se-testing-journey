import pytest
import requests

# --- 第 1 部分：Fixture（夹具） ---
# 使用 @pytest.fixture 装饰器，定义公共准备（这里把基础 URL 提取出来）
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/todos"

# --- 第 2 部分：准备测试数据 ---
# 一个列表里套元组，每个元组就是一次测试的参数
test_data = [
    (1, 200, "delectus aut autem"),
    (2, 200, "quis ut nam facilis et officia qui"),
    (999, 404, None)  # 故意测试一个不存在的ID
]

# --- 第 3 部分：参数化测试函数 ---
# @pytest.mark.parametrize 会读取上面的 test_data
@pytest.mark.parametrize("todo_id, expected_status, expected_title", test_data)
def test_get_todo_with_params(todo_id, expected_status, expected_title, base_url):
    # 这里的 base_url 就是上面 fixture 返回的值
    url = f"{base_url}/{todo_id}"
    
    response = requests.get(url, timeout=10)
    
    # 断言状态码是否符合预期
    assert response.status_code == expected_status
    
    # 如果期望状态码是 200，再进一步校验 title
    if expected_status == 200:
        data = response.json()
        assert data.get("title") == expected_title