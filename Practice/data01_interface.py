import pytest
import requests
@pytest.fixture
def api_access():
    session = requests.Session()
    session.headers.update({
        "Content-Type":"application/json"
    })
    return session
def test_get_user_list(api_access):
    url = "https://jsonplaceholder.typicode.com/users"
    resp = api_access.get(url)
    assert resp.status_code == 200 #"接口返回状态码不是200"
    user_list = resp.json()
    assert len(user_list) > 0 #"用户列表为空！"