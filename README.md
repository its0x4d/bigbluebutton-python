# bigbluebutton-python
#### An unofficial bigbluebutton python api library.
```python

from bigbluepython import MainBBB

bbb = MainBBB(BBB_SERVICE_URL, BBB_SECRET_KEY)

meetings = bbb.api.getMeetings()

for i in meetings:
    print(i.meetingID)

```