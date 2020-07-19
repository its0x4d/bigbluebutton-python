from dataclasses import dataclass


@dataclass
class endMeetingResponse:
    returncode: str
    messageKey: str
    message: str