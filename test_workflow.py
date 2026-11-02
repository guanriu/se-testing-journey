import requests
def test_creat_and_get_post():
    bur_url = "https://jsonplaceholder.typicode.com"
    # ------接口1：创建帖子---------
    new_post = {
        "title":"软件工程学习记录",
        "body":"这是测开day5的作业",
        "userid":1
    }
    create_res = requests.post(bur_url + "/posts", json=new_post,timeout=5)
    assert create_res.status_code == 201
    # 关键提取，从返回的JSON的字典中获取服务器生成的帖子ID
    created_post_id =create_res.json().get("id")
    print(f"\n提取到的新帖子的ID是:{created_post_id}")

    # ------接口2：查询帖子---------
    get_res = requests.get(bur_url + f"/posts/{created_post_id}",timeout=5)
    assert get_res.status_code == 404

    # 验证查出来的内容，看是不是提交的内容
    get_data = get_res.json()
    # assert get_data.get('title') == new_post['title']
    print(f"\n查询成功，返回的帖子内容是:{get_data}")