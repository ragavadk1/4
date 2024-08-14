import requests
import json
import re
import os
"""
cookies = {
    'PREF': 'hl=en&tz=UTC',
    'SOCS': 'CAI',
    'GPS': '1',
    'YSC': 'G5P-C1Yb9HA',
    'VISITOR_INFO1_LIVE': 'bRix5ZcqxGE',
    'VISITOR_PRIVACY_METADATA': 'CgJJThIEGgAgKg%3D%3D',
}
"""
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
    'videoId': 'gdmMZRH34uE',
    'playbackContext': {
        'contentPlaybackContext': {
            'html5Preference': 'HTML5_PREF_WANTS',
        },
    },
    'contentCheckOk': True,
    'racyCheckOk': True,
}
cookies = {
    'SOCS': 'CAISOAgDEitib3FfaWRlbnRpdHlmcm9udGVuZHVpc2VydmVyXzIwMjQwNTEyLjA3X3AwGgVlbi1JTiACGgYIgJmVsgY',
    'VISITOR_PRIVACY_METADATA': 'CgJEWhIEGgAgOw%3D%3D',
    'VISITOR_INFO1_LIVE': '6k3DyB1Zghs',
    'PREF': 'f7=4000&tz=Asia.Calcutta&f4=4000000',
    'GPS': '1',
    'HSID': 'AvzEKD5_6XpSW6Xtx',
    'SSID': 'AJbP-SMbz6tv96KZe',
    'APISID': '_yI5OpDtfGdPg87H/AdzktGxrSoqTCvHYm',
    'SAPISID': '7T-VKOBJGLFdIoWg/AymhvIM25MLnFao4h',
    '__Secure-1PAPISID': '7T-VKOBJGLFdIoWg/AymhvIM25MLnFao4h',
    '__Secure-3PAPISID': '7T-VKOBJGLFdIoWg/AymhvIM25MLnFao4h',
    'SID': 'g.a000mwhGw29_N_hjTgU_7PAAWjT8qiXwy3UxD8rzheShTWTsstWyWBmnJ3sfq-_2UqZ25p7sSwACgYKAZESARASFQHGX2Mi5Epu9_EvKMh9HfJol3qhRBoVAUF8yKrifCHV6BrUFmp-_IVECMv50076',
    '__Secure-1PSID': 'g.a000mwhGw29_N_hjTgU_7PAAWjT8qiXwy3UxD8rzheShTWTsstWyp2rLdp_55Wkm4_aVE7azcQACgYKAeoSARASFQHGX2Mi061vG4WDw0dJK61CutP-3RoVAUF8yKoI_8K27cNhJK1C27vVy2NM0076',
    '__Secure-3PSID': 'g.a000mwhGw29_N_hjTgU_7PAAWjT8qiXwy3UxD8rzheShTWTsstWyyCj7LxsRqoHr9EwJLFwEpQACgYKAfUSARASFQHGX2MiLaQ4UqUokS6SUA2cd123GxoVAUF8yKrn3TMX6t6Gb31HrhUVZKDk0076',
    '__Secure-1PSIDTS': 'sidts-CjEBUFGoh0G4S-EMeMrDBNV_FzeqdNJZO3I-n8jZvezKi-XgEcJIuDkzGuwQb3IqHbF2EAA',
    '__Secure-3PSIDTS': 'sidts-CjEBUFGoh0G4S-EMeMrDBNV_FzeqdNJZO3I-n8jZvezKi-XgEcJIuDkzGuwQb3IqHbF2EAA',
    'LOGIN_INFO': 'AFmmF2swRgIhAMcMyS9oN7zw3vf8__1G2wDkDQWC6jE5Is37xWvsjsMuAiEA3MaZpdtOXY71iei97k1_v7O_f9EZnKaMSYrJNm4f9Ao:QUQ3MjNmeVd5OXdRNUdRcXN2Q0ZMTG92UERjaXlDYmRoa1JTa19rcnNfcm4xd1EwZ25jUU1kd2o0ZHdYRFo4WGtnRVoyQ2RxOVhtemlPZU9lckdQaThNR1hvcFNyY3p1MFc2ZzdPUUtzVlBUd3VBYkFqUDRmTlVCMzRDU2NYR2xPUTNDSjZRazhVVFpjdjJncXZkRlQ3YXdfVHJIeXlTSTF3',
    'SIDCC': 'AKEyXzW0IzIDsXtCviPTQYrrA_m6f2Sc0C9KFTlB9ias0XwGRCXZBBTZ7F_XmXjpvRNqIc-P',
    '__Secure-1PSIDCC': 'AKEyXzXwwvVGlDvJt44um2jss038cxqCT6yTcQbDDuyPDSrWZY0GfMa1JofJxXTIZs6oSNYX-A',
    '__Secure-3PSIDCC': 'AKEyXzW2IjGU6-u8RJ0oNBRUDn40PFK0JC4Q_evVeHeLb4xCYhMu7LEdf779Pm31ePs_SuFS'
}
response = requests.post(
    'https://www.youtube.com/youtubei/v1/player',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
pr = json.loads(response.text)["streamingData"]["adaptiveFormats"]
print(pr)


#aq = pr['streamingData']["adaptiveFormats"]
#print(aq)
#pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]
#print(response.text)
l = []
for __ in pr:
    if "1080p" in str(__) and "mp4" in str(__):
        l.append(__)
    if "AUDIO_QUALITY_MEDIUM" in str(__) and not 'isDrc' in str(__):
        l.append(__)
v = l[0]['url']
a = l[-1]['url']
print("AUDIO : ", a)
print("VIDEO : ", v)

os.system(f"ffmpeg -ss 7:00:00 -to 10:00:00 -re -i '{v}' -ss 7:00:00 -to 10:00:00 -re -i '{a}' -threads 4 -vcodec libx264 -b:v 9000k -c:a copy -preset ultrafast -tune zerolatency -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js")
