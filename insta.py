import re
import json
import os
import requests

headers = {
    'User-Agent': 'Instagram 332.0.0.38.90 Android (34/14; 396dpi; 1080x2238; vivo; V2311; V2225; mt6833; en_IN; 601420827)',
    'Accept-Language': 'en-IN, en-US',
    'Authorization': 'Bearer IGT:2:eyJkc191c2VyX2lkIjoiNTE5NDE3Mzc5ODIiLCJzZXNzaW9uaWQiOiI1MTk0MTczNzk4MiUzQTRFQkFoOXAxOXRqOGFIJTNBMyUzQUFZYzBPdG9xbkszY1FTdm9lSy1vQl9lc1lGYXFBMkFBX0tVSjVDQ3NhZyJ9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection': 'Keep-Alive',
}

data = {
    'broadcast_message': 'Shit',
    'user_pay_enabled': 'true',
    'source_type': '5',
    'preview_height': '1920',
    'should_use_rsys_rtc_infra': 'true',
    'broadcast_type': 'RTMP',
    'preview_width': '1080',
    'sup_active': 'true',
    'internal_only': 'false',
    'visibility': '0',
}

response = requests.post('https://i.instagram.com/api/v1/live/create/', headers=headers, data=data)

p7 = response.json()
print(p7)
broadcastid = p7['broadcast_id']
upload_url = p7['upload_url']
print(upload_url)
print(broadcastid)

rr = requests.post(f"https://i.instagram.com/api/v1/live/{broadcastid}/start/", headers=headers, data={'should_send_notifications': 1})
print(rr.text)

headers = {
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-platform': '"Android"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://dlive.tv',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://dlive.tv/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
}

url = re.findall("https://.*/src/live.m3u8", requests.get("https://live.prd.dlive.tv/hls/live/dlive-05900794.m3u8").text)[0]

json_data = {
    'playlisturi': f'{url}'
}

esponse44 = requests.post('https://live.prd.dlive.tv/hls/sign/url', headers=headers, json=json_data).text

os.system(f"ffmpeg -headers $'User-Agent: Mozilla/5.0 (Android; vivo V2311) Android/14 version/1.17.74\r\nHost: livestreamc.prdv3.dlivecdn.com\r\nConnection: Keep-Alive\r\nAccept-Encoding: identity\r\nReferer: https://dlive.tv/\r\n' -i '{esponse44}' -vf transpose=1 -threads 4 -vcodec libx264 -b:v 9000k -acodec copy -preset ultrafast -tune zerolatency -flags low_delay -fflags '+nobuffer+flush_packets' -max_delay 0 -muxdelay 0 -qp 0 -f flv '{upload_url}'")
