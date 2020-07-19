from dataclasses import dataclass


@dataclass
class getMeetingsResponse:
    returncode: str
    meetings: str = None
    messageKey: str = None
    message: str = None