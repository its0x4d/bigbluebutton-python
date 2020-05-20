import hashlib
import requests
import xmltodict
import collections
from typing import Optional
from xmltodict import OrderedDict

from .request import BBBRequests

class MainBBB:

    def __init__(self, service_url: str, secret: str):
        self.service_url = service_url
        self.secret = secret

        if not service_url.endswith('/'):
            raise ValueError('Invalid Api please append slash to the end of service_url')

        self.api = BBBRequests(self)

    def checksum(self, endpoint: str, params: dict = {}) -> str:
        url_params_partial = []
        for key, value in params.items():
            url_params_partial.append("{}={}".format(key, value))

        param_str = "&".join(url_params_partial)
        plaintext = endpoint + param_str + self.secret
        sha1 = hashlib.sha1()
        sha1.update(plaintext.encode('utf-8'))
        checksum = sha1.hexdigest()
        return checksum
    
    def send_request(self, endpoint: str, params: dict = {}) -> Optional[collections.OrderedDict]:
        data = params
        data.update({
            'checksum': self.checksum(endpoint, params=params)
        })
        req = requests.get(self.service_url + endpoint, params=data)
        print(req.url)
        if int(req.status_code / 100) != 2:
            raise Exception('Non 2xx HTTP status code response')

        response = xmltodict.parse(req.text)

        if str(response['response']['returncode']).lower() != 'success':
            raise Exception('Recieved a non-success response: ' + response['response']['message'])

        return response['response']