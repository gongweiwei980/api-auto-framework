"""
项目配置：域名、公共请求头等
实际项目中，敏感信息（如 X-Authorization）建议从环境变量读取
"""

# 抽奖接口基础域名
BASE_URL = "https://testapi.apifolo.com"

# 公共请求头，从浏览器抓包复制
COMMON_HEADERS = {
    "authority": "testapi.apifolo.com",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,vi-VN;q=0.6,vi;q=0.5",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Origin": "https://web-test.toofun.live",
    "Pragma": "no-cache",
    "Referer": "https://web-test.toofun.live/",
    "Sec-Ch-Ua": '"Not/A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "X-Frompackage": "act-cricket-battle-v2@0.9.3",
    "X-Language": "zh",
    "X-Mac": "debug",
    "X-Requestsource": "h5",
}

# 需要登录态的 header，抓包时直接复制，后续可改为从登录接口获取
AUTH_HEADERS = {
    "X-Authorization": "4b01d9362ea8135e0ecb861f68348afd5d091aa8",
    "X-Uid": "3959987",
}

# 抽奖成功用例的请求体（从浏览器 DevTools 的 Payload 标签页复制）
# 注意：当前静态 token 可能过期，导致调接口返回 invalid prize pool
# 若本地跑 test_draw_success 被 skip，说明需要刷新 X-Authorization
DRAW_PAYLOAD = {
    "id": 19,
    "drawCount": 1,
    "isMerge": True,
}

