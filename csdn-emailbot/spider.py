import re
import requests
import json


def PoJie(headers):
    # 提取主页
    session = requests.session()
    qdurl = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
    qd = session.post(qdurl, headers=headers)
    soup=session.post(url="https://www.52pojie.cn/forum.php", headers=headers).text
    if  re.findall(r"(wbs.png)",str(soup))[0] == "wbs.png": 
        waxx="吾爱打卡成功"
    else:
        waxx="吾爱打卡失败"
    return waxx
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
        'cookie':'KF4=Gzx4tU; htVC_2132_saltkey=mo7RIh5v; htVC_2132_lastvisit=1638112294; htVC_2132_seccodecS=5454231.03a35da74d1a4cd661; htVC_2132_seccodecSxV4=5454232.b4a53c9065defbf2a3; htVC_2132_ulastactivity=1638115902%7C0; htVC_2132_auth=69c5Wtp2KQR4Kl2KSgFKLaKoehnjFVMeoyFByG6mTICSFUZs%2FMamPyWMUIYYtaJ7X19%2FKZI2bIQg4OG0FC%2FpfKmuZV4; htVC_2132_lip=112.49.76.86%2C1638115902; htVC_2132_sid=0; htVC_2132_connect_is_bind=1; htVC_2132_nofavfid=1; wzws_sid=b8faeb71d36f40743f54e68be0c95bd7deb9ecbf7ee9d07c90410adfecb50326190b58d15d033a0c393042f20dab1d358765ff00c09f87908e774aaa4af183ff952eee725c89e93372a4659b531f755e; htVC_2132_onlineusernum=20021; htVC_2132_checkpm=1; htVC_2132_lastact=1638116295%09home.php%09spacecp; htVC_2132_lastcheckfeed=212945%7C1638116295,'
        'ContentType': 'text/html;charset=gbk'
        }

waxx=PoJie(headers)



# 消息推送
content =waxx
pdata ={
	"token": "6d0fa8fdf6014c96aef41245e39015dc",
    "title":"多网站打卡",
	"content":"\n".join(content),
	"template": "html"
}
requests.post(url="http://pushplus.hxtrip.com/send",data=pdata)





