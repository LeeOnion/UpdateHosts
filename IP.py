import requests
from bs4 import BeautifulSoup as bs

# 利用requests获取数据，并用BeautifulSoup解析
def getWebData(src):
    html = requests.get(src).content
    soup = bs(html, 'lxml')
    return soup.li

def updateHosts(ip1, ip2):
    # 根据自己实际hosts文件地址进行修改
    PATH = 'C:\Windows\System32\drivers\etc\hosts'

    # log
    print("github.com IP Address:" + ip1)
    print("github.global.ssl.fastly.net IP Address:" + ip2)

    with open(PATH, 'r+', encoding='utf-8') as fileR:
        lines = fileR.readlines()
    with open(PATH, 'w+', encoding='utf-8') as fileW:
        exist1 = False
        exist2 = False
        for line in lines:
            # 加空格防止误匹配
            if " github.com" in line:
                line = line.replace(line, ip1 + " github.com\n")
                exist1 = True
            if " github.global.ssl.fastly.net" in line:
                line = line.replace(line, ip2 + " github.global.ssl.fastly.net\n")
                exist2 = True
            fileW.write(line)
        # 如果之前不存在，则添加
        if exist1 == False:
            fileW.write(ip1 + " github.com\n")
        if exist2 == False:
            fileW.write(ip2 + " github.global.ssl.fastly.net\n")

if __name__ == '__main__':
    # url
    src1 = 'https://github.com.ipaddress.com/'
    src2 = 'https://fastly.net.ipaddress.com/github.global.ssl.fastly.net'
    ip1 = str(getWebData(src1))
    ip2 = str(getWebData(src2))
    # 简单解析获取IP地址
    updateHosts(ip1[4:len(ip1) - 5], ip2[4:len(ip2) - 5])