# bigbluebutton-python
### An unofficial bigbluebutton python api library. enjoy!

- [X] create
- [X] join
- [X] isMeetingRunning
- [X] end
- [X] getMeetingInfo
- [X] getMeeting
## Installation
```
pip3 install bigbluepy
```

```python

from bigbluepy import MainBBB

bbb = MainBBB("BBB_SERVICE_URL", "BBB_SECRET_KEY")

response = bbb.api.getMeetings()

for i in response.meetings['meeting']:
    print(i['meetingID'])

```