from typing import Any

import requests
import xmltodict

from bigbluepy import utils
from bigbluepy.requests import BBBRequests


class MainBBB:

    def __init__(self, service_url: str, secret: str):
        """
        :param service_url: 'https://bbb.example.com/bigbluebutton/api/'
        :param secret: You can get your secret key by using ```bbb-conf --secret```
        """
        self.service_url = service_url
        self.secret = secret

        if not service_url.endswith('/'):
            raise ValueError('Invalid SERVICE_URL. Please append slash to the end of SERVICE_URL')

        self.session = requests.Session()
        self.last_response = None

        self.api = BBBRequests(self)

    def send_request(self, endpoint: str, params: dict = None, just_create: bool = False, data: Any = None) -> Any:
        request_data = {
            'checksum': utils.checksum(endpoint=endpoint, secret=self.secret, params=params)
        }
        request_data.update(params or {})
        request_data = utils.http_build_query(request_data)
        self.session.headers.update({
            'content-type': 'application/xml'
        })
        try:
            if just_create:
                return self.service_url + endpoint + '/?' + request_data
            _request = self.session.post(self.service_url + endpoint, params=request_data, data=data, verify=True)
            self.last_response = _request
        except:
            raise Exception("Connection Error")

        if _request.status_code == 413:
            raise Exception("File too large")

        if int(_request.status_code / 100) != 2:
            raise Exception('Non 2xx HTTP status code response')

        response = xmltodict.parse(_request.text)

        return response['response']
