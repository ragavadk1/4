import requests
import re
import json
import os

#org
#__ = {'csrftoken': 'ORIQsBXGouDFzpd1VmF8K5GchvHGlGLN', 'rur': '\"VLL\\0548510847248\\0541752299374:01f7a430cf0c607ba0f4a6afb8f9b3b8dde6feaa399e85302c119932418f457214e2a63f\"', 'mid': 'Zki-HwALAAHGxyPe3ATMxcewqF5-', 'ds_user_id': '8510847248', 'ig_did': '174B4DF3-F44A-43B1-8FE5-B65885FB0256', 'sessionid': '8510847248%3AqrRw5zWeND3mxR%3A25%3AAYe2Z86MFJ3UvoyPHk78MzGblSuoPnouZW9-0TUczA'}

#dup
__ = {'csrftoken': '30DWARI3KYNCwwLVwAJcgk9UvYuaDprV', 'rur': '"CCO\\05451941737982\\0541752503674:01f7f7ee3b04c8a482feae83d829462f0b64c53c8ba5f6f858124217ba2822f1a7d03cfe"', 'mid': 'ZpPh9QALAAEzuDejuFXnTExbR64U', 'ds_user_id': '51941737982', 'ig_did': '50F439F2-69F5-401B-B6F5-80DE9691328E', 'sessionid': '51941737982%3AD4kCrUJkf1t75I%3A10%3AAYeYFLZhm5_x-6h3nlRYy_hracihne8nWCVBK1aPuQ'}
session = requests.session()
Cookies = __

csrf = Cookies["csrftoken"]
id = Cookies["ds_user_id"]

cookies = requests.utils.cookiejar_from_dict(Cookies)
session.cookies.update(cookies)

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Priority': 'u=1, i',
    'Referer': 'https://www.instagram.com/settings/help/account_status/?hl=en',
    'sec-ch-prefers-color-scheme': 'light',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-csrftoken': f'{csrf}',
    'x-ig-app-id': '936619743392459',
    'X-Requested-With': 'XMLHttpRequest',
}

session.headers = headers
data = {
    'broadcast_message': 'Fun with horrors - evil within 1',
    'internal_only': 'false',
    'preview_height': '1920',
    'preview_width': '1080',
    'source_type': '5',
    'broadcast_type': 'RTMP',
    'visibility': '0'
}


res = session.post("https://www.instagram.com/api/v1/live/create/", params={'hl': 'en'}, data=data)
p6 = res.json()
print(p6)
broadcastid = p6['broadcast_id']
upload_url = p6['upload_url']
print(upload_url)
print(broadcastid)

rr = session.post(f"https://www.instagram.com/api/v1/live/{broadcastid}/start/", data={'should_send_notifications': 1})



#os.system(f"ffmpeg -probesize 200 -analyzeduration 100 -re -i '{pr}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,setpts=0\" -tune zerolatency -threads 4 -map 0:p:6 -b:v 8000k -acodec copy -g 60 -f flv rtmp://a.rtmp.youtube.com/live2/qtaa-xx6x-h99h-hjtp-1wf1")


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

os.system(f"ffmpeg -headers $'User-Agent: Mozilla/5.0 (Android; vivo V2311) Android/14 version/1.17.74\r\nHost: livestreamc.prdv3.dlivecdn.com\r\nConnection: Keep-Alive\r\nAccept-Encoding: identity\r\nReferer: https://dlive.tv/\r\n' -i '{esponse44}' -vf transpose=1 -threads 4 -vcodec libx264 -b:v 9000k -acodec copy -preset ultrafast -tune zerolatency -flags low_delay -fflags '+nobuffer+flush_packets' -max_delay 0 -muxdelay 0 -x264opts keyint=30 -f flv '{upload_url}'")
