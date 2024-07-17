import requests
import re
import json
import os
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
print(esponse44)

os.system(f"ffmpeg -headers $'User-Agent: Mozilla/5.0 (Android; vivo V2311) Android/14 version/1.17.74\r\nHost: livestreamc.prdv3.dlivecdn.com\r\nConnection: Keep-Alive\r\nAccept-Encoding: identity\r\nReferer: https://dlive.tv/\r\n' -i '{esponse44}' -threads 4 -vcodec libx264 -b:v 9000k -preset ultrafast -tune zerolatency -flags low_delay -fflags '+nobuffer+flush_packets' -max_delay 0 -muxdelay 0 -x264opts keyint=30 -acodec copy -f flv 'rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js'")

# su2299515339885rcaf93ac2e0aee5c25cedf5d4c5fadf81?guid=0aa89b1d4ad38c663d01621d631d83b1&hyapp=81&hymuid=2299515339885&hyroom=4490358181&psign=7a30ad473706180969f1b16722a064a5&rtag=cah5FXgQJ9&sru=Q9I63Q2I1&txHost=txpush.rtmp.nimo.tv&ua=d2ViJjEuMC40Jm5pbW9UVg==&appid=81&room=4490358181&muid=4599030693329&seq=1721010178435&streamcode=huya_inner_user
