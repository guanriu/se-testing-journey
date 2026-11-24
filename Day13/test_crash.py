import requests as rq
import pytest
def test_get_user_crash():
    # 我们这里请求一个不存在的ID试试
    url = "https://jsonplaceholder.typicode.com/users/999"
    res = rq.get(url)
    assert res.status_code == 200,f"预期的状态码是200，这里返回的状态码是{res.status_code}"
    