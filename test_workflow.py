import requests
import pytest
import json
from api_client import ApiClient

def get_test_data():
    with open("data/test_data.json","r","utf-8") as f:
        return json.load(f)
@pytest.fixture
def client():
    return ApiClient(base_url="https://jsonplaceholder.typicode.com")

@pytest.mark.parametrize("post_data",get_test_data())

def test_workflow_with_class(client,post_data):
    # new_post = {"title":"Day6作业","bode":"测试","userId":1}
    print(f'\n正在测试发布帖子，标题为：{post_data.get("title")}')
    create_res = client.post("/posts", json_data=post_data )
    assert create_res.status_code == 201
    created_post_id =create_res.json().get("id")
    get_res = client.get(f"/posts/{created_post_id}")
    assert get_res.status_code ==404