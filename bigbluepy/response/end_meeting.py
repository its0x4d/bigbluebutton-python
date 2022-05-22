from dataclasses import dataclass


@dataclass
class EndMeetingResponse:
    returncode: str
    messageKey: str
    message: str
