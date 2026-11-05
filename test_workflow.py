import requests
import pytest
from api_client import ApiClient
@pytest.fixture
def client():
    return ApiClient(base_url="https://jsonplaceholder.typicode.com")
def test_workflow_with_class(client):
    new_post = {"title":"Day6作业","bode":"测试","userId":1}
    create_res = client.post("/posts", json_data=new_post )
    assert create_res.status_code == 201
    # 关键提取，从返回的JSON的字典中获取服务器生成的帖子ID
    created_post_id =create_res.json().get("id")
    get_res = client.get(f"/posts/{created_post_id}")
    assert get_res.status_code ==404

    # ------接口2：查询帖子---------
    # get_res = requests.get(bur_url + f"/posts/{created_post_id}",timeout=5)
    # assert get_res.status_code == 404

    # 验证查出来的内容，看是不是提交的内容
    # get_data = get_res.json()
    # assert get_data.get('title') == new_post['title']
    # print(f"\n查询成功，返回的帖子内容是:{get_data}")