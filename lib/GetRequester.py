import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(URL)
        return response.content

    def load_json(self):
        content_list = []
        contents = json.loads(self.get_response_body())
        for content in contents:
            content_list.append(content)

        return content_list
