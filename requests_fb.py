import requests
import json
import sys

class requests_fb:
    def __init__(self,cookie):
        self.httpx = requests.Session()
        self.header_get = {
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language":'en-US,en;q=0.9',
        "cache-control":"max-age=0",
        "cookie": cookie,
        "dpr":"1",
        "priority":"u=0, i",
        "referer":"https://www.facebook.com/",
        "sec-ch-prefers-color-scheme":"drak",
        "sec-ch-ua":'"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-full-version-list":'"Google Chrome";v="137.0.7151.120", "Chromium";v="137.0.7151.120", "Not/A)Brand";v="24.0.0.0"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-model":"",
        "sec-ch-ua-platform":"Windows",
        "sec-ch-ua-platform-version":"10.0.0",
        "sec-fetch-dest":"document",
        "sec-fetch-mode":"navigate",
        "sec-fetch-site":"none",
        "sec-fetch-user":"?1",
        "upgrade-insecure-requests":"1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        }
        self.header_post = {"accept":"*/*",
        "accept-encoding":"gzip, deflate, br, zstd",
        "accept-language":'en-US,en;q=0.9',
        "content-length":"6412",
        "content-type":"application/x-www-form-urlencoded",
        "cookie": cookie,
        'Pragma': 'no-cache',
        "dpr":"1",
        "origin":"https://www.facebook.com",
        "priority":"u=0, i",
        "referer":"https://www.facebook.com/",
        "sec-ch-prefers-color-scheme":"drak",
        "sec-ch-ua":'"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-full-version-list":'"Google Chrome";v="137.0.7151.120", "Chromium";v="137.0.7151.120", "Not/A)Brand";v="24.0.0.0"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-model":"",
        "sec-ch-ua-platform":"Windows",
        "sec-ch-ua-platform-version":"10.0.0",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "upgrade-insecure-requests":"1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        }

    def auto_like(self,cookie_fb,id,type,proxies):
        
        id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
        id_ads = id
        type_id = "1635855486666999"
        if (type == "LOVE"):
            type_id = "1678524932434102"
        elif (type == "CARE"):
            type_id = "613557422527858"
        elif (type == "HAHA"):
            type_id = "115940658764963"
        elif (type == "WOW"):
            type_id = "478547315650144"
        elif (type == "SAD"):
            type_id = "908563459236466"
        elif (type == "ANGRY"):
            type_id = "444813342392137"
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}',headers = self.header_get,proxies=proxies).url

        form = self.httpx.get(url=f'{fake_link}',headers=self.header_get,proxies=proxies).text
        try:
            fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
            jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
            lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
            feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
        except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
        except:
            
            return
        

        data = {
            "av": f"{id_fb}",
            "__user": f"{id_fb}",
            "fb_dtsg": f"{fb_dtsg}",
            "jazoest": f"{jazoest}",
            "lsd": f"{lsd}",
            "doc_id": "29333620026283566",  # Mã doc dùng cho CometUFIFeedbackReactMutation
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "CometUFIFeedbackReactMutation",
            '__dyn': '',
            "variables": json.dumps({
                "input": {
                    "feedback_id": f"{feelback}",
                    "feedback_reaction_id": f"{type_id}",  # reaction type (VD: Like)
                    "feedback_source": "TAHOE",
                    "is_tracking_encrypted": True,
                    "tracking": [],
                    "actor_id": f"{id_fb}",
                    "client_mutation_id": "1"
                },
                "useDefaultActor": False,
                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False
            }),
            "server_timestamps": True
        }

        print("da ban api")
        response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = self.header_post,data=data,proxies=proxies)

    def auto_comment(self,cookie_fb,id,Text, proxies):

        id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
        id_ads = id
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}', headers=self.header_get,proxies=proxies).url

        form = self.httpx.get(url=f'{fake_link}',headers=self.header_get,proxies=proxies).text
        try:
            fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
            jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
            lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
            feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
        except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
        except:
            
            return

        data = {
            "av": f"{id_fb}",
            "__user": f"{id_fb}",
            "fb_dtsg": f"{fb_dtsg}",
            "jazoest": f"{jazoest}",
            "lsd": f"{lsd}",
            "doc_id": "9761804193899543",  # Mã doc dùng cho CometUFIFeedbackReactMutation
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "useCometUFICreateCommentMutation",
            '__dyn': '',
            "variables": json.dumps({
                "feedLocation":"NEWSFEED","feedbackSource":1,"groupID":None,
                "input": {
                    "feedback_id": f"{feelback}",
                    "feedback_source": "TAHOE",
                    "is_tracking_encrypted": True,
                    "tracking": [],
                    "actor_id": f"{id_fb}",
                    "client_mutation_id": "1",
                    "message":{"ranges":[],"text":f"{Text}"}
                },
                "useDefaultActor": False,
                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False
            }),
            "server_timestamps": True
        }
        print("Da ban api")


        response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = self.header_post,data=data,proxies=proxies)
        print(response.text)

    

    def up_load(self,cookie_fb,id,image_path, proxies):
        

        id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
        id_ads = id
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}',headers=self.header_get,proxies=proxies).url

        form = self.httpx.get(url=f'{fake_link}',headers=self.header_get,proxies=proxies).text
        try:
            fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
            jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
            lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
            
        except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
        except:
            
            return
        if "jfif" in image_path or "jpeg" in image_path:
            files = {
    "file": (image_path, open(image_path, "rb"), "image/jpeg")
}       
        elif "png" in image_path: 
            files = {
    "file": (image_path, open(image_path, "rb"), "image/png")
}


        response = self.httpx.post(url=f"https://www.facebook.com/ajax/ufi/upload/?av={id_fb}&profile_id={id_fb}&source=19&target_id={id_fb}&__aaid=0&__user={id_fb}&__a=1&__req=17&__hs=20273.HYP%3Acomet_pkg.2.1...0&dpr=1&__ccg=EXCELLENT&__rev=1024455538&__s=2gcofg%3Azv0wa0%3At7n6nz&__hsi=7523196173020553131&__dyn=7xeUjGU5a5Q1ryaxG4Vp41twWwIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320qa321Rwwwqo462mcwfG12wOx62G5Usw9m1YwBgK7o6C0Mo4G17yovwRwlE-U2exi4UaEW2G1jwUBwJK14xm3y11xfxmu3W3y261eBx_wHwoE2mwLyEbUGdG0HE88cA0z8c84q58jyUaUbGxe6Uak0zU8oC1hxB0qo4e4UO2m3Gfw-KufxamEbbxG1fBG2-2K2G1Rwgo620XEaUcEK&__csr=g5dd4T2y10ztOONIv2v4NAiyQKOTTsZsYBII8tNhiOtYlkQP4ZFEpey4jZcPXHATYkAGtj9UwLAROaACHAVdajujqACaZnAGihfF5iAp2AQiJoOHEzWGgCpeQQiQ9y4qmmmdBhqHBBVeQiFrKWU_B_x3iBy8CrFaXgoyuheiV99rALAy99VmnABG4_BAy42ifx6aKEV6AUjAwJx2Q4U-qFpUDxh7yoByGV8WczUNx69xicCAyUx3bx65UKQm5EKUC8wjopheaxCewzx28yF8C3qeyWwSyUSA11zoSbCyU8o9UC4ES747A9yo6q3-ijxeu7UrUCt1a58pJaawEx2ewTKmez888oG3im0mCl123e3zbqFki0DWwxwDw4Og2kg2Wz4dxq6o3Ea0lJk0NVo30wLwh815oowc20hWrg3JwywbZwk82sw5xo1dk0wk4o8o95DyQdy40yWgcU2oG645pt0trx65oKiESdxe1Xwh8O9fyA0AHw4pw6Nw1vyU0bue07ko4C1JCw17u0FU0Ne00ROoiy8B2Uy320pu3Si0k-E1q8S0wo2Sw3hE080o5G362G1Cw8Gawcy0bTw0VVG583Mg21wIzUux0w8o0hqwhU4C1pg1vrxS0U40eYwKwHgK9gnxe0dJG545-09Lwba0VA038q0Dz02c87O0hC1Wwda08gyU0VUw0R69wahOkye0n65o0Km2W4A&__hsdp=gbA6uw8i0PPE98y2qEO48VfmvlEsAhiCir9QN9cB58912wk4j8qy6tA49KbHnC8giZkzWShu45LByJASPEQiDlc_4MGN28mzFN4rYbkBej0S4130wgjYuwHaOI9EIaF4lJD8l4gFFaRdLP9cGlEt8VlKqkwAJum8gogvgOEF9aow-G_m8jhuUgzUE-icL8v8FApLbBRgKmnLKbKiJi6rSkgl9mz11amiAznmyd2b494HghjgyC98h342FWAzoPgGBO7B253k4F8xLPQkC4Uqp4xgC6C9Uy8pcFkAkAq6A2S9Qm9gV0Hwxg8okxS8Azox9ybml4WFc40Kyi2UEE98gBUWuqmVbJyJ52yByah44awwwFxanqo8UiyV8bQ24FoQF418pbckUij3gQCbxORDacwSG22bp5xbgayDwnUswRuu3OegR0mQq2i1Owgk3m0D8bobU9axW5Uesd0XwgA2a5EcE4HwIg6mcxSQ3Neexoc0xxJ1Ewyljovz49h8Hw4DwmUaoc84afwJzo-322em1rwnU423m1bwKwno2szQ1rG1ca1og6q1Twa23J0xw8y322y0CEuwuE2Bwoo3Ew5ow53wd-78y1ewdUEeEc87K2u0om0G8fU6y0yUkwn8uwlU6aq0I819U8ovw9im0lG4o2PDwj86u0bmwbmU7u0EUsxe09OwxwjU6a1xwoo2xw41w9O0hS1bw2KQ&__hblp=09Bzk1kkR2km4oV1G22VUdUdE6y2W26322u4EgwBwaa2a0hqGU727V8c85Cq1hK1iws8oxCq4U8pUK8wUgKcyUjG7U8U8U5i1Dzoa84i2y1cm2C4ESVK1FwOwyw-wBwYx6E2ExWi1Pg7t0XKq5odUqG22cBm4E2mx-3vFk1czE1fUdo6i3u3S14wUg563W1Cxq2G1ixi1Og9Ujw9q2u2ZaEb81ho12EeE-1kBwpU5e3yu0wpo26wb61nG11wpQ0O8lwdPwwxG0DEa9U26yUuwCz89UuwLwto888ojyElw-wuEowjE12o1Io762m0_E6S321XwDwei9wvqgkgiG361vxGexm1Egd8lw_xi1sxW1nxe1eCwno5a0iuUtx-0B9obE3owQxS4rwaOFWxiawFwpU0Am1Wxm0Jry9VpU98cUeo6C78jwo81ZUpwEwi86a1oy8520qi1lwQwxwgo5-awp9XxGdwywgoG10wu862m0KF82dgsEE&__sjsp=gbA6uw8i0PPE848wCGcx3crmvlEsAhiCJIzAppyakwA4a1gh4oAxRpkAiibHny4hJ4XFaWy45VpolhyczzZc_fPCbAamEAxfiAgOnAgN9qDJpvACJyem1xzo4phPGEuF6xlKXauye5ScgKbIEGqlAwymaB89bAzA3B3UV38iAUWQ78qfxn8vgJ6XODHgK4ohKvl0BjG7oR8R9p9oiihaQ4ki8Kapkcgb988kdH8uk8kdgny66U3iwTQ0ji39wRBUWexah2J5b7a4F44U6lwc10tQMQd80_2DwnU5W0V87a0ke2-16wkv201rA1BwrrzEm306J0hEHw63wmE0Wafg2Ha0tC0d-w18a1nwdUE054i0Eo&__comet_req=15&fb_dtsg={fb_dtsg}&jazoest={jazoest}&lsd={lsd}&__spin_r=1024455538&__spin_b=trunk&__spin_t=1751630607&__crn=comet.fbweb.CometSinglePostDialogRoute",headers = {
    'accept':'*/*',
    "Accept-Encoding": "gzip",
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Cookie': f'{cookie_fb}',
    'Dpr': '1',
    'Pragma': 'no-cache',
    'Priority': 'u=0, i',
    'referer':f'{fake_link}',
    'Sec-CH-Prefers-Color-Scheme': 'dark',
    'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Model': '""',
    'Sec-CH-UA-Platform': '"Windows"',
    'Sec-CH-UA-Platform-Version': '"10.0.0"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'X-Asbd-Id':'359341',
    "X-Fb-Lsd":f"{lsd}",
}
,files=files,proxies=proxies)
        print(response.text)
        data = response.text
        id_image = data.split('fbid=')[1].split('&amp;')[0]
        print(id_image)
        return id_image
    
    def auto_comment_image(self,cookie_fb,id,Text,id_image, proxies):

        id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
        id_ads = id
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}', headers=self.header_get,proxies=proxies).url

        form = self.httpx.get(url=f'{fake_link}',headers=self.header_get,proxies=proxies).text
        try:
            fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
            jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
            lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
            feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
        except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
        except:
            
            return

        data = {
            "av": f"{id_fb}",
            "__user": f"{id_fb}",
            "fb_dtsg": f"{fb_dtsg}",
            "jazoest": f"{jazoest}",
            "lsd": f"{lsd}",
            "doc_id": "9761804193899543",  # Mã doc dùng cho CometUFIFeedbackReactMutation
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "useCometUFICreateCommentMutation",
            '__dyn': '',
            "variables": json.dumps({
                "feedLocation":"NEWSFEED","feedbackSource":1,"groupID":None,
                "input": {
                    "feedback_id": f"{feelback}",
                    "feedback_source": "TAHOE",
                    "is_tracking_encrypted": True,
                    "tracking": [],
                    "actor_id": f"{id_fb}",
                    "client_mutation_id": "1",
                    "message":{"ranges":[],"text":f"{Text}"},
                    "attachments":[{"media":{"id":f"{id_image}"}}],
                },
                "useDefaultActor": False,
                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False
            }),
            "server_timestamps": True
        }
        print("Da ban api")


        response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = self.header_post,data=data,proxies=proxies)
        print(response.text)

id_image = requests_fb().up_load()
requests_fb().auto_comment_image()