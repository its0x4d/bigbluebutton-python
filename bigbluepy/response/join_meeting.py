from dataclasses import dataclass


@dataclass
class joinMeetingResponse:
    returncode: str
    meeting_id: str
    user_id: str
    auth_token: str
    session_token: str
    url: str
    guestStatus: str
    messageKey: str
    message: str