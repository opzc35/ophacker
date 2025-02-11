import requests
import time

# 假设你的cookie列表是一个包含字典的列表，每个字典包含 __uid 和 __client_id
cookie_list = [
    {"__uid": "1664685", "__client_id": "b24ff458ba44fe9b1fa1412df6d51c637eae724d"},
    {"__uid": "1234567", "__client_id": "abcdef1234567890abcdef1234567890abcdef12"},
    # 添加更多用户的cookie
]

# 目标URL
url = "https://www.luogu.com.cn/api/team/join/98902"

# 请求头
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "dnt": "1",
    "origin": "https://www.luogu.com.cn",
    "priority": "u=1, i",
    "referer": "https://www.luogu.com.cn/team/98902",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "x-csrf-token": "1739349086:zP7BiiDLegBUYpVusI8aNVwLlBcp/EbPogAlTBCPpjQ=",
    "x-requested-with": "XMLHttpRequest",
}

# 请求体
data = {
    "applyMessage": "asdf"
}

# 遍历每个用户的cookie并发送请求
for cookie in cookie_list:
    # 构造完整的cookie字符串
    cookies = {
        "__client_id": cookie["__client_id"],
        "_uid": cookie["__uid"],
        "C3VK": "598882"  # 假设C3VK是固定的
    }

    # 发送POST请求
    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=data)
        print(f"用户 {cookie['__uid']} 的请求结果: 状态码 {response.status_code}, 响应内容: {response.text}")
    except Exception as e:
        print(f"用户 {cookie['__uid']} 的请求失败: {e}")

    # 每隔0.5秒发送一次请求
    time.sleep(0.5)