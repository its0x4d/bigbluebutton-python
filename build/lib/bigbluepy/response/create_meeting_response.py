from dataclasses import dataclass


@dataclass
class createMeetingResponse:
    returncode: str
    meetingID: str
    internalMeetingID: str 
    parentMeetingID: str 
    attendeePW: str 
    moderatorPW: str 
    createTime: str 
    createDate: str 
    hasUserJoined: bool
    duration: int 
    hasBeenForciblyEnded: bool 
    messageKey: str 
    message: str 
    