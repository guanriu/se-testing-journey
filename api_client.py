import requests
class ApiClient:
    def __init__(self,base_url):
        self.base_url = base_url
        self.timeout = 5
        self.session = requests.Session()


    def get(self,endpoint,**kwargs):
        url = f"{self.base_url}{endpoint}"
        print(f"[请求]GET{url}")
        return self.session.get(url,timeout=self.timeout,**kwargs)
    
    def post(self,endpoint,json_data):
        url = f"{self.base_url}{endpoint}"
        print(f"[请求]POST{url}")
        return self.session.post(url,json=json_data,timeout=self.timeout)