from dataclasses import dataclass
from typing import List


@dataclass
class Attendee:
    userID: str
    fullName: str
    role: str
    isPresenter: str
    isListeningOnly: str
    hasJoinedVoice: str
    hasVideo: str
    clientType: str


@dataclass
class GetMeetingInfoResponse:
    returncode: str = None
    meetingName: str = None
    meetingID: str = None
    internalMeetingID: str = None
    createTime: int = None
    createDate: str = None
    voiceBridge: int = None
    dialNumber: str = None
    attendeePW: str = None
    moderatorPW: str = None
    running: bool = None
    duration: int = None
    hasUserJoined: bool = None
    recording: bool = None
    hasBeenForciblyEnded: bool = None
    startTime: int = None
    endTime: int = None
    participantCount: int = None
    listenerCount: int = None
    voiceParticipantCount: int = None
    videoCount: int = None
    maxUsers: int = None
    moderatorCount: int = None
    attendees: List[Attendee] = None
    isBreakout: bool = None
    metadata: str = None
    breakoutRooms: dict = None
