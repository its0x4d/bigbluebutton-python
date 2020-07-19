from dataclasses import dataclass


@dataclass
class createMeetingResponse:
    returncode: str = None
    meetingID: str = None
    internalMeetingID: str = None 
    parentMeetingID: str = None 
    attendeePW: str = None 
    moderatorPW: str = None 
    createTime: str = None 
    createDate: str = None 
    hasUserJoined: bool = None
    duration: int = None
    hasBeenForciblyEnded: bool = None 
    messageKey: str = None
    message: str = None 
    voiceBridge: int = None
    dialNumber: str = None