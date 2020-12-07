import requests
import random
DEBUG = False
Times = 32
name = '2555'
headers = {
    "Host": "expert.baidu.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36",
    "Accept": "*/*",
    "Origin": "http://expert.baidu.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "http://expert.baidu.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    #"Cookie": 'BAIDUID=1BF580582D825CFB37323160D887197B:FG=1; PSTM=1607326758; BIDUPSID=F9EEF3F002F758AD0665D48DE348A945; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; BAIDUID_BFESS=4736021C7747F9B90EA221840997A1C7:FG=1; H_PS_PSSID=1435_33103_33123_33060_32974_33098_33101_32938_33199_33238_33149_22159; BA_HECTOR=2g00al0h20a5858kio1fsro0j0q'
    "Cookie": 'BAIDUID=10257; '
    }
#https://expert.baidu.com/med/page/jp/topic/vote?name=2543&referlid=1620565154&applid=&lid=1620565154
for i in range(Times):
    ag = random.randint(1e6,1e9)
    BAIDUID = random.randint(1e9,9e9)
    headers['Cookie'] = 'BAIDUID={}'.format(BAIDUID)
    agent = str(ag)
    url = 'https://expert.baidu.com/med/page/jp/topic/vote?name={}&referlid={}&applid=&lid={}'.format(name,agent,agent)
    res = requests.get(url,headers = headers)
    ret = res.text
    s = ret.find('"num')
    j = ret.find(',"voted')
    ret = ret[s:j]
    if(s == j):
        print('Repeated Operations')
    if DEBUG:
        print(url,ag,BAIDUID)
        print("NOW:{}\t".format(ret),i,res.status_code,res.text)
    else :
        print("NOW:{}\t".format(ret))
