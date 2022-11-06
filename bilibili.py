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
    def __init__ (O0OOOO000O0O000O0 )->None :#line:28
        O0OOOO000O0O000O0 .log =''#line:29
        O0OOOO000O0O000O0 .session =requests .Session ()#line:30
    @staticmethod #line:32
    def exchange_cookie (O0O0O00OOO0OOOO0O :str ):#line:33
        ""#line:38
        OO00OO00OOOOOO0O0 =dict ([OOOO0O0OOOO00O00O .split ("=",1 )for OOOO0O0OOOO00O00O in O0O0O00OOO0OOOO0O .split ("; ")])#line:39
        return OO00OO00OOOOOO0O0 #line:40
    def __OO000O0OOOOOO0000 (OOOOOOOOO0OOO000O ,OO0O0OO0OO0O0O0O0 :str )->int :#line:42
        ""#line:47
        O0OO0OO0O00O0O00O =Bilibili .exchange_cookie (OO0O0OO0OO0O0O0O0 )#line:48
        OO0OO000O0OOOOO0O =OOOOOOOOO0OOO000O .session .get (url =api .coin_url ,cookies =O0OO0OO0O00O0O00O ).json ()#line:49
        O0O0O00O0OO0OOOO0 =OO0OO000O0OOOOO0O ['code']#line:50
        if O0O0O00O0OO0OOOO0 ==0 :#line:51
            return 1 #line:53
        return 0 #line:54
    def __O000O000O0O0OOOOO (O00OOO0OOO0O0OO00 ,OO0OOOOOO00000OO0 :str )->int :#line:56
        ""#line:62
        OOOO0O0O0000OOOOO =O00OOO0OOO0O0OO00 .exchange_cookie (OO0OOOOOO00000OO0 )#line:63
        O00O000OOOO00O000 =O00OOO0OOO0O0OO00 .session .get (url =api .coin_url ,headers =data .headers ,cookies =OOOO0O0O0000OOOOO ).json ()#line:65
        OOOOO000O0OO0O000 =O00O000OOOO00O000 ['data']['money']#line:66
        if OOOOO000O0OO0O000 is None :#line:67
            return 0 #line:69
        else :#line:70
            return OOOOO000O0OO0O000 #line:71
    @staticmethod #line:73
    def get_csrf (OO0OOO0OO00OOOO00 :str )->str :#line:74
        ""#line:79
        O0O0OOO0OOOOOO0O0 =Bilibili .exchange_cookie (OO0OOO0OO00OOOO00 )#line:80
        O0O0OOO00O00OOO00 =O0O0OOO0OOOOOO0O0 ['bili_jct']#line:81
        return O0O0OOO00O00OOO00 #line:82
    def __O0OOO0OO0O000OOOO (O00OOO0O00OOOOO0O ,O0OO0000OO0OO00O0 :str )->None :#line:84
        ""#line:89
        OO0O0O00O0OOOOO0O =f'{O0OO0000OO0OO00O0}</br>'#line:90
        O00OOO0O00OOOOO0O .log =f'{O00OOO0O00OOOOO0O.log}{OO0O0O00O0OOOOO0O}'#line:91
    def __O000OO0OO00OO000O (O0OO0O0OO0O0O0O00 ,OO0OOO000000OOOO0 :str )->tuple :#line:93
        ""#line:98
        OOO0OO00OO0O0O00O =Bilibili .exchange_cookie (OO0OOO000000OOOO0 )#line:99
        O00O0O00O0OOOOO0O =O0OO0O0OO0O0O0O00 .session .get (url =api .inquire_url ,cookies =OOO0OO00OO0O0O00O ).json ()#line:101
        OO0OOO00OO0OOO000 =O00O0O00O0OOOOO0O ['data']['login']#line:102
        O000000OO0O0OO00O =O00O0O00O0OOOOO0O ['data']['watch']#line:103
        OOOO00O000O0O00O0 =O00O0O00O0OOOOO0O ['data']['coins']#line:104
        OO00O00OO0OOO0OOO =O00O0O00O0OOOOO0O ['data']['share']#line:105
        OOO0OO00O0OO00O0O =O00O0O00O0OOOOO0O ['data']['email']#line:107
        O0OOO00O0O0OO000O =O00O0O00O0OOOOO0O ['data']['tel']#line:108
        OO0O000OO0OOO0O00 =O00O0O00O0OOOOO0O ['data']['safe_question']#line:109
        OO0OOO0OOOOOOOO0O =O00O0O00O0OOOOO0O ['data']['identify_card']#line:110
        O0000O000OO00O00O =[OO0OOO00OO0OOO000 ,O000000OO0O0OO00O ,OOOO00O000O0O00O0 ,OO00O00OO0OOO0OOO ]#line:112
        OO00OO00O0O0O0O00 =[OOO0OO00O0OO00O0O ,O0OOO00O0O0OO000O ,OO0O000OO0OOO0O00 ,OO0OOO0OOOOOOOO0O ]#line:113
        return O0000O000OO00O00O ,OO00OO00O0O0O0O00 #line:114
    def __OO0OO000OO0O0OOO0 (O0OO0O0O0O0000000 ,O0OO0O0OOOOOOOOOO :str )->None :#line:116
        ""#line:121
        OO00OO0OO0O00OO0O =Bilibili .exchange_cookie (O0OO0O0OOOOOOOOOO )#line:122
        OO0O00O0OOOO000OO =O0OO0O0O0O0000000 .session .get (url =api .info_url ,cookies =OO00OO0OO0O00OO0O ).json ()#line:123
        OOOO00O0O00000000 =OO0O00O0OOOO000OO ['data']['mid']#line:124
        OOO0O0O0O0OOOOO0O =OO0O00O0OOOO000OO ['data']['name']#line:125
        O0OO0OO0000O0O0O0 =OO0O00O0OOOO000OO ['data']['level']#line:126
        OOOOOOO0OOOO000OO =OO0O00O0OOOO000OO ['data']['level_exp']['current_exp']#line:127
        O0O0OO00OOO0OOO0O =OO0O00O0OOOO000OO ['data']['level_exp']['next_exp']#line:128
        O000O0O00OOO0OO0O =O0O0OO00OOO0OOO0O -OOOOOOO0OOOO000OO #line:129
        OO0000O00O0O000OO =int (O000O0O00OOO0OO0O /65 )#line:130
        OO00O0OOOOOO0OOOO =OO0O00O0OOOO000OO ['data']['coins']#line:131
        OO00O0O0OO0OOOOO0 =OO0O00O0OOOO000OO ['data']['vip']['status']#line:132
        O00OO00O0O0O00OO0 =OO0O00O0OOOO000OO ['data']['vip']['due_date']#line:133
        O00OO00O0O0O00OO0 =utools .formate_time (O00OO00O0O0O00OO0 )#line:134
        if OO00O0O0OO0OOOOO0 :#line:135
            O0000OO0OO000O00O =f"用户{OOO0O0O0O0OOOOO0O},uid为{OOOO00O0O00000000}您是大会员,大会员到期时间为{O00OO00O0O0O00OO0},你目前的等级是{O0OO0OO0000O0O0O0}级,目前的经验{OOOOOOO0OOOO000OO},离下个等级还差{O000O0O00OOO0OO0O}经验,需要{OO0000O00O0O000OO}天剩余硬币还有{OO00O0OOOOOO0OOOO}个"#line:136
            O0OO0O0O0O0000000 .__O0OOO0OO0O000OOOO (f"用户名:{OOO0O0O0O0OOOOO0O}</br>uid:{OOOO00O0O00000000}</br>VIP:大会员</br>到期时间:{O00OO00O0O0O00OO0}</br>目前的等级:{O0OO0OO0000O0O0O0}级</br>目前的经验:{OOOOOOO0OOOO000OO}</br>离下个等级:{O000O0O00OOO0OO0O}经验<br>距升级还差:{OO0000O00O0O000OO}天</br>剩余硬币数:{OO00O0OOOOOO0OOOO}个")#line:138
            utools .formate_print (O0000OO0OO000O00O )#line:139
        else :#line:140
            O0000OO0OO000O00O =f"用户{OOO0O0O0O0OOOOO0O},uid为{OOOO00O0O00000000}您的大会员已过期,过期时间为{O00OO00O0O0O00OO0},你目前的等级是{O0OO0OO0000O0O0O0}级,目前的经验{OOOOOOO0OOOO000OO},离下个等级还差{O000O0O00OOO0OO0O}经验,需要{OO0000O00O0O000OO}天,剩余硬币还有{OO00O0OOOOOO0OOOO}个"#line:141
            O0OO0O0O0O0000000 .__O0OOO0OO0O000OOOO (f"用户名:{OOO0O0O0O0OOOOO0O}</br>uid:{OOOO00O0O00000000}</br>VIP:非大会员</br>过期时间:{O00OO00O0O0O00OO0}</br>目前的等级:{O0OO0OO0000O0O0O0}级</br>目前的经验:{OOOOOOO0OOOO000OO}</br>离下个等级:{O000O0O00OOO0OO0O}经验<br>距升级还差:{OO0000O00O0O000OO}天</br>剩余硬币数:{OO00O0OOOOOO0OOOO}个")#line:143
            utools .formate_print (O0000OO0OO000O00O )#line:144
    def __OO00OOO0O000O0O00 (OO0OOO00O00OOOO0O ,OO0OOOO00O0O00000 )->list :#line:146
        ""#line:150
        O00OOO0O0O00O000O =config .UID_LIST #line:152
        O0O00000O0O0O00OO =data .video_list_headers #line:153
        O0O00000O0O0O00OO ['cookie']=OO0OOOO00O0O00000 #line:154
        O0OO0000O00OO0OOO =OO0OOO00O00OOOO0O .session .get (url =api .get_video_list_url .format (random .choice (O00OOO0O0O00O000O )),headers =O0O00000O0O0O00OO ).json ()#line:156
        OOO0O000O00O00OO0 =O0OO0000O00OO0OOO ['data']['list']['vlist']#line:159
        return OOO0O000O00O00OO0 #line:160
    def __O0OO0OOO0O0OO00OO (OO0OO00OO00OO0O00 ,OOOOO00OO0O00O0O0 :str ,OOOOO0O0O0O00OOO0 :str )->None :#line:162
        ""#line:168
        O0O0O000O0OOO0O00 =random .randint (30 ,60 )#line:169
        data .watch_video_data ['bvid']=OOOOO00OO0O00O0O0 #line:170
        data .watch_video_data ['played_time']=str (O0O0O000O0OOO0O00 )#line:171
        data .watch_video_data ['csrf']=Bilibili .get_csrf (OOOOO0O0O0O00OOO0 )#line:172
        O0OO00OOOO000OO00 =Bilibili .exchange_cookie (OOOOO0O0O0O00OOO0 )#line:173
        OOOOO0O0OOO0O000O =OO0OO00OO00OO0O00 .session .post (url =api .watch_video_url ,data =data .watch_video_data ,cookies =O0OO00OOOO000OO00 ).json ()#line:175
        OOOOO0O000O0OOO00 =OOOOO0O0OOO0O000O ['code']#line:176
        if OOOOO0O000O0OOO00 ==0 :#line:178
            utools .formate_print ('看视频完成')#line:179
        else :#line:180
            utools .formate_print ('看视频失败')#line:181
    def __OO0O0OO00O00OO0OO (O00O000OOOO0OOOO0 ,O00OO00O000OOO00O :str ,OOOOO000OOO00OOOO :str )->None :#line:183
        ""#line:189
        data .share_video_data ['bvid']=O00OO00O000OOO00O #line:190
        data .share_video_data ['csrf']=Bilibili .get_csrf (OOOOO000OOO00OOOO )#line:191
        OOOO0OOO0O000O00O =Bilibili .exchange_cookie (OOOOO000OOO00OOOO )#line:192
        OOO0000O0000O0O0O =O00O000OOOO0OOOO0 .session .post (url =api .share_video_url ,data =data .share_video_data ,cookies =OOOO0OOO0O000O00O ,headers =data .headers ).json ()#line:194
        O00O0OO0O0OO0OO0O =OOO0000O0000O0O0O ['code']#line:195
        if O00O0OO0O0OO0OO0O ==0 :#line:196
            utools .formate_print ('分享视频成功')#line:197
        else :#line:198
            utools .formate_print ('分享视频失败')#line:199
    def __O00OOO000000OO0OO (OOO0O000000OO0000 ,OOO00OOO0O00OOOOO :str ,OO000OOOO0OO0000O :str )->int :#line:201
        ""#line:208
        O00O00OO0O0OOOOO0 =Bilibili .exchange_cookie (OO000OOOO0OO0000O )#line:209
        OO0000OO0OOOO0OOO =data .insert_coin_data #line:210
        OOO0O000000OOO0O0 =data .insert_coin_headers #line:211
        OO0000OO0OOOO0OOO ['aid']=OOO00OOO0O00OOOOO #line:212
        OO0000OO0OOOO0OOO ['csrf']=Bilibili .get_csrf (OO000OOOO0OO0000O )#line:213
        OOO0O000000OOO0O0 ['cookie']=OO000OOOO0OO0000O #line:214
        O0OO000O0O0000OOO =OOO0O000000OO0000 .session .post (url =api .insert_coins_url ,headers =OOO0O000000OOO0O0 ,data =OO0000OO0OOOO0OOO ,cookies =O00O00OO0O0OOOOO0 ).json ()#line:217
        O00O000O0OO00OOOO =O0OO000O0O0000OOO ['data']['like']#line:218
        if O00O000O0OO00OOOO :#line:219
            utools .formate_print ('投币成功')#line:220
            return 1 #line:221
        else :#line:222
            utools .formate_print ('投币失败')#line:223
            return 0 #line:224
    @staticmethod #line:226
    def random_video_para (O00O0O0O000000O00 :list )->tuple :#line:227
        ""#line:232
        OOOO0OO0OOOO00000 =random .randint (0 ,len (O00O0O0O000000O00 )-1 )#line:233
        O0OOO0OOOO0000OO0 =O00O0O0O000000O00 [OOOO0OO0OOOO00000 ]['bvid']#line:234
        OOO0000O0O0OO0OOO =O00O0O0O000000O00 [OOOO0OO0OOOO00000 ]['title']#line:235
        O0OO000O00000OO0O =O00O0O0O000000O00 [OOOO0OO0OOOO00000 ]['author']#line:236
        O000000OO00OO00O0 =O00O0O0O000000O00 [OOOO0OO0OOOO00000 ]['aid']#line:237
        return O0OOO0OOOO0000OO0 ,OOO0000O0O0OO0OOO ,O0OO000O00000OO0O ,O000000OO00OO00O0 #line:238
    def __O0O000O00O0OOOOO0 (O0OOO000000O0OO00 ,OO0O00OO0OO0O0O00 :str )->int :#line:240
        ""#line:245
        O0O0OO0O0OO0OOOO0 =O0OOO000000O0OO00 .__OO00OOO0O000O0O00 (OO0O00OO0OO0O0O00 )#line:246
        O0O00OOOOOO00O0O0 ,O0OOOOOO0OOO000O0 ,O0OO0OO0000000OO0 ,O0O0000OOOO0O00OO =Bilibili .random_video_para (O0O0OO0O0OO0OOOO0 )#line:248
        utools .formate_print (f'开始向{O0OO0OO0000000OO0}的视频{O0OOOOOO0OOO000O0}投币……')#line:249
        OO0O00OO0O00OO000 =O0OOO000000O0OO00 .__O00OOO000000OO0OO (O0O0000OOOO0O00OO ,OO0O00OO0OO0O0O00 )#line:250
        return OO0O00OO0O00OO000 #line:251
    def __OOO0OOO0OO00O0O0O (O00OOOO0OOO0O0O0O ,OO000O0O0O0OO0OOO :str )->None :#line:253
        OO0OO0OO0OOO0O0O0 =O00OOOO0OOO0O0O0O .session .get (url =api .live_sign_url ,cookies =Bilibili .exchange_cookie (OO000O0O0O0OO0OOO )).json ()#line:254
        if OO0OO0OO0OOO0O0O0 ['code']==0 :#line:255
            OOOOO0OOO0OO0O000 =OO0OO0OO0OOO0O0O0 ['data']['text']#line:256
            OO0000OOO00OOO00O =OO0OO0OO0OOO0O0O0 ['data']['hadSignDays']#line:257
            O00OOOO0OOO0O0O0O .__O0OOO0OO0O000OOOO ('直播签到:签到成功,签到天数为{}'.format (OO0000OOO00OOO00O ))#line:258
            utools .formate_print (f'签到奖励:{OOOOO0OOO0OO0O000},连续签到{OO0000OOO00OOO00O}天')#line:259
            O00OOOO0OOO0O0O0O .__O0OOO0OO0O000OOOO (f'签到奖励:{OOOOO0OOO0OO0O000},连续签到{OO0000OOO00OOO00O}天')#line:260
        else :#line:261
            utools .formate_print ('直播签到:当天已签到~')#line:262
            O00OOOO0OOO0O0O0O .__O0OOO0OO0O000OOOO ('直播签到:当天已签到')#line:263
    def __O0OOOO0OO0OO0OO0O (O0OOOO0OOO0OO0O00 ,O0O0000OOOO0000O0 :str )->bool :#line:265
        ""#line:270
        O0O00OO000OOOO0O0 =O0OOOO0OOO0OO0O00 .session .get (url =api .live_info_url ,cookies =Bilibili .exchange_cookie (O0O0000OOOO0000O0 )).json ()#line:271
        O0OOOO0OOO0OO0O00 .__O0OOO0OO0O000OOOO (f'银瓜子数量:{O0O00OO000OOOO0O0["data"]["silver"]}')#line:272
        utools .formate_print (f'银瓜子数量:{O0O00OO000OOOO0O0["data"]["silver"]}')#line:273
        if O0O00OO000OOOO0O0 ['data']['silver']>700 :#line:274
            return True #line:275
        return False #line:276
    def __O00OO0O0000000O0O (O0OO00O00O00OOOO0 ,O00OOOOOOOO0OOOOO :str )->None :#line:278
        O0OO00O00O0OOOO00 =data .silver2coin_data #line:279
        O0OO00O00O0OOOO00 ['csrf']=Bilibili .get_csrf (O00OOOOOOOO0OOOOO )#line:280
        O0OO00O00O0OOOO00 ['csrf_token']=Bilibili .get_csrf (O00OOOOOOOO0OOOOO )#line:281
        OO00O0OO0O0O0O0O0 =O0OO00O00O00OOOO0 .session .post (url =api .silver2coin_url ,cookies =Bilibili .exchange_cookie (O00OOOOOOOO0OOOOO ),data =O0OO00O00O0OOOO00 ).json ()#line:282
        if OO00O0OO0O0O0O0O0 ['code']==0 :#line:283
            OOOOO0OOOO000O000 =OO00O0OO0O0O0O0O0 ['data']['silver']#line:284
            utools .formate_print ('银瓜子兑换:成功!')#line:285
            utools .formate_print (f'银瓜子剩余:{OOOOO0OOOO000O000}个')#line:286
            O0OO00O00O00OOOO0 .__O0OOO0OO0O000OOOO ('银瓜子兑换:成功!')#line:287
            O0OO00O00O00OOOO0 .__O0OOO0OO0O000OOOO (f'银瓜子剩余:{OOOOO0OOOO000O000}个')#line:288
        else :#line:289
            utools .formate_print ('银瓜子兑换:当天已兑换!')#line:290
            O0OO00O00O00OOOO0 .__O0OOO0OO0O000OOOO ('银瓜子兑换:当天已兑换!')#line:291
    def __OOOOO0OOOO00OOOOO (O00OO0000O00O0O00 ,OO0000O000000OO0O :str )->None :#line:293
        ""#line:298
        OO000OO000000O00O =O00OO0000O00O0O00 .__OO000O0OOOOOO0000 (OO0000O000000OO0O )#line:299
        if OO000OO000000O00O :#line:300
            O0O0OO0OOO0OO0O00 =O00OO0000O00O0O00 .__O000O000O0O0OOOOO (OO0000O000000OO0O )#line:301
            utools .formate_print ('cookie有效即将开始查询任务……')#line:302
            utools .formate_print ('=========以下是任务信息=========')#line:303
            O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('=========以下是任务信息=========')#line:304
            OOO0OO0OO0O000O00 =O00OO0000O00O0O00 .__O000OO0OO00OO000O (OO0000O000000OO0O )#line:306
            OO00O0000000O0O0O ,O00O00OOOO0O0000O =OOO0OO0OO0O000O00 #line:307
            for OO00O00O00OOOO0O0 ,O0OOOO00OOOOO00OO in enumerate (OO00O0000000O0O0O ):#line:310
                if OO00O00O00OOOO0O0 ==0 :#line:311
                    utools .formate_print ('登录任务已完成')if O0OOOO00OOOOO00OO else utools .formate_print ('登录任务未完成')#line:313
                    O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('每日登录:已完成~获得5点经验值')#line:314
                elif OO00O00O00OOOO0O0 ==1 :#line:315
                    if O0OOOO00OOOOO00OO :#line:316
                        utools .formate_print ('观看视频任务已完成')#line:317
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('观看视频:已完成~获得5点经验值')#line:318
                    else :#line:319
                        utools .formate_print ('观看视频任务未完成,即将开始观看视频任务……')#line:320
                        O0OO0O000O0000O00 =O00OO0000O00O0O00 .__OO00OOO0O000O0O00 (OO0000O000000OO0O )#line:321
                        OO0000OOOOO000OOO ,OO00OOOOOOOO0OO00 ,OO0O00O00O0O0O00O ,O0O0O0OO0O0OO00OO =Bilibili .random_video_para (O0OO0O000O0000O00 )#line:323
                        utools .formate_print (f'开始观看作者{OO0O00O00O0O0O00O}的视频{OO00OOOOOOOO0OO00}……')#line:324
                        O00OO0000O00O0O00 .__O0OO0OOO0O0OO00OO (OO0000OOOOO000OOO ,OO0000O000000OO0O )#line:325
                        utools .formate_print ('观看视频任务已完成，即将开始下一个任务……')#line:326
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('观看视频:完成~获得5点经验值')#line:327
                elif OO00O00O00OOOO0O0 ==2 :#line:328
                    if config .COIN_OR_NOT and O0O0OO0OOO0OO0O00 >=5 :#line:329
                        if O0OOOO00OOOOO00OO ==50 :#line:332
                            utools .formate_print ('投币任务已完成')#line:333
                            O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('每日投币:已完成~获得50点经验值')#line:334
                        else :#line:335
                            utools .formate_print ('投币任务未完成,即将开始投币任务')#line:336
                            OOOO000O0O0OO0O0O =int ((50 -O0OOOO00OOOOO00OO )/10 )#line:337
                            for OO0O0OO0OO0O0O0OO in range (0 ,OOOO000O0O0OO0O0O ):#line:338
                                OOOO0O0O000OO0000 =0 #line:339
                                if config .STRICT_MODE :#line:340
                                    while 1 :#line:341
                                        OOOO0OOO0O0OO0OO0 =O00OO0000O00O0O00 .__O0O000O00O0OOOOO0 (OO0000O000000OO0O )#line:342
                                        OOOO0O0O000OO0000 +=1 #line:343
                                        if OOOO0OOO0O0OO0OO0 or OOOO0O0O000OO0000 ==5 :#line:344
                                            break #line:347
                                        time .sleep (2 )#line:348
                                else :#line:349
                                    O00OO0000O00O0O00 .__O0O000O00O0OOOOO0 (OO0000O000000OO0O )#line:350
                                    time .sleep (2 )#line:351
                                time .sleep (1 )#line:352
                            utools .formate_print ('投币任务已完成，即将开始下一个任务……')#line:353
                            O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('每日投币:完成~获得50点经验值')#line:354
                    else :#line:355
                        utools .formate_print ('投币任务已跳过')#line:356
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('每日投币:跳过~')#line:357
                else :#line:358
                    if O0OOOO00OOOOO00OO :#line:359
                        utools .formate_print ('分享任务已完成')#line:360
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('每日分享:已完成~获得5点经验值')#line:361
                    else :#line:362
                        utools .formate_print ('分享任务未完成,即将开始分享任务……')#line:363
                        O0OO0O000O0000O00 =O00OO0000O00O0O00 .__OO00OOO0O000O0O00 (OO0000O000000OO0O )#line:364
                        OO0000OOOOO000OOO ,OO00OOOOOOOO0OO00 ,OO0O00O00O0O0O00O ,O0O0O0OO0O0OO00OO =Bilibili .random_video_para (O0OO0O000O0000O00 )#line:366
                        utools .formate_print (f'开始分享{OO0O00O00O0O0O00O}的视频{OO00OOOOOOOO0OO00}……')#line:367
                        O00OO0000O00O0O00 .__OO0O0OO00O00OO0OO (OO0000OOOOO000OOO ,OO0000O000000OO0O )#line:368
                        utools .formate_print ('分享任务已完成,日常任务已全部完成!即将查询额外任务……')#line:369
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('每日分享:完成~获得5点经验值')#line:370
                        time .sleep (1 )#line:371
            utools .formate_print ('==========以下是额外任务==============')#line:372
            O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('=========以下是额外任务=========')#line:373
            for OO00O00O00OOOO0O0 ,O0OOOO00OOOOO00OO in enumerate (O00O00OOOO0O0000O ):#line:375
                if OO00O00O00OOOO0O0 ==0 :#line:376
                    if O0OOOO00OOOOO00OO :#line:377
                        utools .formate_print ('绑定邮箱任务已完成')#line:378
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('绑定邮箱:已完成')#line:379
                    else :#line:380
                        utools .formate_print ('绑定邮箱任务未完成,完成可以获得20点经验值~')#line:381
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('绑定邮箱:未完成~完成可获得20点经验')#line:382
                elif OO00O00O00OOOO0O0 ==1 :#line:383
                    if O0OOOO00OOOOO00OO :#line:384
                        utools .formate_print ('绑定手机任务已完成')#line:385
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('绑定手机:已完成')#line:386
                    else :#line:387
                        utools .formate_print ('绑定手机任务未完成,完成可以获得100点经验值~')#line:388
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('绑定手机:未完成~完成可获得20点经验')#line:389
                elif OO00O00O00OOOO0O0 ==2 :#line:390
                    if O0OOOO00OOOOO00OO :#line:391
                        utools .formate_print ('设置密保任务已完成')#line:392
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('密保任务:已完成')#line:393
                    else :#line:394
                        utools .formate_print ('设置密保任务未完成,完成可以获得30点经验值~')#line:395
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('密保任务:未完成~完成可获得30点经验')#line:396
                else :#line:397
                    if O0OOOO00OOOOO00OO :#line:398
                        utools .formate_print ('实名认证任务已完成')#line:399
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('实名认证:已完成')#line:400
                    else :#line:401
                        utools .formate_print ('实名认证任务未完成,完成可以获得50点经验值~')#line:402
                        O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('实名认证:未完成~完成可获得50点经验')#line:403
            utools .formate_print ('==========以下是直播任务==============')#line:404
            O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('=========以下是直播任务=========')#line:405
            O00OO0000O00O0O00 .__OOO0OOO0OO00O0O0O (OO0000O000000OO0O )#line:406
            if config .SILVER2COIN_OR_NOT and O00OO0000O00O0O00 .__O0OOOO0OO0OO0OO0O (OO0000O000000OO0O ):#line:407
                O00OO0000O00O0O00 .__O00OO0O0000000O0O (OO0000O000000OO0O )#line:409
            else :#line:410
                O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('银瓜子转换币:跳过~')#line:411
                utools .formate_print ('银瓜子兑换:跳过~')#line:412
            O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('=========以下是个人信息=========')#line:413
            utools .formate_print ('=========以下是个人信息=========')#line:414
            O00OO0000O00O0O00 .__OO0OO000OO0O0OOO0 (OO0000O000000OO0O )#line:415
        else :#line:416
            utools .formate_print ('cookie已失效,任务停止,请更换新的cookie!')#line:417
            O00OO0000O00O0O00 .__O0OOO0OO0O000OOOO ('cookie已失效,任务停止,请更换新的cookie!')#line:418
        utools .formate_print ('==========分割线==============')#line:419
    def go (O0OO00O0OOO00OOO0 )->None :#line:421
        ""#line:425
        utools .formate_print (f'成功添加{len(config.COOKIE_LIST)}个cookie,开始任务……')#line:426
        for O000OO0000OO00000 ,OO0O0OO0O00O0O000 in enumerate (config .COOKIE_LIST ):#line:427
            O0OO00O0OOO00OOO0 .__O0OOO0OO0O000OOOO (f'=========这是第{O000OO0000OO00000+1}个账号=========')#line:428
            utools .formate_print (f'正在签到第{O000OO0000OO00000+1}个账号……')#line:429
            O0OO00O0OOO00OOO0 .__OOOOO0OOOO00OOOOO (OO0O0OO0O00O0O000 )#line:430
            time .sleep (1 )#line:431
        if config .PUSH_OR_NOT :#line:432
            push .pushplus (config .TOKEN ,O0OO00O0OOO00OOO0 .log )#line:433
