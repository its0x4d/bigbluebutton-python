import os
import random
from uuid import uuid4

from bigbluepy import utils
from bigbluepy.response.create_meeting import CreateMeetingResponse
from bigbluepy.response.end_meeting import EndMeetingResponse
from bigbluepy.response.join_meeting import JoinMeetingResponse
from bigbluepy.response.meeting_info import GetMeetingInfoResponse, Attendee
from bigbluepy.response.meetings import GetMeetingsResponse


class BBBRequests:

    def __init__(self, app):
        self.app = app

    @staticmethod
    def create_voice_bride():
        """
        Voice conference number for the FreeSWITCH voice conference associated with this meeting.
        This must be a 5-digit number in the range 10000 to 99999.
        If you add a phone number to your BigBlueButton server. 
        This parameter sets the personal identification number (PIN) that
        FreeSWITCH will prompt for a phone-only user to enter.
        If you want to change this range, 
        edit FreeSWITCH dialplan and defaultNumDigitsForTelVoice of bigbluebutton.properties.
        """
        return int("".join(random.choices("1234567890", k=5)))

    @staticmethod
    def create_meeting_id():
        return str(uuid4())

    def create_meeting(self, name: str, meeting_id: str = None, attendee_pw: str = None,
                       moderator_pw: str = None,
                       welcome: str = None, dial_number: str = None, voice_bridge: int = None,
                       max_participants: int = None, logout_url: str = None, record: bool = None,
                       duration: int = None, is_breakout: bool = None, parent_meeting_Id: str = None,
                       sequence: int = None, freeJoin: bool = None, meta: str = None,
                       moderator_only_message: str = None, auto_start_recording: bool = None,
                       allow_start_stop_recording: bool = True, webcams_only_for_moderator: bool = None,
                       logo: str = None, banner_text: str = None, banner_color: str = None, _copyright: str = None,
                       mute_on_start: bool = None, allow_mods_to_unmute_users: bool = False,
                       lock_settings_disable_cam: bool = False, lock_settings_disable_mic: bool = False,
                       lock_settings_disable_private_chat: bool = False,
                       lock_settings_disable_public_chat: bool = False, lock_settings_disable_note: bool = False,
                       lock_settings_locked_layout: bool = False, lock_settings_lock_on_join: bool = True,
                       lock_settings_lock_on_join_configurable: bool = False, guest_policy: str = None
                       ) -> CreateMeetingResponse:
        """
        https://docs.bigbluebutton.org/dev/api.html#create
        
        :param name: The name of the meeting.
        :param meeting_id: The meeting ID that identifies the meeting.
        :param attendee_pw: The attendee password for this meeting.
        :param moderator_pw: The moderator password for this meeting.
        :param welcome: The welcome message for this meeting.
        :param dial_number: The phone number to dial into this meeting.
        :param voice_bridge: The voice bridge for this meeting.
        :param max_participants: The maximum number of participants that can join this meeting.
        :param logout_url: The URL to which users will be redirected when they log out of the meeting.
        :param record: Whether to record this meeting.
        :param duration: The duration of the meeting in minutes.
        :param is_breakout: Whether this is a breakout room.
        :param parent_meeting_Id: The parent meeting ID for this meeting.
        :param sequence: The sequence number for this meeting.
        :param freeJoin: Whether the meeting is free-join.
        :param meta: The meta data for this meeting.
        :param moderator_only_message: The moderator-only message for this meeting.
        :param auto_start_recording: Whether to automatically start recording when the meeting starts.
        :param allow_start_stop_recording: Whether to allow the user to start/stop recording.
        :param webcams_only_for_moderator: Whether to allow webcams only for moderator.
        :param logo: The logo for this meeting.
        :param banner_text: The banner text for this meeting.
        :param banner_color: The banner color for this meeting.
        :param _copyright: The copyright for this meeting.
        :param mute_on_start: Whether to mute participants on start.
        :param allow_mods_to_unmute_users: Whether to allow moderators to unmute users.
        :param lock_settings_disable_cam: Whether to disable camera for participants.
        :param lock_settings_disable_mic: Whether to disable microphone for participants.
        :param lock_settings_disable_private_chat: Whether to disable private chat for participants.
        :param lock_settings_disable_public_chat: Whether to disable public chat for participants.
        :param lock_settings_disable_note: Whether to disable notes for participants.
        :param lock_settings_locked_layout: Whether to lock the layout for participants.
        :param lock_settings_lock_on_join: Whether to lock the meeting on join.
        :param lock_settings_lock_on_join_configurable: Whether to lock the meeting on join configurable.
        :param guest_policy: The guest policy for this meeting.
        """
        if not meeting_id:
            # A good choice for the meeting ID is to generate a GUID value as this all but guarantees that different
            # meetings will not have the same meetingID.
            meeting_id = self.create_meeting_id()
        data = {
            'meetingID': meeting_id
        }
        if name:
            if not isinstance(name, str):
                raise ValueError(f'name must be instance of str, not {type(name)}')
            data['name'] = name

        if attendee_pw:
            if not isinstance(attendee_pw, str):
                raise ValueError(f'attendeePW must be instance of str, not {type(attendee_pw)}')
            data['attendeePW'] = attendee_pw

        if moderator_pw:
            if not isinstance(moderator_pw, str):
                raise ValueError(f'moderatorPW must be instance of str, not {type(moderator_pw)}')
            data['moderatorPW'] = moderator_pw

        if welcome:
            if not isinstance(welcome, str):
                raise ValueError(f'welcome must be instance of str, not {type(welcome)}')
            data['welcome'] = welcome

        if dial_number:
            if not isinstance(dial_number, str):
                raise ValueError(f'dialNumber must be instance of str, not {type(dial_number)}')
            data['dialNumber'] = dial_number

        if voice_bridge:
            if not isinstance(voice_bridge, int):
                raise ValueError(f'voiceBridge must be instance of int, not {type(voice_bridge)}')
            data['voiceBridge'] = voice_bridge

        if max_participants:
            if not isinstance(max_participants, int):
                raise ValueError(f'maxParticipants must be instance of int, not {type(max_participants)}')
            data['maxParticipants'] = max_participants

        if logout_url:
            if not isinstance(logout_url, str):
                raise ValueError(f'logoutURL must be instance of str, not {type(logout_url)}')
            data['logoutURL'] = logout_url

        if record:
            if not isinstance(duration, bool):
                raise ValueError(f'duration must be instance of bool, not {type(duration)}')
            data['record'] = record

        if duration:
            if not isinstance(duration, int):
                raise ValueError(f'duration must be instance of int, not {type(duration)}')
            data['duration'] = duration

        if is_breakout:
            if not isinstance(is_breakout, bool):
                raise ValueError(f'isBreakout must be instance of bool, not {type(is_breakout)}')
            data['isBreakout'] = is_breakout
            if not parent_meeting_Id:
                raise ValueError(
                    f'If you want to create BreakOut room you must call parentMeetingID,sequence parameters')
            else:
                if not isinstance(parent_meeting_Id, str):
                    raise ValueError(f'parentMeetingID must be instance of str, not {type(parent_meeting_Id)}')
                data['parentMeetingID'] = parent_meeting_Id
            if not sequence:
                raise ValueError(
                    f'If you want to create BreakOut room you must call parentMeetingID,sequence parameters')
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

        if moderator_only_message:
            if not isinstance(moderator_only_message, str):
                raise ValueError(f'moderatorOnlyMessage must be instance of str, not {type(moderator_only_message)}')
            data['moderatorOnlyMessage'] = moderator_only_message

        if auto_start_recording:
            if not isinstance(auto_start_recording, bool):
                raise ValueError(f'autoStartRecording must be instance of bool, not {type(auto_start_recording)}')
            data['autoStartRecording'] = auto_start_recording

        if allow_start_stop_recording:
            if not isinstance(allow_start_stop_recording, bool):
                raise ValueError(
                    f'allowStartStopRecording must be instance of bool, not {type(allow_start_stop_recording)}')
            data['allowStartStopRecording'] = allow_start_stop_recording

        if webcams_only_for_moderator:
            if not isinstance(webcams_only_for_moderator, bool):
                raise ValueError(
                    f'webcamsOnlyForModerator must be instance of bool, not {type(webcams_only_for_moderator)}')
            data['webcamsOnlyForModerator'] = webcams_only_for_moderator

        if logo:
            if not isinstance(logo, str):
                raise ValueError(f'logo must be instance of str, not {type(logo)}')
            data['logo'] = logo

        if banner_text:
            if not isinstance(banner_text, str):
                raise ValueError(f'bannerText must be instance of str, not {type(banner_text)}')
            data['bannerText'] = banner_text

        if banner_text:
            if not isinstance(banner_text, str):
                raise ValueError(f'bannerText must be instance of str, not {type(banner_text)}')
            data['bannerText'] = banner_text

        if banner_color:
            if not isinstance(banner_color, str):
                raise ValueError(f'bannerColor must be instance of str, not {type(banner_color)}')
            if '#' not in banner_color:
                raise ValueError(f'You must use hex colors')
            data['bannerColor'] = banner_color

        if _copyright:
            if not isinstance(_copyright, str):
                raise ValueError(f'copyright must be instance of str, not {type(_copyright)}')
            data['copyright'] = _copyright

        if mute_on_start:
            if not isinstance(mute_on_start, bool):
                raise ValueError(f'muteOnStart must be instance of bool, not {type(mute_on_start)}')
            data['muteOnStart'] = mute_on_start

        if allow_mods_to_unmute_users:
            if not isinstance(allow_mods_to_unmute_users, bool):
                raise ValueError(
                    f'allowModsToUnmuteUsers must be instance of bool, not {type(allow_mods_to_unmute_users)}')
            data['allowModsToUnmuteUsers'] = allow_mods_to_unmute_users

        if lock_settings_disable_cam:
            if not isinstance(lock_settings_disable_cam, bool):
                raise ValueError(
                    f'lockSettingsDisableCam must be instance of bool, not {type(lock_settings_disable_cam)}')
            data['lockSettingsDisableCam'] = lock_settings_disable_cam

        if lock_settings_disable_mic:
            if not isinstance(lock_settings_disable_mic, bool):
                raise ValueError(
                    f'lockSettingsDisableMic must be instance of bool, not {type(lock_settings_disable_mic)}')
            data['lockSettingsDisableMic'] = lock_settings_disable_mic

        if lock_settings_disable_private_chat:
            if not isinstance(lock_settings_disable_private_chat, bool):
                raise ValueError(
                    f'lockSettingsDisablePrivateChat must be instance of bool, '
                    f'not {type(lock_settings_disable_private_chat)}'
                )
            data['lockSettingsDisablePrivateChat'] = lock_settings_disable_private_chat

        if lock_settings_disable_public_chat:
            if not isinstance(lock_settings_disable_public_chat, bool):
                raise ValueError(
                    f'lockSettingsDisablePublicChat must be instance of bool, '
                    f'not {type(lock_settings_disable_public_chat)}'
                )
            data['lockSettingsDisablePublicChat'] = lock_settings_disable_public_chat

        if lock_settings_disable_note:
            if not isinstance(lock_settings_disable_note, bool):
                raise ValueError(
                    f'lockSettingsDisableNote must be instance of bool, not {type(lock_settings_disable_note)}')
            data['lockSettingsDisableNote'] = lock_settings_disable_note

        if lock_settings_locked_layout:
            if not isinstance(lock_settings_locked_layout, bool):
                raise ValueError(
                    f'lockSettingsLockedLayout must be instance of bool, not {type(lock_settings_locked_layout)}')
            data['lockSettingsLockedLayout'] = lock_settings_locked_layout

        if lock_settings_lock_on_join:
            if not isinstance(lock_settings_lock_on_join, bool):
                raise ValueError(
                    f'lockSettingsLockOnJoin must be instance of bool, not {type(lock_settings_lock_on_join)}')
            data['lockSettingsLockOnJoin'] = lock_settings_lock_on_join

        if lock_settings_lock_on_join_configurable:
            if not isinstance(lock_settings_lock_on_join_configurable, bool):
                raise ValueError(
                    f'lockSettingsLockOnJoinConfigurable must be instance of bool, '
                    f'not {type(lock_settings_lock_on_join_configurable)}'
                )
            data['lockSettingsLockOnJoinConfigurable'] = lock_settings_lock_on_join_configurable

        if guest_policy:
            types = ['ALWAYS_ACCEPT', 'ALWAYS_DENY', 'ASK_MODERATOR']
            if not isinstance(guest_policy, str):
                raise ValueError(f'guestPolicy must be instance of bool, not {type(guest_policy)}')
            if guest_policy not in types:
                raise ValueError(f'Invalid guestPolicy type. Valid types are {str(types)}')
            data['guestPolicy'] = guest_policy

        query = self.app.send_request('create', params=data)
        return CreateMeetingResponse(**query)

    def join_meeting(self, full_name: str, meeting_id: str, password: str, create_time: str = None, user_id: str = None,
                     web_voice_conf: str = None, config_token: str = None,
                     default_layout: str = None, avatar_url: str = None, redirect: bool = True,
                     client_url: str = None, exclude_from_dashboard: bool = False, guest: bool = None
                     ) -> JoinMeetingResponse:
        """
        https://docs.bigbluebutton.org/dev/api.html#join

        :param full_name: The full name that is to be used to identify this user to other conference attendees.
        :param meeting_id: The meeting ID that identifies the meeting you are attempting to join.
        :param password: The password that this attendee is using. If the moderator password is supplied,
            he will be given moderator status (and the same for attendee password, etc.)
        :param create_time: The timestamp of when the meeting was created.
        :param user_id: The user ID that is to be used to identify this user to other conference attendees.
        :param web_voice_conf: The voice conference that is to be used to identify
            this user to other conference attendees.
        :param config_token: The config token that is to be used to identify this user to other conference attendees.
        :param default_layout: The default layout that is to be used to identify
            this user to other conference attendees.
        :param avatar_url: The avatar URL that is to be used to identify this user to other conference attendees.
        :param redirect: If true, the client will be redirected to the meeting URL.
        :param client_url: The client URL that is to be used to identify this user to other conference attendees.
        :param exclude_from_dashboard: If true, the client will not be shown on the BigBlueButton web dashboard.
        :param guest: If true, the user will be given guest status.
        """
        data = {
            'fullName': full_name,
            'meetingID': meeting_id,
            'password': password,
            'redirect': 'false' if not redirect else 'true',
            'excludeFromDashboard': 'true' if exclude_from_dashboard else 'false'
        }

        if create_time:
            if not isinstance(create_time, str):
                raise ValueError(f'createTime must be instance of str, not {type(create_time)}')
            data['createTime'] = create_time
        if user_id:
            if not isinstance(user_id, str):
                user_id = str(user_id)
            data['userID'] = user_id
        if web_voice_conf:
            if not isinstance(web_voice_conf, str):
                raise ValueError(f'webVoiceConf must be instance of str, not {type(web_voice_conf)}')
            data['webVoiceConf'] = web_voice_conf
        if config_token:
            if not isinstance(config_token, str):
                raise ValueError(f'configToken must be instance of str, not {type(config_token)}')
            data['configToken'] = config_token
        if default_layout:
            if not isinstance(default_layout, str):
                raise ValueError(f'defaultLayout must be instance of str, not {type(default_layout)}')
            data['defaultLayout'] = default_layout
        if avatar_url:
            if not isinstance(avatar_url, str):
                raise ValueError(f'avatarURL must be instance of str, not {type(avatar_url)}')
            data['avatarURL'] = avatar_url
        if redirect:
            if not isinstance(redirect, bool):
                raise ValueError(f'redirect must be instance of bool, not {type(redirect)}')
            data['redirect'] = redirect
        if client_url:
            if not isinstance(client_url, str):
                raise ValueError(f'clientURL must be instance of str, not {type(client_url)}')
            data['clientURL'] = client_url
        if guest:
            if not isinstance(guest, bool):
                raise ValueError(f'guest must be instance of bool, not {type(guest)}')
            data['guest'] = guest

        if redirect:
            query = self.app.send_request('join', params=data, just_create=True)
            return query
        query = self.app.send_request('join', params=data, just_create=True)
        return JoinMeetingResponse(**query)

    def is_meeting_running(self, meeting_id: str):
        """
        https://docs.bigbluebutton.org/dev/api.html#ismeetingrunning

        :param meeting_id: The meeting ID that identifies the meeting you are attempting to check on.
        """
        if not isinstance(meeting_id, str):
            meeting_id = str(meeting_id)
        data = {
            'meetingID': meeting_id
        }
        query = self.app.send_request('isMeetingRunning', params=data)
        return query.get('running') == 'true'

    def end_meeting(self, meeting_id: str, password):
        """
        https://docs.bigbluebutton.org/dev/api.html#end

        :param meeting_id: The meeting ID that identifies the meeting you are attempting to end.
        :param password: The moderator password for this meeting. You can not end a meeting using the attendee password.
        """
        if not isinstance(meeting_id, str):
            meeting_id = str(meeting_id)
        data = {
            'meetingID': meeting_id,
            'password': password
        }
        query = self.app.send_request('end', params=data)
        return EndMeetingResponse(**query)

    def get_meeting_info(self, meeting_id: str):
        """
        https://docs.bigbluebutton.org/dev/api.html#getmeetinginfo

        :param meeting_id: The meeting ID that identifies the meeting you are attempting to check on.
        """
        if not isinstance(meeting_id, str):
            meeting_id = str(meeting_id)
        data = {
            'meetingID': meeting_id
        }
        query = self.app.send_request('getMeetingInfo', params=data)
        response = {
            **query,
            'attendees': []
        }

        if isinstance(query['attendees']['attendee'], list):
            for attendee in query['attendees']['attendee']:
                response['attendees'].append(Attendee(**attendee))
        else:
            response['attendees'].append(Attendee(**query['attendees']['attendee']))

        return GetMeetingInfoResponse(**response)

    def get_meetings(self):
        """
        https://docs.bigbluebutton.org/dev/api.html#getmeetings
        """
        query = self.app.send_request('getMeetings')
        data = {
            **query,
            'meetings': []
        }

        for meeting in query['meetings']['meeting']:
            data['meetings'].append(GetMeetingInfoResponse(**meeting))

        return GetMeetingsResponse(**data)

    def insert_document(
            self, meeting_id: str, file_path: str,
            file_name: str = None, removable: bool = False,
            downloadable: bool = False
    ):
        """
        https://docs.bigbluebutton.org/dev/api.html#insertdocument

        :param meeting_id: The meeting ID that identifies the meeting you are attempting to check on.
        :param file_path: The path to the document you wish to upload.
        :param file_name: The name of the document you wish to upload.
        :param removable: If true, the document will be marked as removable.
        :param downloadable: If true, the document will be marked as downloadable.
        """
        data = {
            'meetingID': meeting_id
        }
        query = self.app.send_request('insertDocument', params=data, data=utils.generate_file_upload_xml(
            file_path=file_path, name=os.path.basename(file_path) if not file_name else file_name,
            removable=removable, downloadable=downloadable
        ))
        return query
