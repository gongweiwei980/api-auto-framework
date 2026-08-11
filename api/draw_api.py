"""
抽奖接口封装层
把 HTTP 请求细节藏起来，测试用例只关心业务断言
"""
import requests
from config.config import BASE_URL, COMMON_HEADERS, AUTH_HEADERS


class DrawAPI:
    """H5 抽奖活动接口封装"""

    def __init__(self):
        self.base_url = BASE_URL
        # 合并公共 header 和登录态 header
        self.headers = {**COMMON_HEADERS, **AUTH_HEADERS}

    def draw(self, payload=None):
        """
        调用抽奖接口：POST /api/web/draw/sys/draw
        :param payload: 请求体 dict；不传默认空 JSON
        :return: requests.Response 对象
        """
        url = f"{self.base_url}/api/web/draw/sys/draw"
        body = payload if payload is not None else {}
        return requests.post(url, headers=self.headers, json=body, timeout=10)

    def draw_without_auth(self, payload=None):
        """
        不带登录态调用抽奖接口，用于验证未登录拦截
        """
        url = f"{self.base_url}/api/web/draw/sys/draw"
        body = payload or {}
        return requests.post(url, headers=COMMON_HEADERS, json=body, timeout=10)
