from bigbluepy.main import MainBBB

bbb = MainBBB(
    service_url='https://test-install.blindsidenetworks.com/bigbluebutton/api/',
    secret='8cd8ef52e8e101574e400365b55e11a6'
)

_response = bbb.api.create_meeting(
    name='Test Meeting'
)

print(
    '[+] Meeting created:',
    _response,
)
