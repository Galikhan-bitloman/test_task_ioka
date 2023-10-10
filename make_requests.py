from typing import Optional

from requests import Response
import requests

from common.consts import HTTP_METHOD, HEADERS


class Requesting:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_requests(self, method: str,path: str, params: dict = None) -> dict:
        try:
            headers = {"API-KEY": HEADERS.API_KEY.value, "Content-Type": "application/json"}
            if method == HTTP_METHOD.GET.value:
                req = requests.get(url=self.base_url + path, headers=headers)
                return req.json()
            if method == HTTP_METHOD.POST.value:
                req = requests.post(url=self.base_url + path, json=params, headers=headers)
                return req.json()
        except (ConnectionError, TimeoutError) as e:
            return e
