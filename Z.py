import requests
import json
import re
import os

cookies = {
    'ST-17nskln': 'itct=CLADEKQwGAEiEwjEzuiFifqHAxXBgmMGHY0hLwwyB3JlbGF0ZWRIrYHp0Mej2a6OAZoBBQgBEPgd&csn=k5sALznerfeekHse&session_logininfo=AFmmF2swRAIgPpgFTCYVhzMZTV-rUjxUDbp2g43WT8AjQDhXPDi_C2MCIA7wVzCPDvzNY5PBig_WVXmUlbuZRmkZ0tpTVz6oI6O7%3AQUQ3MjNmenhnRUh6UE4yazhGYkJhRXIyaURfLTNpTEVfWHUxLXpUTk9UZGhRTE0tRTRTaGtxSklnd2E5ek1NYWR5NmFPUGRXUGF2RkFHbU1JVXNEZGVzSTFhZ1RZeU12QXVJVmxSakdZZWVxR2lRTmpuRnVwbWJUTTlxeVBXLWJSWHhVa093Yzc0U3AzU3VQLUsxbkxER0pZUWZJSHBvNmxR&endpoint=%7B%22clickTrackingParams%22%3A%22CLADEKQwGAEiEwjEzuiFifqHAxXBgmMGHY0hLwwyB3JlbGF0ZWRIrYHp0Mej2a6OAZoBBQgBEPgd%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fwatch%3Fv%3D669eV_kjAmQ%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_WATCH%22%2C%22rootVe%22%3A3832%7D%7D%2C%22watchEndpoint%22%3A%7B%22videoId%22%3A%22669eV_kjAmQ%22%2C%22nofollow%22%3Atrue%2C%22watchEndpointSupportedOnesieConfig%22%3A%7B%22html5PlaybackOnesieConfig%22%3A%7B%22commonConfig%22%3A%7B%22url%22%3A%22https%3A%2F%2Frr8---sn-ci5gup-jwce.googlevideo.com%2Finitplayback%3Fsource%3Dyoutube%26oeis%3D1%26c%3DWEB%26oad%3D3200%26ovd%3D3200%26oaad%3D11000%26oavd%3D11000%26ocs%3D700%26oewis%3D1%26oputc%3D1%26ofpcc%3D1%26siu%3D1%26msp%3D1%26odepv%3D1%26id%3Debaf5e57f9230264%26ip%3D2401%253A4900%253A8824%253A42c5%253A6de7%253Afdec%253A1a33%253A194c%26initcwndbps%3D1815000%26mt%3D1723830090%26oweuc%3D%26pxtags%3DCg4KAnR4Egg1MTE4MTI5Nw%26rxtags%3DCg4KAnR4Egg1MTE4MTI5Ng%252CCg4KAnR4Egg1MTE4MTI5Nw%252CCg4KAnR4Egg1MTE4MTI5OA%22%7D%7D%7D%7D%7D',
    'SIDCC': 'AKEyXzX64KuUsAH5xAe5_Hc6LxogZ52M2E4-1x3YeK3W3rkrdSJUFMetw5_wLx97Qq3yMszlXQ',
    '__Secure-1PSIDCC': 'AKEyXzWv71IKt37tRWJ6jRASMc2akQ-kpN_a-D2aTaPk87xgTQCTAj5JOoh4FcIRE3hdZoHwQg',
    '__Secure-3PSIDCC': 'AKEyXzUdmF5uCb2N811wm-E7FKUOz06xdhDeR8xALKtyVPhGT4XT7VbQKBefnALJMcgxE8pH5w',
    'PREF': 'f6=40000000&tz=Asia.Calcutta&f4=4000000&f7=100',
    'ST-xuwub9': 'session_logininfo=AFmmF2swRAIgPpgFTCYVhzMZTV-rUjxUDbp2g43WT8AjQDhXPDi_C2MCIA7wVzCPDvzNY5PBig_WVXmUlbuZRmkZ0tpTVz6oI6O7%3AQUQ3MjNmenhnRUh6UE4yazhGYkJhRXIyaURfLTNpTEVfWHUxLXpUTk9UZGhRTE0tRTRTaGtxSklnd2E5ek1NYWR5NmFPUGRXUGF2RkFHbU1JVXNEZGVzSTFhZ1RZeU12QXVJVmxSakdZZWVxR2lRTmpuRnVwbWJUTTlxeVBXLWJSWHhVa093Yzc0U3AzU3VQLUsxbkxER0pZUWZJSHBvNmxR',
    '__Secure-1PSIDTS': 'sidts-CjEBUFGoh1GhQYk0_G5SCnBDfpX0EOpmUp1na31Bl02HsF5ciAh2iB4qn-veQOBLFZcDEAA',
    '__Secure-3PSIDTS': 'sidts-CjEBUFGoh1GhQYk0_G5SCnBDfpX0EOpmUp1na31Bl02HsF5ciAh2iB4qn-veQOBLFZcDEAA',
    'APISID': 'LgzI5IkvUrC519Kl/AGoWnwSv2_yBl_G-3',
    'HSID': 'AqaJcGw5Goks0UDJQ',
    'LOGIN_INFO': 'AFmmF2swRAIgPpgFTCYVhzMZTV-rUjxUDbp2g43WT8AjQDhXPDi_C2MCIA7wVzCPDvzNY5PBig_WVXmUlbuZRmkZ0tpTVz6oI6O7:QUQ3MjNmenhnRUh6UE4yazhGYkJhRXIyaURfLTNpTEVfWHUxLXpUTk9UZGhRTE0tRTRTaGtxSklnd2E5ek1NYWR5NmFPUGRXUGF2RkFHbU1JVXNEZGVzSTFhZ1RZeU12QXVJVmxSakdZZWVxR2lRTmpuRnVwbWJUTTlxeVBXLWJSWHhVa093Yzc0U3AzU3VQLUsxbkxER0pZUWZJSHBvNmxR',
    'SAPISID': 'XpfIQLmA8vJjQG96/ApuF1_l7buvQZqe4A',
    'SID': 'g.a000nAiP2p1gD864T_YjGO-oceiiTrS0FezL8vtr3qrIam9eQBvC-hhAUl36E5dzm3Z3L0zVVQACgYKAdkSARYSFQHGX2MiMDBrf-c1vishSV5WeH4c7BoVAUF8yKp9O3ebl6cZu6P2XHuKx96O0076',
    'SSID': 'AwbVxOFdExG_yY0w6',
    '__Secure-1PAPISID': 'XpfIQLmA8vJjQG96/ApuF1_l7buvQZqe4A',
    '__Secure-1PSID': 'g.a000nAiP2p1gD864T_YjGO-oceiiTrS0FezL8vtr3qrIam9eQBvCF2mM-bOuY00UY0prtyk1uAACgYKAUQSARYSFQHGX2Mi5f54J-VP4NXL4DYEc1kg-RoVAUF8yKqQ1ELeaq_lWVfUAMY4fum80076',
    '__Secure-3PAPISID': 'XpfIQLmA8vJjQG96/ApuF1_l7buvQZqe4A',
    '__Secure-3PSID': 'g.a000nAiP2p1gD864T_YjGO-oceiiTrS0FezL8vtr3qrIam9eQBvC0JzkIJOzpmPGw9xYPOMIFQACgYKAVsSARYSFQHGX2MiGkTFTQtGz5TU4MnAuotdyhoVAUF8yKrCsL14w6eMPUUyva9ZIAcV0076',
    'GPS': '1',
    'VISITOR_INFO1_LIVE': 'JGMGkoxlU1U',
    'VISITOR_PRIVACY_METADATA': 'CgJJThIEGgAgUQ%3D%3D',
    'YSC': '9FAfqXmzcww',
}

