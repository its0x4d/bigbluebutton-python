# bigbluebutton-python
### An unofficial bigbluebutton python api library. enjoy!

- [X] create
- [X] join
- [X] isMeetingRunning
- [X] end
- [X] getMeetingInfo
- [X] getMeeting
- [X] InsertDocument
## Installation
```
pip3 install bigbluepy
```
## Manual Installation
```
git clone https://github.com/its0x4d/bigbluebutton-python
pip3 install -r requirments.txt
python3 setup.py install
```
## Code Example
```python

from bigbluepy import MainBBB

bbb = MainBBB("BBB_SERVICE_URL", "BBB_SECRET_KEY")

response = bbb.api.getMeetings()

for i in response.meetings['meeting']:
    print(i['meetingID'])

```