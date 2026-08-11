import pytest 
import requests 
import yaml 
from api.draw_api import DrawAPI
@pytest.fixture(scope="session") 
def session(): # 创建Session对象，自动管理Cookie 
    s = requests.Session() 
    s.headers.update({ "Content-Type": "application/json", "User-Agent": "api-auto-test/1.0" }) 
    yield s 
    s.close() 
@pytest.fixture(scope="session") 
def base_url(): # 从配置文件读取环境地址 
    with open("config/dev.yaml", "r", encoding="utf-8") as f: config = yaml.safe_load(f) 
    return config["base_url"] 
@pytest.fixture(scope="session") 
def auth_token(session, base_url): # 登录获取token，其他用例复用 
    resp = session.post(f"{base_url}/api/login", json={ "username": "testuser", "password": "testpass" }) 
    return resp.json()["token"]

@pytest.fixture
def draw_api():
    """每个用例都拿到一个 DrawAPI 实例"""
    return DrawAPI()