"""
H5 抽奖接口测试用例
针对 /api/web/draw/sys/draw 的 POST 请求
通过实际调接口，验证参数校验、返回结构和错误码
"""
import pytest
from api.draw_api import DrawAPI
from config.config import DRAW_PAYLOAD
import yaml

def load_cases():
    with open("config/draw_case.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("case", load_cases())
def test_draw_params(draw_api, case):
    resp = draw_api.draw(payload=case["payload"])
    data = resp.json()
    assert data["code"] == case["expected_code"]
    assert case["expected_msg"] in data["msg"]

def test_draw_response_structure(draw_api):
    """
    验证抽奖接口返回结构合法：有 code/msg/res 字段
    """
    resp = draw_api.draw()
    data = resp.json()

    assert resp.status_code == 200
    assert "code" in data
    assert "msg" in data
    assert "res" in data

def test_draw_missing_id(draw_api):
    """
    参数校验：请求体为空，缺少 id 字段
    预期返回 code=1，提示 'Id Can not be empty'
    """
    resp = draw_api.draw(payload={})
    data = resp.json()

    assert resp.status_code == 200
    assert data["code"] == 1
    assert "Id Can not be empty" in data["msg"]

def test_draw_missing_draw_count(draw_api):
    """
    参数校验：只传 id，缺少 drawCount 字段
    预期返回 code=1，提示 'DrawCount Can not be empty'
    """
    resp = draw_api.draw(payload={"id": 224})
    data = resp.json()

    assert resp.status_code == 200
    assert data["code"] == 1
    assert "DrawCount Can not be empty" in data["msg"]

def test_draw_invalid_prize_pool(draw_api):
    """
    业务校验：参数完整，但当前环境奖品池无效
    预期返回 code=2，提示 'invalid prize pool'
    注：若活动时间/奖品池配置变化，此用例断言需同步调整
    """
    resp = draw_api.draw(payload={"id": 224, "drawCount": 1})
    data = resp.json()

    assert resp.status_code == 200
    assert data["code"] == 2
    assert "invalid prize pool" in data["msg"]

def test_draw_success(draw_api):
    """
    抽奖成功（happy path）：code=0 且返回中奖信息
    成功响应示例：
    {
      "code": 0, "nowUnix": 1786076608, "msg": "",
      "res": {"prizeInfos": [{"prizeId": 2472, "itemType": 12, ...}]}
    }
    """
    resp = draw_api.draw(payload=DRAW_PAYLOAD)
    data = resp.json()

    # 成功时的结构断言
    assert resp.status_code == 200
    assert data["code"] == 0
    assert data["msg"] == ""
    assert "res" in data
    assert "prizeInfos" in data["res"]
    assert isinstance(data["res"]["prizeInfos"], list)
    assert len(data["res"]["prizeInfos"]) > 0

    # 校验奖品信息字段完整
    prize = data["res"]["prizeInfos"][0]
    assert "prizeId" in prize
    assert "itemType" in prize
    assert "itemCount" in prize
    assert "content" in prize


def test_draw_without_auth():
    """
    未携带登录态调用抽奖接口，应被拦截
    实际状态可能是 401/403，或 code != 0 的错误响应
    """
    api = DrawAPI()
    resp = api.draw_without_auth()

    # 服务层可能直接 401，也可能 200 但返回业务错误码
    assert resp.status_code in [200, 401, 403]
    if resp.status_code == 200:
        assert resp.json()["code"] != 0
