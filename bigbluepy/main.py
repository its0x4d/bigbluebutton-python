import json
import hashlib
import requests
import xmltodict
import collections
from typing import Optional
from xmltodict import OrderedDict
import urllib.parse

from bigbluepy.requests import BBBRequests

class MainBBB:

    def __init__(self, service_url: str, secret: str):
        """
        :service_url = 'https://bbb.example.com/bigbluebutton/api/'
        :secret = You can get your secret key by using ```bbb-conf --secret```
        """
        self.service_url = service_url
        self.secret = secret

        if not service_url.endswith('/'):
            raise ValueError('Invalid SERVICE_URL. Please append slash to the end of SERVICE_URL')
        
        self.session = requests.Session()
        self.last_response = None

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
    
    def http_build_query(self, query):
        return urllib.parse.urlencode(
            query
        )

    def build_user_data(self, data):
        user_data = {}
        for key, value in data.items():
            if isinstance(value, bool):
                user_data.update({f'userdata-{key}': 'true' if value else 'false'})
            else:
                user_data.update({f'userdata-{key}': value})
        return user_data
    
    def build_meta_data(self, data):
        meta_data = {}
        for key, value in data.items():
            if isinstance(value, bool):
                meta_data.update({f'meta-{key}': 'true' if value else 'false'})
            else:
                meta_data.update({f'meta-{key}': value})
        return meta_data

    def send_request(self, endpoint: str, params: dict = {}, just_create: bool = False) -> Optional[collections.OrderedDict]:
        data = params
        data = data.update({
            'checksum': self.checksum(endpoint, params=params)
        })
        data = self.http_build_query(params)
        self.session.headers.update({
            'Content-type': 'application/xml',
        })
        try:
            if just_create:
                return self.service_url + endpoint + '/?' + data
            _request = self.session.post(self.service_url + endpoint, params=data, verify=True)
            self.last_response = _request
        except:
            raise Exception("Connection Error")
        
        if int(_request.status_code / 100) != 2:
            raise Exception('Non 2xx HTTP status code response')

        response = xmltodict.parse(_request.text)

        return response['response']