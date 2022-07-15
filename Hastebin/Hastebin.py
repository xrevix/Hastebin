# Https://github.com/xrevix


import requests, json


class Hastebin:
    def __init__(self, proxy: str= None):
        self.session = requests.Session()
        self.session.proxies = {"http": proxy, "https": proxy} if proxy else None
        self.base_url = "https://www.toptal.com/developers/hastebin/documents"
        self.raw_base_url = "https://www.toptal.com/developers/hastebin/raw/"

    def create(self, text: str):
        if text == "":
            return "Enter Content Please" 
        response = self.session.post('https://hastebin.com/documents', data=text)

        key = json.loads(response.content)
        return "https://www.toptal.com/developers/hastebin/" + key['key']

    def lookup(self, key: str):
        response = self.session.get(self.raw_base_url + key).text
        if key == "":
            return "Enter Content Please" 
            
        if response == """{"message":"Document not found."}""":
            return "Key Is Not Right"

        return response
