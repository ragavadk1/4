import requests
import json
import re
import os
cookies = {
    'PREF': 'hl=en&tz=UTC',
    'SOCS': 'CAI',
    'GPS': '1',
    'YSC': 'G5P-C1Yb9HA',
    'VISITOR_INFO1_LIVE': 'bRix5ZcqxGE',
    'VISITOR_PRIVACY_METADATA': 'CgJJThIEGgAgKg%3D%3D',
}
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'com.google.ios.youtube/19.29.1 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X;)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us,en;q=0.5',
    'Sec-Fetch-Mode': 'navigate',
    'X-Youtube-Client-Name': '5',
    'X-Youtube-Client-Version': '19.29.1',
    'Origin': 'https://www.youtube.com',
}
params = {
    'key': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
    'prettyPrint': 'false',
}
json_data = {
    'context': {
        'client': {
            'clientName': 'IOS',
            'clientVersion': '19.29.1',
            "deviceMake": "Apple",
            'deviceModel': 'iPhone16,2',
            'userAgent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
            "osVersion": "17.5.1.21F90",
            'hl': 'en',
            'timeZone': 'UTC',
            'utcOffsetMinutes': 0,
        },
    },
    'videoId': 'KcrMssDp8Mo',
    'playbackContext': {
        'contentPlaybackContext': {
            'html5Preference': 'HTML5_PREF_WANTS',
        },
    },
    'contentCheckOk': True,
    'racyCheckOk': True,
}
response = requests.post(
    'https://www.youtube.com/youtubei/v1/player',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
pr = json.loads(response.text)
print(pr)
"""
#aq = pr['streamingData']["adaptiveFormats"]
print(aq)
#pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]
#print(response.text)
l = []
for __ in aq:
    if "1080p" in str(__) and "mp4" in str(__):
        l.append(__)
    if "AUDIO_QUALITY_MEDIUM" in str(__) and not 'isDrc' in str(__):
        l.append(__)
v = l[0]['url']
a = l[-1]['url']
print("AUDIO : ", a)
print("VIDEO : ", v)

#os.system(f"ffmpeg -ss 7:00:00 -to 10:00:00 -re -i '{v}' -ss 7:00:00 -to 10:00:00 -re -i '{a}' -threads 4 -vcodec libx264 -b:v 9000k -c:a copy -preset ultrafast -tune zerolatency -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js")
"""