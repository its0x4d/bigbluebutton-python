import base64
import hashlib
from urllib import parse


def checksum(endpoint: str, secret: str, params: dict = None) -> str:
    url_params_partial = []
    params = params if params is not None else {}
    for key, value in params.items():
        url_params_partial.append("{}={}".format(key, value))

    param_str = "&".join(url_params_partial)
    plaintext = endpoint + param_str + secret
    sha1 = hashlib.sha1()
    sha1.update(plaintext.encode('utf-8'))
    _checksum = sha1.hexdigest()
    return _checksum


def http_build_query(query):
    return parse.urlencode(
        query
    )


def build_user_data(data):
    user_data = {}
    for key, value in data.items():
        if isinstance(value, bool):
            user_data.update({f'userdata-{key}': 'true' if value else 'false'})
        else:
            user_data.update({f'userdata-{key}': value})
    return user_data


def build_meta_data(data):
    meta_data = {}
    for key, value in data.items():
        if isinstance(value, bool):
            meta_data.update({f'meta-{key}': 'true' if value else 'false'})
        else:
            meta_data.update({f'meta-{key}': value})
    return meta_data


def file_to_base64(file_path):
    with open(file_path, 'rb') as file:
        # convert binary data to base64 encoded string
        return base64.b64encode(file.read()).decode()


def generate_file_upload_xml(file_path, name, url: str = None, removable: bool = False, downloadable: bool = False):
    return f'''
        <modules>
            <module name="presentation">
                <document current="true" downloadable="{'true' if downloadable else 'false'}" url="null" filename="{name}"/>
                    <document removable="{'true' if removable else 'false'}" name="{name}">
                        {file_to_base64(file_path)}
                    </document>
            </module>
        </modules>
    '''
