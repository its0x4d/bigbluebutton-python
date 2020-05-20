from bbb_monitor import MainBBB


bbb = MainBBB('https://live.youmeet.ir/bigbluebutton/api/', 'wgYvfg2bzzeYlNmZdhfOlYXLQXT4bLZ8a5zDbqvyjGg')

s = bbb.send_request('getMeetings', 1)
print(s)