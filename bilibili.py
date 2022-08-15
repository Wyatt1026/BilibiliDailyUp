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
    def __init__ (O0OO0OO00000OO000 )->None :#line:28
        O0OO0OO00000OO000 .log =''#line:29
        O0OO0OO00000OO000 .session =requests .Session ()#line:30
    @staticmethod #line:32
    def exchange_cookie (OOO00OOO00O0O00O0 :str ):#line:33
        ""#line:38
        OOO0O0OO000OOOOOO =dict ([O0OOOO000O00O00O0 .split ("=",1 )for O0OOOO000O00O00O0 in OOO00OOO00O0O00O0 .split ("; ")])#line:39
        return OOO0O0OO000OOOOOO #line:40
    def __O0O0OO00O00O0OO00 (O0OOOO00O000OO000 ,O0O0OO0O0000O0OOO :str )->int :#line:42
        ""#line:47
        OO000OOO00OO0O0OO =Bilibili .exchange_cookie (O0O0OO0O0000O0OOO )#line:48
        OOOO00OO00O0O00OO =O0OOOO00O000OO000 .session .get (url =api .coin_url ,cookies =OO000OOO00OO0O0OO ).json ()#line:49
        O0OOO0O0O0OOOOOOO =OOOO00OO00O0O00OO ['code']#line:50
        if O0OOO0O0O0OOOOOOO ==0 :#line:51
            return 1 #line:53
        return 0 #line:54
    def __O0O0000000O0O0O0O (O0OO00O0OO0O00000 ,O000O0OO00OO000O0 :str )->int :#line:56
        ""#line:62
        OOOOO00O0O00O0O00 =O0OO00O0OO0O00000 .exchange_cookie (O000O0OO00OO000O0 )#line:63
        OO00O0O000OOOO000 =O0OO00O0OO0O00000 .session .get (url =api .coin_url ,headers =data .headers ,cookies =OOOOO00O0O00O0O00 ).json ()#line:65
        OO0O00O0O0O0O0O0O =OO00O0O000OOOO000 ['data']['money']#line:66
        if OO0O00O0O0O0O0O0O is None :#line:67
            return 0 #line:69
        else :#line:70
            return OO0O00O0O0O0O0O0O #line:71
    @staticmethod #line:73
    def get_csrf (O0OO00000OO00O000 :str )->str :#line:74
        ""#line:79
        O0O0OO00O0OO00O00 =Bilibili .exchange_cookie (O0OO00000OO00O000 )#line:80
        OO0OOOO0O00O00OO0 =O0O0OO00O0OO00O00 ['bili_jct']#line:81
        return OO0OOOO0O00O00OO0 #line:82
    def __OO0OOOOO000O000O0 (OOOOO0OO0OOOOO0O0 ,O00000O00O000O0O0 :str )->None :#line:84
        ""#line:89
        OO000000000OOOO0O =f'{O00000O00O000O0O0}</br>'#line:90
        OOOOO0OO0OOOOO0O0 .log =f'{OOOOO0OO0OOOOO0O0.log}{OO000000000OOOO0O}'#line:91
    def __O00O0OOO00O0O0OO0 (O0O0O0O0O000000O0 ,O00000O0O0OOO0O00 :str )->tuple :#line:93
        ""#line:98
        OO00OOO00OOO0O00O =Bilibili .exchange_cookie (O00000O0O0OOO0O00 )#line:99
        OOOO0O0O00O0O00O0 =O0O0O0O0O000000O0 .session .get (url =api .inquire_url ,cookies =OO00OOO00OOO0O00O ).json ()#line:101
        O000OOO000OOOO0O0 =OOOO0O0O00O0O00O0 ['data']['login']#line:102
        O0O00O0O0O0000O00 =OOOO0O0O00O0O00O0 ['data']['watch']#line:103
        O00000OO0O0O000O0 =OOOO0O0O00O0O00O0 ['data']['coins']#line:104
        O0000OOOO0O0O0OO0 =OOOO0O0O00O0O00O0 ['data']['share']#line:105
        O0OO0000OOO000O0O =OOOO0O0O00O0O00O0 ['data']['email']#line:107
        OO00OOOOO00OO0000 =OOOO0O0O00O0O00O0 ['data']['tel']#line:108
        O0OO0O00OOO000O00 =OOOO0O0O00O0O00O0 ['data']['safe_question']#line:109
        O0OOOOOOO0OOOO00O =OOOO0O0O00O0O00O0 ['data']['identify_card']#line:110
        O0OO0O0O0O0OO00OO =[O000OOO000OOOO0O0 ,O0O00O0O0O0000O00 ,O00000OO0O0O000O0 ,O0000OOOO0O0O0OO0 ]#line:112
        OOO0O0000OOOO00O0 =[O0OO0000OOO000O0O ,OO00OOOOO00OO0000 ,O0OO0O00OOO000O00 ,O0OOOOOOO0OOOO00O ]#line:113
        return O0OO0O0O0O0OO00OO ,OOO0O0000OOOO00O0 #line:114
    def __OOO0OO00O00O0O000 (O0OOOO00OOO0O000O ,O0O0O00OOO0OO0OOO :str )->None :#line:116
        ""#line:121
        OO0O00000O0O00O00 =Bilibili .exchange_cookie (O0O0O00OOO0OO0OOO )#line:122
        OOO0O000OO000O000 =O0OOOO00OOO0O000O .session .get (url =api .info_url ,cookies =OO0O00000O0O00O00 ).json ()#line:123
        O0O0O00O000OO0O00 =OOO0O000OO000O000 ['data']['mid']#line:124
        OO00OOO000OO00OOO =OOO0O000OO000O000 ['data']['name']#line:125
        OO00O0000000O000O =OOO0O000OO000O000 ['data']['level']#line:126
        O000OOOO0OOOO000O =OOO0O000OO000O000 ['data']['level_exp']['current_exp']#line:127
        O0O0O00000O0O00OO =OOO0O000OO000O000 ['data']['level_exp']['next_exp']#line:128
        O0OOOOOO0OO0OOO00 =O0O0O00000O0O00OO -O000OOOO0OOOO000O #line:129
        OO000O0O00000O000 =int (O0OOOOOO0OO0OOO00 /65 )#line:130
        O0O00OOO000O000O0 =OOO0O000OO000O000 ['data']['coins']#line:131
        O0000O0O0OOOOOOOO =OOO0O000OO000O000 ['data']['vip']['status']#line:132
        O000OO0OO0O00O000 =OOO0O000OO000O000 ['data']['vip']['due_date']#line:133
        O000OO0OO0O00O000 =utools .formate_time (O000OO0OO0O00O000 )#line:134
        if O0000O0O0OOOOOOOO :#line:135
            O00O000O000000OO0 =f"用户{OO00OOO000OO00OOO},uid为{O0O0O00O000OO0O00}您是大会员,大会员到期时间为{O000OO0OO0O00O000},你目前的等级是{OO00O0000000O000O}级,目前的经验{O000OOOO0OOOO000O},离下个等级还差{O0OOOOOO0OO0OOO00}经验,需要{OO000O0O00000O000}天剩余硬币还有{O0O00OOO000O000O0}个"#line:136
            O0OOOO00OOO0O000O .__OO0OOOOO000O000O0 (f"用户名:{OO00OOO000OO00OOO}</br>uid:{O0O0O00O000OO0O00}</br>VIP:大会员</br>到期时间:{O000OO0OO0O00O000}</br>目前的等级:{OO00O0000000O000O}级</br>目前的经验:{O000OOOO0OOOO000O}</br>离下个等级:{O0OOOOOO0OO0OOO00}经验<br>距升级还差:{OO000O0O00000O000}天</br>剩余硬币数:{O0O00OOO000O000O0}个")#line:138
            utools .formate_print (O00O000O000000OO0 )#line:139
        else :#line:140
            O00O000O000000OO0 =f"用户{OO00OOO000OO00OOO},uid为{O0O0O00O000OO0O00}您的大会员已过期,过期时间为{O000OO0OO0O00O000},你目前的等级是{OO00O0000000O000O}级,目前的经验{O000OOOO0OOOO000O},离下个等级还差{O0OOOOOO0OO0OOO00}经验,需要{OO000O0O00000O000}天,剩余硬币还有{O0O00OOO000O000O0}个"#line:141
            O0OOOO00OOO0O000O .__OO0OOOOO000O000O0 (f"用户名:{OO00OOO000OO00OOO}</br>uid:{O0O0O00O000OO0O00}</br>VIP:非大会员</br>过期时间:{O000OO0OO0O00O000}</br>目前的等级:{OO00O0000000O000O}级</br>目前的经验:{O000OOOO0OOOO000O}</br>离下个等级:{O0OOOOOO0OO0OOO00}经验<br>距升级还差:{OO000O0O00000O000}天</br>剩余硬币数:{O0O00OOO000O000O0}个")#line:143
            utools .formate_print (O00O000O000000OO0 )#line:144
    def __O0OOO0OO00O00OO0O (O00O00OOO0O0OOOO0 )->list :#line:146
        ""#line:150
        O00O0OO0O00O0OO0O =config .UID_LIST #line:152
        OO0O00O00OOOO0O00 =O00O00OOO0O0OOOO0 .session .get (url =api .get_video_list_url .format (random .choice (O00O0OO0O00O0OO0O ))).json ()#line:154
        O0O000OO0000OOOOO =OO0O00O00OOOO0O00 ['data']['list']['vlist']#line:155
        return O0O000OO0000OOOOO #line:156
    def __O000OOOOO00O00O00 (OOOO00O00OO0OOOO0 ,O0O0OOOO000O0OO0O :str ,OOO0OO0OOO0OO00O0 :str )->None :#line:158
        ""#line:164
        OO00OOOO000O00OOO =random .randint (30 ,60 )#line:165
        data .watch_video_data ['bvid']=O0O0OOOO000O0OO0O #line:166
        data .watch_video_data ['played_time']=str (OO00OOOO000O00OOO )#line:167
        data .watch_video_data ['csrf']=Bilibili .get_csrf (OOO0OO0OOO0OO00O0 )#line:168
        O0OOO00O00O00OO0O =Bilibili .exchange_cookie (OOO0OO0OOO0OO00O0 )#line:169
        O00O000OO00O00O0O =OOOO00O00OO0OOOO0 .session .post (url =api .watch_video_url ,data =data .watch_video_data ,cookies =O0OOO00O00O00OO0O ).json ()#line:171
        O0OOO0OOOOOOO0OO0 =O00O000OO00O00O0O ['code']#line:172
        if O0OOO0OOOOOOO0OO0 ==0 :#line:174
            utools .formate_print ('看视频完成')#line:175
        else :#line:176
            utools .formate_print ('看视频失败')#line:177
    def __O0OOO0O000O0O000O (O00O0OO00O0000O0O ,OO000OO000000O000 :str ,O00OOO0O0OO000000 :str )->None :#line:179
        ""#line:185
        data .share_video_data ['bvid']=OO000OO000000O000 #line:186
        data .share_video_data ['csrf']=Bilibili .get_csrf (O00OOO0O0OO000000 )#line:187
        O00O0OO00O000O0O0 =Bilibili .exchange_cookie (O00OOO0O0OO000000 )#line:188
        O00OOOOOOOOO0OOO0 =O00O0OO00O0000O0O .session .post (url =api .share_video_url ,data =data .share_video_data ,cookies =O00O0OO00O000O0O0 ,headers =data .headers ).json ()#line:190
        OO00000OO00000O0O =O00OOOOOOOOO0OOO0 ['code']#line:191
        if OO00000OO00000O0O ==0 :#line:192
            utools .formate_print ('分享视频成功')#line:193
        else :#line:194
            utools .formate_print ('分享视频失败')#line:195
    def __OOO0O00OOOO0OOO0O (OO0000O0OO0O0OO0O ,O0O0O00OOO0OOO00O :str ,OO00OOOOO0OO00O0O :str )->int :#line:197
        ""#line:204
        O000O0O0OO0O0O0OO =Bilibili .exchange_cookie (OO00OOOOO0OO00O0O )#line:205
        OO0OOO0OO00000000 =data .insert_coin_data #line:206
        O000OOOO0000O0O00 =data .insert_coin_headers #line:207
        OO0OOO0OO00000000 ['aid']=O0O0O00OOO0OOO00O #line:208
        OO0OOO0OO00000000 ['csrf']=Bilibili .get_csrf (OO00OOOOO0OO00O0O )#line:209
        O000OOOO0000O0O00 ['cookie']=OO00OOOOO0OO00O0O #line:210
        O0OOO0O0000000O00 =OO0000O0OO0O0OO0O .session .post (url =api .insert_coins_url ,headers =data .insert_coin_headers ,data =OO0OOO0OO00000000 ,cookies =O000O0O0OO0O0O0OO ).json ()#line:213
        OO000000O0O00OOOO =O0OOO0O0000000O00 ['data']['like']#line:214
        if OO000000O0O00OOOO :#line:215
            utools .formate_print ('投币成功')#line:216
            return 1 #line:217
        else :#line:218
            utools .formate_print ('投币失败')#line:219
            return 0 #line:220
    @staticmethod #line:222
    def random_video_para (OOO0OOO0OOO000OOO :list )->tuple :#line:223
        ""#line:228
        OOOO0OO0O0OO00O0O =random .randint (0 ,len (OOO0OOO0OOO000OOO )-1 )#line:229
        O0OO0OO00O0O0OO00 =OOO0OOO0OOO000OOO [OOOO0OO0O0OO00O0O ]['bvid']#line:230
        O0000O0000O00O000 =OOO0OOO0OOO000OOO [OOOO0OO0O0OO00O0O ]['title']#line:231
        O0O0O000OOOO0O00O =OOO0OOO0OOO000OOO [OOOO0OO0O0OO00O0O ]['author']#line:232
        O0OOOOOOOO00O000O =OOO0OOO0OOO000OOO [OOOO0OO0O0OO00O0O ]['aid']#line:233
        return O0OO0OO00O0O0OO00 ,O0000O0000O00O000 ,O0O0O000OOOO0O00O ,O0OOOOOOOO00O000O #line:234
    def __O00O0000OO0000000 (OOOO0OOOO00000O00 ,O0O00000000O0O00O :str )->int :#line:236
        ""#line:241
        OO000O0O0OOOOOO00 =OOOO0OOOO00000O00 .__O0OOO0OO00O00OO0O ()#line:242
        O00000OO000000O0O ,O0OO0OOOOOOOOOO00 ,O000OO000OO0000OO ,O00000000000O0OO0 =Bilibili .random_video_para (OO000O0O0OOOOOO00 )#line:244
        utools .formate_print (f'开始向{O000OO000OO0000OO}的视频{O0OO0OOOOOOOOOO00}投币……')#line:245
        OOO0OOO00OOO0O0O0 =OOOO0OOOO00000O00 .__OOO0O00OOOO0OOO0O (O00000000000O0OO0 ,O0O00000000O0O00O )#line:246
        return OOO0OOO00OOO0O0O0 #line:247
    def __OOO0O0000000OO00O (OOOOO000OO000O00O ,OOO0OOOOO0O0O0OOO :str )->None :#line:249
        O000O0O00OOOOOO0O =OOOOO000OO000O00O .session .get (url =api .live_sign_url ,cookies =Bilibili .exchange_cookie (OOO0OOOOO0O0O0OOO )).json ()#line:250
        if O000O0O00OOOOOO0O ['code']==0 :#line:251
            OO00O00OO00O00O0O =O000O0O00OOOOOO0O ['data']['text']#line:252
            OOO00O0O0OOOOOO00 =O000O0O00OOOOOO0O ['data']['hadSignDays']#line:253
            OOOOO000OO000O00O .__OO0OOOOO000O000O0 ('直播签到:签到成功,签到天数为{}'.format (OOO00O0O0OOOOOO00 ))#line:254
            utools .formate_print (f'签到奖励:{OO00O00OO00O00O0O},连续签到{OOO00O0O0OOOOOO00}天')#line:255
            OOOOO000OO000O00O .__OO0OOOOO000O000O0 (f'签到奖励:{OO00O00OO00O00O0O},连续签到{OOO00O0O0OOOOOO00}天')#line:256
        else :#line:257
            utools .formate_print ('直播签到:当天已签到~')#line:258
            OOOOO000OO000O00O .__OO0OOOOO000O000O0 ('直播签到:当天已签到')#line:259
    def __O0OOOOO0OO0000OO0 (O000O0OO0OOOOOO0O ,OO0OO0OOO00O0OO0O :str )->bool :#line:261
        ""#line:266
        O00O0O0O0O00O0O00 =O000O0OO0OOOOOO0O .session .get (url =api .live_info_url ,cookies =Bilibili .exchange_cookie (OO0OO0OOO00O0OO0O )).json ()#line:267
        O000O0OO0OOOOOO0O .__OO0OOOOO000O000O0 (f'银瓜子数量:{O00O0O0O0O00O0O00["data"]["silver"]}')#line:268
        utools .formate_print (f'银瓜子数量:{O00O0O0O0O00O0O00["data"]["silver"]}')#line:269
        if O00O0O0O0O00O0O00 ['data']['silver']>700 :#line:270
            return True #line:271
        return False #line:272
    def __O00000OOOOOOOOOOO (OO0OO0O00OOOOO00O ,OOOO0O00OO00OOO00 :str )->None :#line:274
        O00OOO0O00OOOO0O0 =data .silver2coin_data #line:275
        O00OOO0O00OOOO0O0 ['csrf']=Bilibili .get_csrf (OOOO0O00OO00OOO00 )#line:276
        O00OOO0O00OOOO0O0 ['csrf_token']=Bilibili .get_csrf (OOOO0O00OO00OOO00 )#line:277
        O0OOO00OOOOO0O000 =OO0OO0O00OOOOO00O .session .post (url =api .silver2coin_url ,cookies =Bilibili .exchange_cookie (OOOO0O00OO00OOO00 ),data =O00OOO0O00OOOO0O0 ).json ()#line:278
        if O0OOO00OOOOO0O000 ['code']==0 :#line:279
            OO000OO0OO0O0000O =O0OOO00OOOOO0O000 ['data']['silver']#line:280
            utools .formate_print ('银瓜子兑换:成功!')#line:281
            utools .formate_print (f'银瓜子剩余:{OO000OO0OO0O0000O}个')#line:282
            OO0OO0O00OOOOO00O .__OO0OOOOO000O000O0 ('银瓜子兑换:成功!')#line:283
            OO0OO0O00OOOOO00O .__OO0OOOOO000O000O0 (f'银瓜子剩余:{OO000OO0OO0O0000O}个')#line:284
        else :#line:285
            utools .formate_print ('银瓜子兑换:当天已兑换!')#line:286
            OO0OO0O00OOOOO00O .__OO0OOOOO000O000O0 ('银瓜子兑换:当天已兑换!')#line:287
    def __OOO00OOOO00O0000O (OOOO0O0O0000OOOO0 ,O0OOO0000O0OO00OO :str )->None :#line:289
        ""#line:294
        O000000000OOO00OO =OOOO0O0O0000OOOO0 .__O0O0OO00O00O0OO00 (O0OOO0000O0OO00OO )#line:295
        if O000000000OOO00OO :#line:296
            OO0OO0OOOOOOO0OOO =OOOO0O0O0000OOOO0 .__O0O0000000O0O0O0O (O0OOO0000O0OO00OO )#line:297
            utools .formate_print ('cookie有效即将开始查询任务……')#line:298
            utools .formate_print ('=========以下是任务信息=========')#line:299
            OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('=========以下是任务信息=========')#line:300
            O0OO000O0O00OOOOO =OOOO0O0O0000OOOO0 .__O00O0OOO00O0O0OO0 (O0OOO0000O0OO00OO )#line:302
            O00000OOOO0OO0OOO ,O0000OO00O00OOO00 =O0OO000O0O00OOOOO #line:303
            for O0O0OOO0000OO000O ,O000000O0OO000OOO in enumerate (O00000OOOO0OO0OOO ):#line:306
                if O0O0OOO0000OO000O ==0 :#line:307
                    utools .formate_print ('登录任务已完成')if O000000O0OO000OOO else utools .formate_print ('登录任务未完成')#line:309
                    OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('每日登录:已完成~获得5点经验值')#line:310
                elif O0O0OOO0000OO000O ==1 :#line:311
                    if O000000O0OO000OOO :#line:312
                        utools .formate_print ('观看视频任务已完成')#line:313
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('观看视频:已完成~获得5点经验值')#line:314
                    else :#line:315
                        utools .formate_print ('观看视频任务未完成,即将开始观看视频任务……')#line:316
                        OO00OO0000OOOO00O =OOOO0O0O0000OOOO0 .__O0OOO0OO00O00OO0O ()#line:317
                        OOO00O00O00OOO0O0 ,O000OO000O0O0O00O ,OO0O00O00O00000OO ,OOO00O0000OO0OOOO =Bilibili .random_video_para (OO00OO0000OOOO00O )#line:319
                        utools .formate_print (f'开始观看作者{OO0O00O00O00000OO}的视频{O000OO000O0O0O00O}……')#line:320
                        OOOO0O0O0000OOOO0 .__O000OOOOO00O00O00 (OOO00O00O00OOO0O0 ,O0OOO0000O0OO00OO )#line:321
                        utools .formate_print ('观看视频任务已完成，即将开始下一个任务……')#line:322
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('观看视频:完成~获得5点经验值')#line:323
                elif O0O0OOO0000OO000O ==2 :#line:324
                    if config .COIN_OR_NOT and OO0OO0OOOOOOO0OOO >=5 :#line:325
                        if O000000O0OO000OOO ==50 :#line:328
                            utools .formate_print ('投币任务已完成')#line:329
                            OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('每日投币:已完成~获得50点经验值')#line:330
                        else :#line:331
                            utools .formate_print ('投币任务未完成,即将开始投币任务')#line:332
                            O000OOOOOOOO0O0O0 =int ((50 -O000000O0OO000OOO )/10 )#line:333
                            for OO0OO0OO000000O0O in range (0 ,O000OOOOOOOO0O0O0 ):#line:334
                                OO0O00OOO0OOO0O00 =0 #line:335
                                if config .STRICT_MODE :#line:336
                                    while 1 :#line:337
                                        OOOO0O0O0O00O0000 =OOOO0O0O0000OOOO0 .__O00O0000OO0000000 (O0OOO0000O0OO00OO )#line:338
                                        OO0O00OOO0OOO0O00 +=1 #line:339
                                        if OOOO0O0O0O00O0000 or OO0O00OOO0OOO0O00 ==5 :#line:340
                                            break #line:343
                                        time .sleep (2 )#line:344
                                else :#line:345
                                    OOOO0O0O0000OOOO0 .__O00O0000OO0000000 (O0OOO0000O0OO00OO )#line:346
                                    time .sleep (2 )#line:347
                                time .sleep (1 )#line:348
                            utools .formate_print ('投币任务已完成，即将开始下一个任务……')#line:349
                            OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('每日投币:完成~获得50点经验值')#line:350
                    else :#line:351
                        utools .formate_print ('投币任务已跳过')#line:352
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('每日投币:跳过~')#line:353
                else :#line:354
                    if O000000O0OO000OOO :#line:355
                        utools .formate_print ('分享任务已完成')#line:356
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('每日分享:已完成~获得5点经验值')#line:357
                    else :#line:358
                        utools .formate_print ('分享任务未完成,即将开始分享任务……')#line:359
                        OO00OO0000OOOO00O =OOOO0O0O0000OOOO0 .__O0OOO0OO00O00OO0O ()#line:360
                        OOO00O00O00OOO0O0 ,O000OO000O0O0O00O ,OO0O00O00O00000OO ,OOO00O0000OO0OOOO =Bilibili .random_video_para (OO00OO0000OOOO00O )#line:362
                        utools .formate_print (f'开始分享{OO0O00O00O00000OO}的视频{O000OO000O0O0O00O}……')#line:363
                        OOOO0O0O0000OOOO0 .__O0OOO0O000O0O000O (OOO00O00O00OOO0O0 ,O0OOO0000O0OO00OO )#line:364
                        utools .formate_print ('分享任务已完成,日常任务已全部完成!即将查询额外任务……')#line:365
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('每日分享:完成~获得5点经验值')#line:366
                        time .sleep (1 )#line:367
            utools .formate_print ('==========以下是额外任务==============')#line:368
            OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('=========以下是额外任务=========')#line:369
            for O0O0OOO0000OO000O ,O000000O0OO000OOO in enumerate (O0000OO00O00OOO00 ):#line:371
                if O0O0OOO0000OO000O ==0 :#line:372
                    if O000000O0OO000OOO :#line:373
                        utools .formate_print ('绑定邮箱任务已完成')#line:374
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('绑定邮箱:已完成')#line:375
                    else :#line:376
                        utools .formate_print ('绑定邮箱任务未完成,完成可以获得20点经验值~')#line:377
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('绑定邮箱:未完成~完成可获得20点经验')#line:378
                elif O0O0OOO0000OO000O ==1 :#line:379
                    if O000000O0OO000OOO :#line:380
                        utools .formate_print ('绑定手机任务已完成')#line:381
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('绑定手机:已完成')#line:382
                    else :#line:383
                        utools .formate_print ('绑定手机任务未完成,完成可以获得100点经验值~')#line:384
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('绑定手机:未完成~完成可获得20点经验')#line:385
                elif O0O0OOO0000OO000O ==2 :#line:386
                    if O000000O0OO000OOO :#line:387
                        utools .formate_print ('设置密保任务已完成')#line:388
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('密保任务:已完成')#line:389
                    else :#line:390
                        utools .formate_print ('设置密保任务未完成,完成可以获得30点经验值~')#line:391
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('密保任务:未完成~完成可获得30点经验')#line:392
                else :#line:393
                    if O000000O0OO000OOO :#line:394
                        utools .formate_print ('实名认证任务已完成')#line:395
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('实名认证:已完成')#line:396
                    else :#line:397
                        utools .formate_print ('实名认证任务未完成,完成可以获得50点经验值~')#line:398
                        OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('实名认证:未完成~完成可获得50点经验')#line:399
            utools .formate_print ('==========以下是直播任务==============')#line:400
            OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('=========以下是直播任务=========')#line:401
            OOOO0O0O0000OOOO0 .__OOO0O0000000OO00O (O0OOO0000O0OO00OO )#line:402
            if config .SILVER2COIN_OR_NOT and OOOO0O0O0000OOOO0 .__O0OOOOO0OO0000OO0 (O0OOO0000O0OO00OO ):#line:403
                OOOO0O0O0000OOOO0 .__O00000OOOOOOOOOOO (O0OOO0000O0OO00OO )#line:405
            else :#line:406
                OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('银瓜子转换币:跳过~')#line:407
                utools .formate_print ('银瓜子兑换:跳过~')#line:408
            OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('=========以下是个人信息=========')#line:409
            utools .formate_print ('=========以下是个人信息=========')#line:410
            OOOO0O0O0000OOOO0 .__OOO0OO00O00O0O000 (O0OOO0000O0OO00OO )#line:411
        else :#line:412
            utools .formate_print ('cookie已失效,任务停止,请更换新的cookie!')#line:413
            OOOO0O0O0000OOOO0 .__OO0OOOOO000O000O0 ('cookie已失效,任务停止,请更换新的cookie!')#line:414
        utools .formate_print ('==========分割线==============')#line:415
    def go (O0O000O0OO0OO00O0 )->None :#line:417
        ""#line:421
        if len(config.COOKIE_LIST[0]) == 0:
            utools.formate_print('未添加cookie')
            return
        utools .formate_print (f'成功添加{len(config.COOKIE_LIST)}个cookie,开始任务……')#line:422
        for O0OOOOO0O000OO0OO ,O0OOOOO0O0OO0O00O in enumerate (config .COOKIE_LIST ):#line:423
            O0O000O0OO0OO00O0 .__OO0OOOOO000O000O0 (f'=========这是第{O0OOOOO0O000OO0OO+1}个账号=========')#line:424
            utools .formate_print (f'正在签到第{O0OOOOO0O000OO0OO+1}个账号……')#line:425
            O0O000O0OO0OO00O0 .__OOO00OOOO00O0000O (O0OOOOO0O0OO0O00O )#line:426
            time .sleep (1 )#line:427
        if config .PUSH_OR_NOT :#line:428
            push .pushplus (config .TOKEN ,O0O000O0OO0OO00O0 .log )#line:429
