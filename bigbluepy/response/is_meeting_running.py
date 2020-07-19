from dataclasses import dataclass


@dataclass
class isMeetingRunningResponse:
    returncode: str = None
    messageKey: str = None
    message: str = None
    running: bool = None
