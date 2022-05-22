from dataclasses import dataclass
from typing import List

from bigbluepy.response.meeting_info import GetMeetingInfoResponse


@dataclass
class GetMeetingsResponse:
    returncode: str
    meetings: List[GetMeetingInfoResponse] = None
    messageKey: str = None
    message: str = None
