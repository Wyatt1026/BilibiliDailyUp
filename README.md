## Bilibili升级云函数

## 前言

本意是自己维护且使用的一个脚本,将维护到自己不再使用为止。

## 功能

### 已实现功能

  <table>
 		<tr>
    <td>序号</td>
    <td>功能名称</td>
    <td>对应奖励</td>
    <td>状态</td>
    <td>时间</td>
 	 </tr>
    <tr>
    <td>1</td>
    <td>每日登录</td>
    <td>5点经验值</td>
    <td>✅</td>
    <td>2022/08/10</td>
  	</tr>
    <tr>
    <td>2</td>
    <td>每日观看视频</td>
    <td>5点经验值和一枚硬币</td>
    <td>✅</td>
    <td>2022/08/10</td>
  	</tr>
        <tr>
    <td>3</td>
    <td>每日投币</td>
    <td>50点经验值</td>
    <td>✅</td>
    <td>2022/08/10</td>
  	</tr>
        <tr>
    <td>4</td>
    <td>每日分享视频</td>
    <td>5点经验值</td>
    <td>✅</td>
    <td>2022/08/10</td>
  	</tr>
        <tr>
    <td>5</td>
    <td>每日直播签到</td>
    <td>直播经验和辣条</td>
    <td>✅</td>
    <td>2022/08/10</td>
  	</tr>
        <tr>
    <td>6</td>
    <td>银瓜子兑换硬币</td>
    <td>1枚硬币</td>
    <td>✅</td>
    <td>2022/08/10</td>
  	</tr>
    <tr>
</table>


> 其他功能如漫画签到,直播输赢压硬币等以后随缘添加,因为本来就是自己用的，很多功能自己也用不着

## 配置

> 配置文件是`config.py`文件
### 配置参数列表和说明
  <table>
 		<tr>
    <td>序号</td>
    <td>参数名</td>
    <td>说明</td>
    <td>默认</td>
 	 </tr>
    <tr>
    <td>1</td>
    <td>COIN_OR_NOT</td>
    <td>是否投币</td>
    <td>默认为TRUE</td>
  	</tr>
        <tr>
    <td>2</td>
    <td>SILVER2COIN_OR_NOT</td>
    <td>是否将银瓜子转换为硬币</td>
    <td>默认为TRUE</td>
  	</tr>
            <tr>
    <td>3</td>
    <td>STRICT_MODE</td>
    <td>是否开启严格模式(解释见配置文件)</td>
    <td>默认为TRUE</td>
  	</tr>
                <tr>
    <td>4</td>
    <td>UID_LIST</td>
    <td>投币UP主ID号</td>
    <td>默认新华网/人民日报/央视频/王冰冰/英雄联盟赛事四位UP</td>
  	</tr>
                    <tr>
    <td>5</td>
    <td>COOKIE_LIST</td>
    <td>哔哩哔哩账号COOKIE列表-支持多账号</td>
    <td>无默认值</td>
  	</tr>
                        <tr>
    <td>6</td>
    <td>PUSH_OR_NOT</td>
    <td>是否推送至微信</td>
    <td>默认为False</td>
  	</tr>
                            <tr>
    <td>7</td>
    <td>TOKEN</td>
    <td>PUSHPLUS的TOKEN</td>
    <td>无默认值</td>
  	</tr>
    <tr>
</table>

## 本地运行

- 安装依赖`pip3 install -r requirements.txt`
- `python3 main.py`

## 云端部署

> 阿里云函数我自己不用,理论上来说和腾讯云函数类似

### 腾讯云函数☁️

- 1.新建python3.6空白函数

- 2.在高级配置-环境配置中把初始化时间和执行超时时间改成最大![](https://img.ifool.me/i/2022/08/15/fq93if.webp)

- 3.在创建好的云函数中对着脚本里的文件新建文件复制黏贴代码![](https://img.ifool.me/i/2022/08/15/fs5ua7.webp)

- 4.修改配置文件`config.py`
- 5.部署运行测试
- 6.添加每日定时运行规则

### 青龙面板🐉

> 演示机器腾讯云上海4h3g ubuntu22.04

- 1.ssh连接服务器
- 2.进入青龙面板脚本对应文件夹
- 3.把压缩包上传到脚本目录
- 4.解压
- 运行测试![](https://img.ifool.me/i/2022/08/15/qo0ptr.webp)

## COOKIE抓取

- 打开哔哩哔哩网页端登录好
- 新建一个浏览器页面,打开开发者模式,复制链接`http://account.bilibili.com/site/getCoin`黏贴打开
- 复制`cookie`黏贴到脚本即可![](https://img.ifool.me/i/2022/08/15/h9n8b4.webp)

## up主UID获取

如下图问号前面的一串数字就是UID

![](https://img.ifool.me/i/2022/08/15/hhnbpl.webp)

## 运行截图

![](https://img.ifool.me/i/2022/08/15/hb1oly.webp)