headers = {
    'referer': 'https://www.youtube.com/watch?v=gnWjCFt39jU',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15',
    'x-goog-visitor-id': 'CgtKR01Ha294bFUxVSjmof61BjIKCgJJThIEGgAgUQ%3D%3D',
    'x-goog-authuser': '0',
    'origin': 'https://www.youtube.com',
    'sec-fetch-dest': 'empty',
    'x-youtube-bootstrap-logged-in': 'true',
    'sec-fetch-site': 'same-origin',
    'x-youtube-client-name': '1',
    'authorization': 'SAPISIDHASH 1723830509_6a8510083695edf4b0c38f3a3ea9dc397e1bbc37',
    'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8',
    'x-origin': 'https://www.youtube.com',
    'accept': '*/*',
    'content-type': 'application/json',
    'x-youtube-client-version': '2.20240816.01.00',
    'sec-fetch-mode': 'same-origin',
}

params = {
    'prettyPrint': 'false',
}

json_data = {
    'context': {
        'client': {
            'hl': 'en',
            'gl': 'IN',
            'remoteHost': '2401:4900:8824:42c5:6de7:fdec:1a33:194c',
            'deviceMake': 'Apple',
            'deviceModel': '',
            'visitorData': 'CgtKR01Ha294bFUxVSjmof61BjIKCgJJThIEGgAgUQ%3D%3D',
            'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15,gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': '2.20240816.01.00',
            'osName': 'Macintosh',
            'osVersion': '10_15_7',
            'originalUrl': 'https://www.youtube.com/watch?v=gnWjCFt39jU',
            'screenPixelDensity': 2,
            'platform': 'DESKTOP',
            'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
            'configInfo': {
                'appInstallData': 'COah_rUGEI2UsQUQmZixBRCmkrEFEInorgUQzN-uBRCTtrEFEJrwrwUQkq6xBRCIh7AFEPSrsAUQg7n_EhDj0bAFEO6irwUQxJKxBRDr6P4SEJajsQUQsO6wBRDX6a8FENCNsAUQi7SxBRCKsLEFELfvrwUQha6xBRDd6P4SEIjjrwUQk_yvBRDdrbEFEL22rgUQlImxBRDT4a8FEKKBsAUQt-r-EhCgsLEFEPirsQUQtKCxBRCdprAFEParsAUQyfevBRCmmrAFEKaTsQUQ5fSwBRCe0LAFEL6KsAUQ74ixBRDrmbEFEKiSsQUQro__EhCinbEFEKXC_hIQ1t2wBRDGpLEFEKiTsQUQlpWwBRDJ17AFEKiasAUQlP6wBRCOtLEFENuvrwUQvZmwBRDf9bAFEAAQsdywBRDViLAFEKrYsAUQ4eywBRDqw68FEO_NsAUQ_4ixBRDjxP8SEPyFsAUQyeawBRCNzLAFENnJrwUQzdewBRDSsLEFEOLUrgUQkMawBRDTs7EFEM-xsQUQrsT_EhDX7a0FKiRDQU1TRnhVVW9MMndETURXRHRrN284ZnBDNFNvQVAtMEJoMEg%3D',
            },
            'screenDensityFloat': 2,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
            'timeZone': 'Asia/Calcutta',
            'browserName': 'Safari',
            'browserVersion': '17.5',
            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'deviceExperimentId': 'ChxOelF3TXpjNU5UWXpNVFF3T1RRek1qTTFNdz09EOah_rUGGOah_rUG',
            'screenWidthPoints': 844,
            'screenHeightPoints': 874,
            'utcOffsetMinutes': 330,
            'clientScreen': 'WATCH',
            'mainAppWebInfo': {
                'graftUrl': '/watch?v=gnWjCFt39jU',
                'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                'isWebNativeShareAvailable': True,
            },
        },
        'user': {
            'lockedSafetyMode': False,
        },
        'request': {
            'useSsl': True,
            'internalExperimentFlags': [],
            'consistencyTokenJars': [],
        },
        'clickTracking': {
            'clickTrackingParams': 'CLADEKQwGAEiEwjEzuiFifqHAxXBgmMGHY0hLwwyB3JlbGF0ZWRIrYHp0Mej2a6OAZoBBQgBEPgd',
        },
        'adSignalsInfo': {
            'params': [
                {
                    'key': 'dt',
                    'value': '1723830503446',
                },
                {
                    'key': 'flash',
                    'value': '0',
                },
                {
                    'key': 'frm',
                    'value': '0',
                },
                {
                    'key': 'u_tz',
                    'value': '330',
                },
                {
                    'key': 'u_his',
                    'value': '3',
                },
                {
                    'key': 'u_h',
                    'value': '1024',
                },
                {
                    'key': 'u_w',
                    'value': '768',
                },
                {
                    'key': 'u_ah',
                    'value': '768',
                },
                {
                    'key': 'u_aw',
                    'value': '1024',
                },
                {
                    'key': 'u_cd',
                    'value': '24',
                },
                {
                    'key': 'bc',
                    'value': '31',
                },
                {
                    'key': 'bih',
                    'value': '619',
                },
                {
                    'key': 'biw',
                    'value': '704',
                },
                {
                    'key': 'brdim',
                    'value': '0,0,0,0,1024,0,704,768,844,874',
                },
                {
                    'key': 'vis',
                    'value': '1',
                },
                {
                    'key': 'wgl',
                    'value': 'true',
                },
                {
                    'key': 'ca_type',
                    'value': 'image',
                },
            ],
        },
    },
    'videoId': 'RqEkCBBEP6I',
    'playbackContext': {
        'contentPlaybackContext': {
            'currentUrl': '/watch?v=RqEkCBBEP6I',
            'vis': 0,
            'splay': False,
            'autoCaptionsDefaultOn': False,
            'autonavState': 'STATE_NONE',
            'html5Preference': 'HTML5_PREF_WANTS',
            'signatureTimestamp': 19949,
            'referer': 'https://www.youtube.com/watch?v=kAmUDo_-5PI',
            'lactMilliseconds': '-1',
            'watchAmbientModeContext': {
                'hasShownAmbientMode': True,
                'watchAmbientModeEnabled': True,
            },
        },
    },
    'racyCheckOk': False,
    'contentCheckOk': False,
}

response = requests.post(
    'https://www.youtube.com/youtubei/v1/player',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]
print(pr)

#os.system(f"ffmpeg -http_persistent 0 -re -i '{pr}' -threads 4 -vf \"format=yuv420p\" -c:v libx264 -g 48 -b:v 9000k -c:a copy -preset ultrafast -tune zerolatency -f flv rtmp://a.rtmp.youtube.com/live2/gkjq-gc2k-hbcc-3jwq-9pp6")

#os.system(f"ffmpeg -http_persistent 0 -ss 00:00:00 -re -i '{pr}' -threads 4 -vf \"format=yuv420p,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=18:box=0:boxcolor=black@0.5:boxborderw=15:x=w-tw:y=h-th\" -c:v libx264 -g 48 -b:v 9000k -c:a copy -preset ultrafast -tune zerolatency -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js")
os.system(f"ffmpeg -http_persistent 0 -ss 00:00:00 -re -i '{pr}' -threads 4 -vcodec copy -c:a copy -preset ultrafast -tune zerolatency -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js")
