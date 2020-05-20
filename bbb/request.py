import json
import random
from .response.create_meeting_response import createMeetingResponse 
from .response.end_meeting_response import endMeetingResponse 

class BBBRequests:

    def __init__(self, app):
        self.app = app

    def getVoiceBride(self):
        return random.randint(00000, 99999)

    def createMeeting(self, attendePW: str, moderatorPW: str, name: str, meetingID: str, welcome: str, duration: int = 0, record: bool = False, voiceBridge: int = None, allowStartStopRecording: bool = True, autoStartRecording: bool = False):
        data = {
            'attendeePW': attendePW,
            'moderatorPW': moderatorPW,
            'name': name,
            'meetingID': meetingID,
            'record': record,
            'welcome': welcome,
            'voiceBridge': self.getVoiceBride(),
            'autoStartRecording': autoStartRecording,
            'allowStartStopRecording': allowStartStopRecording,
            'duration': duration,
            'maxParticipants': 20
        }
        query = self.app.send_request('create', params=data)
        return createMeetingResponse(query)

    def endMeeting(self, meetingID: str, moderatorPW: str) -> endMeetingResponse:
        data = {
            'meetingID': meetingID,
            'password': moderatorPW
        }
        query = self.app.send_request('end', data)
        return endMeetingResponse(query)
    
    def isMeetingRunning(self, meetingID: str):
        pass