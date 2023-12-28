import json
import requests
from data import ConstantData


class ApiClient:

    def __init__(self):
        self.base_url = ConstantData.BASE_URL
        self.headers = ConstantData.DEFAULT_HEADERS

    def post(self, path, payload):
        response = requests.post(url=self.base_url + path,
                                 headers=self.headers,
                                 data=json.dumps(payload))
        return response

    def get(self, path):
        response = requests.get(url=self.base_url + path,
                                headers=self.headers)
        return response
