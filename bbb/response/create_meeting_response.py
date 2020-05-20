import json


class createMeetingResponse:

    def __init__(self, data):
        self.as_json = json.dumps(data)
        self.returncode = data['returncode']
        self.meetingID = data['meetingID']
        self.internalMeetingID = data['internalMeetingID']
        self.parentMeetingID = data['parentMeetingID']
        self.attendeePW = data['attendeePW']
        self.moderatorPW = data['moderatorPW']
        self.createTime = data['createTime']
        self.createDate = data['createDate']
        self.hasUserJoined = data['hasUserJoined']
        self.duration = data['duration']
        self.hasBeenForciblyEnded = data['hasBeenForciblyEnded']
        self.messageKey = data['messageKey']
        self.message = data['message']