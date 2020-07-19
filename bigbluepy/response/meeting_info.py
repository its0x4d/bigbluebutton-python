from dataclasses import dataclass

@dataclass
class getMeetingInfogResponse:
    returncode: str
    meetingName: str
    meetingID: str
    internalMeetingID: str
    createTime: int
    createDate: str
    voiceBridge: int
    dialNumber: str
    attendeePW: str
    moderatorPW: str
    running: bool
    duration: int
    hasUserJoined: bool
    recording: bool
    hasBeenForciblyEnded: bool
    startTime: int
    endTime: int
    participantCount: int
    listenerCount: int
    voiceParticipantCount: int
    videoCount: int
    maxUsers: int
    moderatorCount: int
    attendees: dict
    isBreakout: bool
    metadata: str
    breakoutRooms: dict = None