""#line:9
import push #line:13
import utools #line:14
import config #line:15
import data #line:16
import api #line:17
import requests #line:18
import random #line:19
import time #line:20
class Bilibili :#line:23
    ""#line:26
    def __init__ (OO0OOO0OO00000O00 )->None :#line:28
        OO0OOO0OO00000O00 .log =''#line:29
        OO0OOO0OO00000O00 .session =requests .Session ()#line:30
    @staticmethod #line:32
    def exchange_cookie (OOO0O0O0OO0O0000O :str ):#line:33
        ""#line:38
        OOO00O00O0O0OO00O =dict ([O00OO0O0O0O0O0O00 .split ("=",1 )for O00OO0O0O0O0O0O00 in OOO0O0O0OO0O0000O .split ("; ")])#line:39
        return OOO00O00O0O0OO00O #line:40
    def __O0OOOO0O00000O00O (O00O0OO0O0000000O ,OOOOO0OO0OOOO00O0 :str )->int :#line:42
        ""#line:47
        O00O000O00OO0O0OO =Bilibili .exchange_cookie (OOOOO0OO0OOOO00O0 )#line:48
        OOOO0O00OOOO000O0 =O00O0OO0O0000000O .session .get (url =api .coin_url ,cookies =O00O000O00OO0O0OO ).json ()#line:49
        O0OO00O0O0O0OO00O =OOOO0O00OOOO000O0 ['code']#line:50
        if O0OO00O0O0O0OO00O ==0 :#line:51
            return 1 #line:53
        return 0 #line:54
    def __OOOO0OO0OO0OOO0O0 (OO0OOO0OOO00OOO00 ,O00OO0OOOO0OO0000 :str )->int :#line:56
        ""#line:62
        OOOO00OOO0O0000OO =OO0OOO0OOO00OOO00 .exchange_cookie (O00OO0OOOO0OO0000 )#line:63
        O00OO0OOO0O0O000O =OO0OOO0OOO00OOO00 .session .get (url =api .coin_url ,headers =data .headers ,cookies =OOOO00OOO0O0000OO ).json ()#line:65
        OO0O000OO00OO000O =O00OO0OOO0O0O000O ['data']['money']#line:66
        if OO0O000OO00OO000O is None :#line:67
            return 0 #line:69
        else :#line:70
            return OO0O000OO00OO000O #line:71
    @staticmethod #line:73
    def get_csrf (OOOOOOOOOOOO0O000 :str )->str :#line:74
        ""#line:79
        O0O00O00O00O0OO0O =Bilibili .exchange_cookie (OOOOOOOOOOOO0O000 )#line:80
        OO000000O0O0OO000 =O0O00O00O00O0OO0O ['bili_jct']#line:81
        return OO000000O0O0OO000 #line:82
    def __OO000OO0O00O0O000 (O00OO0O00O0O0O0O0 ,O0OOOO000000OO0O0 :str )->None :#line:84
        ""#line:89
        O0O00OO0OOO00O0OO =f'{O0OOOO000000OO0O0}</br>'#line:90
        O00OO0O00O0O0O0O0 .log =f'{O00OO0O00O0O0O0O0.log}{O0O00OO0OOO00O0OO}'#line:91
    def __O00O0O0O000O00OOO (O00O00O00000O000O ,O0O000O00OOO000O0 :str )->tuple :#line:93
        ""#line:98
        OO0O0OO0000O0OO0O =Bilibili .exchange_cookie (O0O000O00OOO000O0 )#line:99
        OO0OO0OOO0000000O =O00O00O00000O000O .session .get (url =api .inquire_url ,cookies =OO0O0OO0000O0OO0O ).json ()#line:101
        OO0O0OOOO0OO000OO =OO0OO0OOO0000000O ['data']['login']#line:102
        O0O00O0OOO0000O00 =OO0OO0OOO0000000O ['data']['watch']#line:103
        OOOO000O0O00O0O0O =OO0OO0OOO0000000O ['data']['coins']#line:104
        O0O0000O0OOOO0O0O =OO0OO0OOO0000000O ['data']['share']#line:105
        O0000000000O0OO00 =OO0OO0OOO0000000O ['data']['email']#line:107
        O000O0OO0O000O00O =OO0OO0OOO0000000O ['data']['tel']#line:108
        OOOO0OO0OOO0OO00O =OO0OO0OOO0000000O ['data']['safe_question']#line:109
        O00000OOOO00OOO0O =OO0OO0OOO0000000O ['data']['identify_card']#line:110
        O0OO00O0O00000O00 =[OO0O0OOOO0OO000OO ,O0O00O0OOO0000O00 ,OOOO000O0O00O0O0O ,O0O0000O0OOOO0O0O ]#line:112
        O0O00O0O000OO0OO0 =[O0000000000O0OO00 ,O000O0OO0O000O00O ,OOOO0OO0OOO0OO00O ,O00000OOOO00OOO0O ]#line:113
        return O0OO00O0O00000O00 ,O0O00O0O000OO0OO0 #line:114
    def __OOO0OOO00O0OO000O (O00000O0O0O0O0OOO ,OO0O0OOOO0000OO0O :str )->None :#line:116
        ""#line:121
        OO0OOOO0OOO0OOO00 =Bilibili .exchange_cookie (OO0O0OOOO0000OO0O )#line:122
        OOO00OO000OOOOO00 =O00000O0O0O0O0OOO .session .get (url =api .info_url ,cookies =OO0OOOO0OOO0OOO00 ).json ()#line:123
        OOOO00000O000OO00 =OOO00OO000OOOOO00 ['data']['mid']#line:124
        O0OO0OOO0OOO0O00O =OOO00OO000OOOOO00 ['data']['name']#line:125
        O0O000O00O0O0O0OO =OOO00OO000OOOOO00 ['data']['level']#line:126
        O00O00OOO0OOO0OOO =OOO00OO000OOOOO00 ['data']['level_exp']['current_exp']#line:127
        OO0OO00OO0O00O00O =OOO00OO000OOOOO00 ['data']['level_exp']['next_exp']#line:128
        O0O000OOOO00OOOO0 =OO0OO00OO0O00O00O -O00O00OOO0OOO0OOO #line:129
        OOOOO0000OO0O0O00 =int (O0O000OOOO00OOOO0 /65 )#line:130
        O0O0O0OO0OO000O00 =OOO00OO000OOOOO00 ['data']['coins']#line:131
        O0000OO0O0O0OOOOO =OOO00OO000OOOOO00 ['data']['vip']['status']#line:132
        OOO00OO00O0OO0O00 =OOO00OO000OOOOO00 ['data']['vip']['due_date']#line:133
        OOO00OO00O0OO0O00 =utools .formate_time (OOO00OO00O0OO0O00 )#line:134
        if O0000OO0O0O0OOOOO :#line:135
            O0OOOO0OOOOO00OOO =f"用户{O0OO0OOO0OOO0O00O},uid为{OOOO00000O000OO00}您是大会员,大会员到期时间为{OOO00OO00O0OO0O00},你目前的等级是{O0O000O00O0O0O0OO}级,目前的经验{O00O00OOO0OOO0OOO},离下个等级还差{O0O000OOOO00OOOO0}经验,需要{OOOOO0000OO0O0O00}天剩余硬币还有{O0O0O0OO0OO000O00}个"#line:136
            O00000O0O0O0O0OOO .__OO000OO0O00O0O000 (f"用户名:{O0OO0OOO0OOO0O00O}</br>uid:{OOOO00000O000OO00}</br>VIP:大会员</br>到期时间:{OOO00OO00O0OO0O00}</br>目前的等级:{O0O000O00O0O0O0OO}级</br>目前的经验:{O00O00OOO0OOO0OOO}</br>离下个等级:{O0O000OOOO00OOOO0}经验<br>距升级还差:{OOOOO0000OO0O0O00}天</br>剩余硬币数:{O0O0O0OO0OO000O00}个")#line:138
            utools .formate_print (O0OOOO0OOOOO00OOO )#line:139
        else :#line:140
            O0OOOO0OOOOO00OOO =f"用户{O0OO0OOO0OOO0O00O},uid为{OOOO00000O000OO00}您的大会员已过期,过期时间为{OOO00OO00O0OO0O00},你目前的等级是{O0O000O00O0O0O0OO}级,目前的经验{O00O00OOO0OOO0OOO},离下个等级还差{O0O000OOOO00OOOO0}经验,需要{OOOOO0000OO0O0O00}天,剩余硬币还有{O0O0O0OO0OO000O00}个"#line:141
            O00000O0O0O0O0OOO .__OO000OO0O00O0O000 (f"用户名:{O0OO0OOO0OOO0O00O}</br>uid:{OOOO00000O000OO00}</br>VIP:非大会员</br>过期时间:{OOO00OO00O0OO0O00}</br>目前的等级:{O0O000O00O0O0O0OO}级</br>目前的经验:{O00O00OOO0OOO0OOO}</br>离下个等级:{O0O000OOOO00OOOO0}经验<br>距升级还差:{OOOOO0000OO0O0O00}天</br>剩余硬币数:{O0O0O0OO0OO000O00}个")#line:143
            utools .formate_print (O0OOOO0OOOOO00OOO )#line:144
    def __O0OOO0O0O0O0OOOOO (O0OOOO00000O0OO0O ,OO0OO0O0OOO00O000 )->list :#line:146
        ""#line:150
        OO0000000OO0O0OOO =Bilibili .exchange_cookie (OO0OO0O0OOO00O000 )#line:152
        O0O0O00OOO0OO0O0O =config .UID_LIST #line:153
        O0O00OO00OOOOO0OO =O0OOOO00000O0OO0O .session .get (url =api .get_video_list_url .format (random .choice (O0O0O00OOO0OO0O0O )),cookies =OO0000000OO0O0OOO ).json ()#line:155
        utools .formate_print (O0O00OO00OOOOO0OO )#line:156
        OO00OO0OOO0O00O00 =O0O00OO00OOOOO0OO ['data']['list']['vlist']#line:157
        return OO00OO0OOO0O00O00 #line:158
    def __O000OO0OOO0O00OOO (O000O0OO00OO0O00O ,O0OOOO0OOO0OO0O0O :str ,OOOOOO000OOO0O00O :str )->None :#line:160
        ""#line:166
        OO0OO00OOO0O0O0OO =random .randint (30 ,60 )#line:167
        data .watch_video_data ['bvid']=O0OOOO0OOO0OO0O0O #line:168
        data .watch_video_data ['played_time']=str (OO0OO00OOO0O0O0OO )#line:169
        data .watch_video_data ['csrf']=Bilibili .get_csrf (OOOOOO000OOO0O00O )#line:170
        O0O0OO0O000O0OOOO =Bilibili .exchange_cookie (OOOOOO000OOO0O00O )#line:171
        O000O00O0O0O0OOO0 =O000O0OO00OO0O00O .session .post (url =api .watch_video_url ,data =data .watch_video_data ,cookies =O0O0OO0O000O0OOOO ).json ()#line:173
        O0O0O00OO0000O00O =O000O00O0O0O0OOO0 ['code']#line:174
        if O0O0O00OO0000O00O ==0 :#line:176
            utools .formate_print ('看视频完成')#line:177
        else :#line:178
            utools .formate_print ('看视频失败')#line:179
    def __O00OO00OOO0O00O0O (O00000OO0OO0OOOOO ,OO00OO00OOO00000O :str ,O0O00O00000OOO0O0 :str )->None :#line:181
        ""#line:187
        data .share_video_data ['bvid']=OO00OO00OOO00000O #line:188
        data .share_video_data ['csrf']=Bilibili .get_csrf (O0O00O00000OOO0O0 )#line:189
        OOOOO00O0O0000OO0 =Bilibili .exchange_cookie (O0O00O00000OOO0O0 )#line:190
        OO00OOO00O00OO0O0 =O00000OO0OO0OOOOO .session .post (url =api .share_video_url ,data =data .share_video_data ,cookies =OOOOO00O0O0000OO0 ,headers =data .headers ).json ()#line:192
        O0O0O00O00OOO0O0O =OO00OOO00O00OO0O0 ['code']#line:193
        if O0O0O00O00OOO0O0O ==0 :#line:194
            utools .formate_print ('分享视频成功')#line:195
        else :#line:196
            utools .formate_print ('分享视频失败')#line:197
    def __OOOO00O0OO00O0O0O (O0O0OOOOO00O0O000 ,O0000O0O0OO0OOOO0 :str ,O0OOO0OOOOO0000O0 :str )->int :#line:199
        ""#line:206
        OOO000000OO0OOOO0 =Bilibili .exchange_cookie (O0OOO0OOOOO0000O0 )#line:207
        OO00O00O000O00O0O =data .insert_coin_data #line:208
        O0OO00000000O0OOO =data .insert_coin_headers #line:209
        OO00O00O000O00O0O ['aid']=O0000O0O0OO0OOOO0 #line:210
        OO00O00O000O00O0O ['csrf']=Bilibili .get_csrf (O0OOO0OOOOO0000O0 )#line:211
        O0OO00000000O0OOO ['cookie']=O0OOO0OOOOO0000O0 #line:212
        O0O0O00000000OO00 =O0O0OOOOO00O0O000 .session .post (url =api .insert_coins_url ,headers =data .insert_coin_headers ,data =OO00O00O000O00O0O ,cookies =OOO000000OO0OOOO0 ).json ()#line:215
        O0O00O0000OOOOOOO =O0O0O00000000OO00 ['data']['like']#line:216
        if O0O00O0000OOOOOOO :#line:217
            utools .formate_print ('投币成功')#line:218
            return 1 #line:219
        else :#line:220
            utools .formate_print ('投币失败')#line:221
            return 0 #line:222
    @staticmethod #line:224
    def random_video_para (OO000OO0OO00O0O0O :list )->tuple :#line:225
        ""#line:230
        OOOO000O0O0000OOO =random .randint (0 ,len (OO000OO0OO00O0O0O )-1 )#line:231
        OOO0O0O00OO0O0O0O =OO000OO0OO00O0O0O [OOOO000O0O0000OOO ]['bvid']#line:232
        OOO0O00O0OO00000O =OO000OO0OO00O0O0O [OOOO000O0O0000OOO ]['title']#line:233
        O0OO0OO0000O000O0 =OO000OO0OO00O0O0O [OOOO000O0O0000OOO ]['author']#line:234
        OO00O0000O0OOOOOO =OO000OO0OO00O0O0O [OOOO000O0O0000OOO ]['aid']#line:235
        return OOO0O0O00OO0O0O0O ,OOO0O00O0OO00000O ,O0OO0OO0000O000O0 ,OO00O0000O0OOOOOO #line:236
    def __OOOOO00OO0OOO0000 (OOO00OO00OO00OOOO ,O00OO0O0000O0O000 :str )->int :#line:238
        ""#line:243
        O0O0O0O000OOO0O00 =OOO00OO00OO00OOOO .__O0OOO0O0O0O0OOOOO (O00OO0O0000O0O000 )#line:244
        OO0O00O0O0OOOOO00 ,O000OOO0O0OOOOOOO ,O0O00O0O0O0OOO0OO ,OOOOO00000OOOOOOO =Bilibili .random_video_para (O0O0O0O000OOO0O00 )#line:246
        utools .formate_print (f'开始向{O0O00O0O0O0OOO0OO}的视频{O000OOO0O0OOOOOOO}投币……')#line:247
        OO0OO0OO0OO000OOO =OOO00OO00OO00OOOO .__OOOO00O0OO00O0O0O (OOOOO00000OOOOOOO ,O00OO0O0000O0O000 )#line:248
        return OO0OO0OO0OO000OOO #line:249
    def __OO0O000000OO0OO00 (OOO0OOO0OO00OO000 ,O0O00OOO0O000OOO0 :str )->None :#line:251
        OOOO0000OOOO00O00 =OOO0OOO0OO00OO000 .session .get (url =api .live_sign_url ,cookies =Bilibili .exchange_cookie (O0O00OOO0O000OOO0 )).json ()#line:252
        if OOOO0000OOOO00O00 ['code']==0 :#line:253
            OO0OOO00O000OO0OO =OOOO0000OOOO00O00 ['data']['text']#line:254
            O0O0OOOOOOOO0OO00 =OOOO0000OOOO00O00 ['data']['hadSignDays']#line:255
            OOO0OOO0OO00OO000 .__OO000OO0O00O0O000 ('直播签到:签到成功,签到天数为{}'.format (O0O0OOOOOOOO0OO00 ))#line:256
            utools .formate_print (f'签到奖励:{OO0OOO00O000OO0OO},连续签到{O0O0OOOOOOOO0OO00}天')#line:257
            OOO0OOO0OO00OO000 .__OO000OO0O00O0O000 (f'签到奖励:{OO0OOO00O000OO0OO},连续签到{O0O0OOOOOOOO0OO00}天')#line:258
        else :#line:259
            utools .formate_print ('直播签到:当天已签到~')#line:260
            OOO0OOO0OO00OO000 .__OO000OO0O00O0O000 ('直播签到:当天已签到')#line:261
    def __O0O00O0OOO00O0O0O (OO00OO0O0000OO000 ,O0O0OOOO0OO0OOO00 :str )->bool :#line:263
        ""#line:268
        O00O0O00OOOOO0OO0 =OO00OO0O0000OO000 .session .get (url =api .live_info_url ,cookies =Bilibili .exchange_cookie (O0O0OOOO0OO0OOO00 )).json ()#line:269
        OO00OO0O0000OO000 .__OO000OO0O00O0O000 (f'银瓜子数量:{O00O0O00OOOOO0OO0["data"]["silver"]}')#line:270
        utools .formate_print (f'银瓜子数量:{O00O0O00OOOOO0OO0["data"]["silver"]}')#line:271
        if O00O0O00OOOOO0OO0 ['data']['silver']>700 :#line:272
            return True #line:273
        return False #line:274
    def __O0OO00O000O0O0000 (O000OOO000000OOOO ,O0OOOOOO00000OO00 :str )->None :#line:276
        OO0OOOO0OO000OO00 =data .silver2coin_data #line:277
        OO0OOOO0OO000OO00 ['csrf']=Bilibili .get_csrf (O0OOOOOO00000OO00 )#line:278
        OO0OOOO0OO000OO00 ['csrf_token']=Bilibili .get_csrf (O0OOOOOO00000OO00 )#line:279
        O000000O0OO0OOO00 =O000OOO000000OOOO .session .post (url =api .silver2coin_url ,cookies =Bilibili .exchange_cookie (O0OOOOOO00000OO00 ),data =OO0OOOO0OO000OO00 ).json ()#line:280
        if O000000O0OO0OOO00 ['code']==0 :#line:281
            OOOO0OO0O0OOOO00O =O000000O0OO0OOO00 ['data']['silver']#line:282
            utools .formate_print ('银瓜子兑换:成功!')#line:283
            utools .formate_print (f'银瓜子剩余:{OOOO0OO0O0OOOO00O}个')#line:284
            O000OOO000000OOOO .__OO000OO0O00O0O000 ('银瓜子兑换:成功!')#line:285
            O000OOO000000OOOO .__OO000OO0O00O0O000 (f'银瓜子剩余:{OOOO0OO0O0OOOO00O}个')#line:286
        else :#line:287
            utools .formate_print ('银瓜子兑换:当天已兑换!')#line:288
            O000OOO000000OOOO .__OO000OO0O00O0O000 ('银瓜子兑换:当天已兑换!')#line:289
    def __OO0O0OO0O000O0OO0 (O0OOO000O00O000OO ,O000000OO0OO0O000 :str )->None :#line:291
        ""#line:296
        OO0OOO0O0O0O0O0OO =O0OOO000O00O000OO .__O0OOOO0O00000O00O (O000000OO0OO0O000 )#line:297
        if OO0OOO0O0O0O0O0OO :#line:298
            OOO00000O0O000OOO =O0OOO000O00O000OO .__OOOO0OO0OO0OOO0O0 (O000000OO0OO0O000 )#line:299
            utools .formate_print ('cookie有效即将开始查询任务……')#line:300
            utools .formate_print ('=========以下是任务信息=========')#line:301
            O0OOO000O00O000OO .__OO000OO0O00O0O000 ('=========以下是任务信息=========')#line:302
            O0O0OO0O00O0OO0OO =O0OOO000O00O000OO .__O00O0O0O000O00OOO (O000000OO0OO0O000 )#line:304
            O00O00OOO0O00OO0O ,OOO0O0000000OO000 =O0O0OO0O00O0OO0OO #line:305
            for O0O000O00000OO0OO ,OOOO0OO000O0OO0OO in enumerate (O00O00OOO0O00OO0O ):#line:308
                if O0O000O00000OO0OO ==0 :#line:309
                    utools .formate_print ('登录任务已完成')if OOOO0OO000O0OO0OO else utools .formate_print ('登录任务未完成')#line:311
                    O0OOO000O00O000OO .__OO000OO0O00O0O000 ('每日登录:已完成~获得5点经验值')#line:312
                elif O0O000O00000OO0OO ==1 :#line:313
                    if OOOO0OO000O0OO0OO :#line:314
                        utools .formate_print ('观看视频任务已完成')#line:315
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('观看视频:已完成~获得5点经验值')#line:316
                    else :#line:317
                        utools .formate_print ('观看视频任务未完成,即将开始观看视频任务……')#line:318
                        OO00O00OO0O0OOO00 =O0OOO000O00O000OO .__O0OOO0O0O0O0OOOOO (O000000OO0OO0O000 )#line:319
                        O0O0O0O0OOO00O0OO ,O00O0O000OOO0OO0O ,OO0OO00OOO0000OO0 ,OO0O0O0O0O000OOO0 =Bilibili .random_video_para (OO00O00OO0O0OOO00 )#line:321
                        utools .formate_print (f'开始观看作者{OO0OO00OOO0000OO0}的视频{O00O0O000OOO0OO0O}……')#line:322
                        O0OOO000O00O000OO .__O000OO0OOO0O00OOO (O0O0O0O0OOO00O0OO ,O000000OO0OO0O000 )#line:323
                        utools .formate_print ('观看视频任务已完成，即将开始下一个任务……')#line:324
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('观看视频:完成~获得5点经验值')#line:325
                elif O0O000O00000OO0OO ==2 :#line:326
                    if config .COIN_OR_NOT and OOO00000O0O000OOO >=5 :#line:327
                        if OOOO0OO000O0OO0OO ==50 :#line:330
                            utools .formate_print ('投币任务已完成')#line:331
                            O0OOO000O00O000OO .__OO000OO0O00O0O000 ('每日投币:已完成~获得50点经验值')#line:332
                        else :#line:333
                            utools .formate_print ('投币任务未完成,即将开始投币任务')#line:334
                            OOO0OOOO00O000000 =int ((50 -OOOO0OO000O0OO0OO )/10 )#line:335
                            for O0OOOOOO0OOO00000 in range (0 ,OOO0OOOO00O000000 ):#line:336
                                OO00OOO0O0O0OOO0O =0 #line:337
                                if config .STRICT_MODE :#line:338
                                    while 1 :#line:339
                                        OO0O0OO0O0O0O0000 =O0OOO000O00O000OO .__OOOOO00OO0OOO0000 (O000000OO0OO0O000 )#line:340
                                        OO00OOO0O0O0OOO0O +=1 #line:341
                                        if OO0O0OO0O0O0O0000 or OO00OOO0O0O0OOO0O ==5 :#line:342
                                            break #line:345
                                        time .sleep (2 )#line:346
                                else :#line:347
                                    O0OOO000O00O000OO .__OOOOO00OO0OOO0000 (O000000OO0OO0O000 )#line:348
                                    time .sleep (2 )#line:349
                                time .sleep (1 )#line:350
                            utools .formate_print ('投币任务已完成，即将开始下一个任务……')#line:351
                            O0OOO000O00O000OO .__OO000OO0O00O0O000 ('每日投币:完成~获得50点经验值')#line:352
                    else :#line:353
                        utools .formate_print ('投币任务已跳过')#line:354
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('每日投币:跳过~')#line:355
                else :#line:356
                    if OOOO0OO000O0OO0OO :#line:357
                        utools .formate_print ('分享任务已完成')#line:358
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('每日分享:已完成~获得5点经验值')#line:359
                    else :#line:360
                        utools .formate_print ('分享任务未完成,即将开始分享任务……')#line:361
                        OO00O00OO0O0OOO00 =O0OOO000O00O000OO .__O0OOO0O0O0O0OOOOO (O000000OO0OO0O000 )#line:362
                        O0O0O0O0OOO00O0OO ,O00O0O000OOO0OO0O ,OO0OO00OOO0000OO0 ,OO0O0O0O0O000OOO0 =Bilibili .random_video_para (OO00O00OO0O0OOO00 )#line:364
                        utools .formate_print (f'开始分享{OO0OO00OOO0000OO0}的视频{O00O0O000OOO0OO0O}……')#line:365
                        O0OOO000O00O000OO .__O00OO00OOO0O00O0O (O0O0O0O0OOO00O0OO ,O000000OO0OO0O000 )#line:366
                        utools .formate_print ('分享任务已完成,日常任务已全部完成!即将查询额外任务……')#line:367
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('每日分享:完成~获得5点经验值')#line:368
                        time .sleep (1 )#line:369
            utools .formate_print ('==========以下是额外任务==============')#line:370
            O0OOO000O00O000OO .__OO000OO0O00O0O000 ('=========以下是额外任务=========')#line:371
            for O0O000O00000OO0OO ,OOOO0OO000O0OO0OO in enumerate (OOO0O0000000OO000 ):#line:373
                if O0O000O00000OO0OO ==0 :#line:374
                    if OOOO0OO000O0OO0OO :#line:375
                        utools .formate_print ('绑定邮箱任务已完成')#line:376
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('绑定邮箱:已完成')#line:377
                    else :#line:378
                        utools .formate_print ('绑定邮箱任务未完成,完成可以获得20点经验值~')#line:379
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('绑定邮箱:未完成~完成可获得20点经验')#line:380
                elif O0O000O00000OO0OO ==1 :#line:381
                    if OOOO0OO000O0OO0OO :#line:382
                        utools .formate_print ('绑定手机任务已完成')#line:383
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('绑定手机:已完成')#line:384
                    else :#line:385
                        utools .formate_print ('绑定手机任务未完成,完成可以获得100点经验值~')#line:386
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('绑定手机:未完成~完成可获得20点经验')#line:387
                elif O0O000O00000OO0OO ==2 :#line:388
                    if OOOO0OO000O0OO0OO :#line:389
                        utools .formate_print ('设置密保任务已完成')#line:390
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('密保任务:已完成')#line:391
                    else :#line:392
                        utools .formate_print ('设置密保任务未完成,完成可以获得30点经验值~')#line:393
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('密保任务:未完成~完成可获得30点经验')#line:394
                else :#line:395
                    if OOOO0OO000O0OO0OO :#line:396
                        utools .formate_print ('实名认证任务已完成')#line:397
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('实名认证:已完成')#line:398
                    else :#line:399
                        utools .formate_print ('实名认证任务未完成,完成可以获得50点经验值~')#line:400
                        O0OOO000O00O000OO .__OO000OO0O00O0O000 ('实名认证:未完成~完成可获得50点经验')#line:401
            utools .formate_print ('==========以下是直播任务==============')#line:402
            O0OOO000O00O000OO .__OO000OO0O00O0O000 ('=========以下是直播任务=========')#line:403
            O0OOO000O00O000OO .__OO0O000000OO0OO00 (O000000OO0OO0O000 )#line:404
            if config .SILVER2COIN_OR_NOT and O0OOO000O00O000OO .__O0O00O0OOO00O0O0O (O000000OO0OO0O000 ):#line:405
                O0OOO000O00O000OO .__O0OO00O000O0O0000 (O000000OO0OO0O000 )#line:407
            else :#line:408
                O0OOO000O00O000OO .__OO000OO0O00O0O000 ('银瓜子转换币:跳过~')#line:409
                utools .formate_print ('银瓜子兑换:跳过~')#line:410
            O0OOO000O00O000OO .__OO000OO0O00O0O000 ('=========以下是个人信息=========')#line:411
            utools .formate_print ('=========以下是个人信息=========')#line:412
            O0OOO000O00O000OO .__OOO0OOO00O0OO000O (O000000OO0OO0O000 )#line:413
        else :#line:414
            utools .formate_print ('cookie已失效,任务停止,请更换新的cookie!')#line:415
            O0OOO000O00O000OO .__OO000OO0O00O0O000 ('cookie已失效,任务停止,请更换新的cookie!')#line:416
        utools .formate_print ('==========分割线==============')#line:417
    def go (OOOO0O00O0O0O0O0O )->None :#line:419
        ""#line:423
        utools .formate_print (f'成功添加{len(config.COOKIE_LIST)}个cookie,开始任务……')#line:424
        for OOO0OO0O0OOOOOOOO ,O0O00O0O0OO00000O in enumerate (config .COOKIE_LIST ):#line:425
            OOOO0O00O0O0O0O0O .__OO000OO0O00O0O000 (f'=========这是第{OOO0OO0O0OOOOOOOO+1}个账号=========')#line:426
            utools .formate_print (f'正在签到第{OOO0OO0O0OOOOOOOO+1}个账号……')#line:427
            OOOO0O00O0O0O0O0O .__OO0O0OO0O000O0OO0 (O0O00O0O0OO00000O )#line:428
            time .sleep (1 )#line:429
        if config .PUSH_OR_NOT :#line:430
            push .pushplus (config .TOKEN ,OOOO0O00O0O0O0O0O .log )#line:431
