import pytest as pt
import requests as ret

class ForumClient:
    def __init__(self,base_url):
        self.base_url = base_url
        self.session = ret.Session()
    def post_article(self,title,body):
        # 
        url = f"{self.base_url}/posts"
        payload = {
            "title":title,
            "body":body,
            "userId":1
        }
        res = self.session.post(url,json=payload)
        return res
def test_post_and_get_article():
    # 根据ForumClient这个图纸，造一个client对象
    client = ForumClient("https://jsonplaceholder.typicode.com")
    # 调用发帖方法
    res_post = client.post_article(title="测试帖子",body="自动化测试内容")
    #断言创建成功，创建成功然后返回201
    assert res_post.status_code == 201
    post_id = res_post.json()["id"]
    print(f"请求查询地址：{client.base_url}/posts/{post_id}")
    res_get = client.session.get(f"{client.base_url}/posts/{post_id}")
    assert res_get.status_code == 200
    data = res_get.json()
    assert data["id"] == post_id