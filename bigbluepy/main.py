import hashlib
import requests
import xmltodict
import collections
from typing import Optional
from xmltodict import OrderedDict

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

        self.api = BBBRequests(self)

    def checksum(self, endpoint: str, params: dict = {}) -> str:
        url_params_partial = []
        for key, value in params.items():
            url_params_partial.append("{}={}".format(key, value))

        param_str = "&".join(url_params_partial)
        plaintext = endpoint + param_str + self.secret
        sha1 = hashlib.sha256()
        sha1.update(plaintext.encode('utf-8'))
        checksum = sha1.hexdigest()
        return checksum
    
    def send_request(self, endpoint: str, params: dict = {}) -> Optional[collections.OrderedDict]:
        data = params
        data.update({
            'checksum': self.checksum(endpoint, params=params)
        })

        try:
            req = requests.get(self.service_url + endpoint, params=data)
        except:
            raise Exception("Connection Error")

        if int(req.status_code / 100) != 2:
            raise Exception('Non 2xx HTTP status code response')

        response = xmltodict.parse(req.text)

        return response['response']