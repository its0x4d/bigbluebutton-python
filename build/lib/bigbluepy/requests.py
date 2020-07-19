import json
import random
from bigbluepy.response.create_meeting_response import createMeetingResponse 
from bigbluepy.response.end_meeting_response import endMeetingResponse 
from uuid import uuid4

class BBBRequests:

    def __init__(self, app):
        self.app = app

    def createVoiceBride(self):
        """
        Voice conference number for the FreeSWITCH voice conference associated with this meeting.
        This must be a 5-digit number in the range 10000 to 99999.
        If you add a phone number to your BigBlueButton server. 
        This parameter sets the personal identification number (PIN) that FreeSWITCH will prompt for a phone-only user to enter.
        If you want to change this range, 
        edit FreeSWITCH dialplan and defaultNumDigitsForTelVoice of bigbluebutton.properties.
        """
        return "".join(random.choices("1234567890", k=5))
    
    def createMeeting(self, name: str = None, meetingID: str = None, attendeePW: str = None, moderatorPW: str = None, welcome: str = None, dialNumber: str = None, voiceBridge: int = None, maxParticipants: int = None, logoutURL: str = None, record: bool = None, duration: int = None, isBreakout: bool = None, parentMeetingID: str = None, sequence: int = None, freeJoin: bool = None, meta: None = str, moderatorOnlyMessage: str = None, autoStartRecording: bool = None, allowStartStopRecording: bool = True, webcamsOnlyForModerator: bool = None, logo: str = None, bannerText: str = None, bannerColor: str = None, _copyright: str = None, muteOnStart: bool = None, allowModsToUnmuteUsers: bool = False, lockSettingsDisableCam: bool = False, lockSettingsDisableMic: bool = False, lockSettingsDisablePrivateChat: bool = False, lockSettingsDisablePublicChat: bool = False, lockSettingsDisableNote: bool = False, lockSettingsLockedLayout: bool = False, lockSettingsLockOnJoin: bool = True, lockSettingsLockOnJoinConfigurable: False, guestPolicy: str = None):
        """
        Create Meeting
        docuement = "https://docs.bigbluebutton.org/dev/api.html#create"
        """
        if not meetingID:
            # A good choice for the meeting ID is to generate a GUID value as this all but guarantees that different meetings will not have the same meetingID.
            meetingID = uuid4()
        data = {
            'meetingID': meetingID
        }
        if name:
            if not isinstance(name, int):
                raise ValueError(f'name must be instance of int, not {type(name)}')
            data['name'] = name

        if attendeePW:
            if not isinstance(attendeePW, int):
                raise ValueError(f'attendeePW must be instance of int, not {type(attendeePW)}')
            data['attendeePW'] = attendeePW

        if moderatorPW:
            if not isinstance(moderatorPW, int):
                raise ValueError(f'moderatorPW must be instance of int, not {type(moderatorPW)}')
            data['moderatorPW'] = moderatorPW

        if welcome:
            if not isinstance(welcome, int):
                raise ValueError(f'welcome must be instance of int, not {type(welcome)}')
            data['welcome'] = welcome

        if dialNumber:
            if not isinstance(dialNumber, int):
                raise ValueError(f'dialNumber must be instance of int, not {type(dialNumber)}')
            data['dialNumber'] = dialNumber

        if voiceBridge:
            if not isinstance(voiceBridge, int):
                raise ValueError(f'voiceBridge must be instance of int, not {type(voiceBridge)}')
            data['voiceBridge'] = voiceBridge
            
        if maxParticipants:
            if not isinstance(maxParticipants, int):
                raise ValueError(f'maxParticipants must be instance of int, not {type(maxParticipants)}')
            data['maxParticipants'] = maxParticipants
        
        if logoutURL:
            if not isinstance(logoutURL, str):
                raise ValueError(f'logoutURL must be instance of str, not {type(logoutURL)}')
            data['logoutURL'] = logoutURL
        
        if record:
            if not isinstance(duration, bool):
                raise ValueError(f'duration must be instance of bool, not {type(duration)}')
            data['record'] = record
        
        if duration:
            if not isinstance(duration, int):
                raise ValueError(f'duration must be instance of int, not {type(duration)}')
            data['duration'] = duration

        if isBreakout:
            if not isinstance(isBreakout, bool):
                raise ValueError(f'isBreakout must be instance of bool, not {type(isBreakout)}')
            data['isBreakout'] = isBreakout
            if not parentMeetingID:
                raise ValueError(f'If you want to create BreakOut room you must call parentMeetingID,sequence parameters')
            else:
                if not isinstance(parentMeetingID, str):
                    raise ValueError(f'parentMeetingID must be instance of str, not {type(parentMeetingID)}')
                data['parentMeetingID'] = parentMeetingID
            if not sequence:
                raise ValueError(f'If you want to create BreakOut room you must call parentMeetingID,sequence parameters')
            else:
                if not isinstance(sequence, int):
                    raise ValueError(f'sequence must be instance of int, not {type(sequence)}')
                data['sequence'] = sequence
            if freeJoin:
                if not isinstance(freeJoin, bool):
                    raise ValueError(f'freeJoin must be instance of bool, not {type(freeJoin)}')
                data['freeJoin'] = freeJoin
            
        if meta:
            if not isinstance(meta, str):
                raise ValueError(f'meta must be instance of str, not {type(meta)}')
            data['meta'] = meta
        
        if moderatorOnlyMessage:
            if not isinstance(moderatorOnlyMessage, str):
                raise ValueError(f'moderatorOnlyMessage must be instance of str, not {type(moderatorOnlyMessage)}')
            data['moderatorOnlyMessage'] = moderatorOnlyMessage
        
        if autoStartRecording:
            if not isinstance(autoStartRecording, bool):
                raise ValueError(f'autoStartRecording must be instance of bool, not {type(autoStartRecording)}')
            data['autoStartRecording'] = autoStartRecording
        
        if allowStartStopRecording:
            if not isinstance(allowStartStopRecording, bool):
                raise ValueError(f'allowStartStopRecording must be instance of bool, not {type(allowStartStopRecording)}')
            data['allowStartStopRecording'] = allowStartStopRecording
        
        if webcamsOnlyForModerator:
            if not isinstance(webcamsOnlyForModerator, bool):
                raise ValueError(f'webcamsOnlyForModerator must be instance of bool, not {type(webcamsOnlyForModerator)}')
            data['webcamsOnlyForModerator'] = webcamsOnlyForModerator
        
        if logo:
            if not isinstance(logo, str):
                raise ValueError(f'logo must be instance of str, not {type(logo)}')
            data['logo'] = logo
        
        if bannerText:
            if not isinstance(bannerText, str):
                raise ValueError(f'bannerText must be instance of str, not {type(bannerText)}')
            data['bannerText'] = bannerText
        
        if bannerText:
            if not isinstance(bannerText, str):
                raise ValueError(f'bannerText must be instance of str, not {type(bannerText)}')
            data['bannerText'] = bannerText
        
        if bannerColor:
            if not isinstance(bannerColor, str):
                raise ValueError(f'bannerColor must be instance of str, not {type(bannerColor)}')
            if '#' not in bannerColor:
                raise ValueError(f'You must use hex colors')
            data['bannerColor'] = bannerColor
        
        if _copyright:
            if not isinstance(_copyright, str):
                raise ValueError(f'copyright must be instance of str, not {type(_copyright)}')
            data['copyright'] = _copyright
        
        if muteOnStart:
            if not isinstance(muteOnStart, bool):
                raise ValueError(f'muteOnStart must be instance of bool, not {type(muteOnStart)}')
            data['muteOnStart'] = muteOnStart
        
        if allowModsToUnmuteUsers:
            if not isinstance(allowModsToUnmuteUsers, bool):
                raise ValueError(f'allowModsToUnmuteUsers must be instance of bool, not {type(allowModsToUnmuteUsers)}')
            data['allowModsToUnmuteUsers'] = allowModsToUnmuteUsers
        
        if lockSettingsDisableCam:
            if not isinstance(lockSettingsDisableCam, bool):
                raise ValueError(f'lockSettingsDisableCam must be instance of bool, not {type(lockSettingsDisableCam)}')
            data['lockSettingsDisableCam'] = lockSettingsDisableCam
        
        if lockSettingsDisableMic:
            if not isinstance(lockSettingsDisableMic, bool):
                raise ValueError(f'lockSettingsDisableMic must be instance of bool, not {type(lockSettingsDisableMic)}')
            data['lockSettingsDisableMic'] = lockSettingsDisableMic
        
        if lockSettingsDisablePrivateChat:
            if not isinstance(lockSettingsDisablePrivateChat, bool):
                raise ValueError(f'lockSettingsDisablePrivateChat must be instance of bool, not {type(lockSettingsDisablePrivateChat)}')
            data['lockSettingsDisablePrivateChat'] = lockSettingsDisablePrivateChat
        
        if lockSettingsDisablePublicChat:
            if not isinstance(lockSettingsDisablePublicChat, bool):
                raise ValueError(f'lockSettingsDisablePublicChat must be instance of bool, not {type(lockSettingsDisablePublicChat)}')
            data['lockSettingsDisablePublicChat'] = lockSettingsDisablePublicChat
        
        if lockSettingsDisableNote:
            if not isinstance(lockSettingsDisableNote, bool):
                raise ValueError(f'lockSettingsDisableNote must be instance of bool, not {type(lockSettingsDisableNote)}')
            data['lockSettingsDisableNote'] = lockSettingsDisableNote
        
        if lockSettingsLockedLayout:
            if not isinstance(lockSettingsLockedLayout, bool):
                raise ValueError(f'lockSettingsLockedLayout must be instance of bool, not {type(lockSettingsLockedLayout)}')
            data['lockSettingsLockedLayout'] = lockSettingsLockedLayout
        
        if lockSettingsLockOnJoin:
            if not isinstance(lockSettingsLockOnJoin, bool):
                raise ValueError(f'lockSettingsLockOnJoin must be instance of bool, not {type(lockSettingsLockOnJoin)}')
            data['lockSettingsLockOnJoin'] = lockSettingsLockOnJoin
        
        if lockSettingsLockOnJoinConfigurable:
            if not isinstance(lockSettingsLockOnJoinConfigurable, bool):
                raise ValueError(f'lockSettingsLockOnJoinConfigurable must be instance of bool, not {type(lockSettingsLockOnJoinConfigurable)}')
            data['lockSettingsLockOnJoinConfigurable'] = lockSettingsLockOnJoinConfigurable
        
        if guestPolicy:
            types = ['ALWAYS_ACCEPT', 'ALWAYS_DENY', 'ASK_MODERATOR']
            if not isinstance(guestPolicy, str):
                raise ValueError(f'guestPolicy must be instance of bool, not {type(guestPolicy)}')
            if guestPolicy not in types:
                raise ValueError(f'Invalid guestPolicy type. Valid types are {str(types)}')
            data['guestPolicy'] = guestPolicy
        
        query = self.app.send_request('create', params=data)
        return createMeetingResponse(query)

        
        
        

        