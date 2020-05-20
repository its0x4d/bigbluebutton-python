import json


class endMeetingResponse:

    def __init__(self, data):
        self.as_json = json.dumps(data)
        self.returncode = data['returncode']
        self.messageKey = data['messageKey']
        self.message = data['message']