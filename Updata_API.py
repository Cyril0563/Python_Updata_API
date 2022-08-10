'''
#Python调用API自动更新模块
#开源地址：https://github.com/Cyril0563/Python_Updata_API
#作者：Cyril0563
#时间：2022-08-10
'''


import requests

url = "https://xxx.cn/API/Version.json"#API接口地址
l_ver = '1.0' #本地软件版本号


#获取服务器API数据
r = requests.get(url)
if r.status_code == 200:
    print(r.status_code)#返回服务器状态码
    print(r.text)
    print("服务器下载地址：" + r.json()['down_url'])
    s_ver = r.json()['ver'] #获取服务器版本
else:
    print("网络错误,错误代码：" + r.status_code)
    # print(r.status_code)返回服务器错误状态码

#比较版本号
if l_ver < r.json()['ver']:
    print("发现新版本，正在更新中……请稍后！")
    #下载新版本
    r = requests.get(r.json()['down_url'])
    #保存新版本
    with open('图片手写识别' + s_ver + '.exe', 'wb') as f:
        f.write(r.content)
    print("更新完成！")
else:
    print("当前版本是最新版本，无需更新！")

    '''
    你可以在这里添加你的代码
    ……
    ……
    ……
    '''