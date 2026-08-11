# api-auto-framework

基于 pytest + requests 的接口自动化测试框架，用于 H5 抽奖等活动接口的自动化验证。

## 环境准备

```bash
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活虚拟环境（Windows PowerShell）
venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt
```

## 项目结构

```
api-auto-framework/
├── api/                  # 接口封装层
│   └── draw_api.py       # 抽奖接口封装
├── config/               # 配置文件
│   └── config.py         # 域名、公共 header、登录态
├── testcases/            # 测试用例
│   └── test_lottery_draw.py
├── conftest.py           # pytest fixture（预留）
├── pytest.ini            # pytest 配置
├── requirements.txt      # 依赖清单
└── README.md
```

## 运行测试

```bash
# 跑全部用例
pytest

# 跑指定文件，显示详细输出
pytest testcases/test_lottery_draw.py -v

# 跑指定用例
pytest testcases/test_lottery_draw.py::test_draw_missing_id -v
```

## 当前测试内容

针对 `POST /api/web/draw/sys/draw` 接口：

- 验证返回结构（code/msg/res）
- 参数缺失校验：id 为空、drawCount 为空
- 业务异常校验：invalid prize pool
- 未登录场景校验

## 注意事项

1. `config/config.py` 中的 `X-Authorization` 和 `X-Uid` 来自浏览器抓包，token 过期后需要更新。
2. 测试环境的业务状态会变化，断言需要根据实际情况调整。
3. `venv/` 和 `__pycache__/` 已加入 `.gitignore`，不会提交到 Git。
