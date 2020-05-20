# bigbluebutton-python

```python

from bigbluepython import MainBBB

bbb = MainBBB(SERVICE_URL, SECRET_KEY)

meetings = bbb.api.getMeetings()

for i in meetings:
    print(i.meetingID)

```