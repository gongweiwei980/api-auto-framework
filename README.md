# api-auto-framework 🧪

[![pytest](https://img.shields.io/badge/pytest-9.1.1-blue)](#)
[![Python](https://img.shields.io/badge/Python-3.13.5-green)](#)
[![Report](https://img.shields.io/badge/report-pytest--html-orange)](#)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](#)

> 基于 pytest + 请求 + 数据驱动的 H5 抽奖活动接口自动化测试框架  
> 3 天从零落地：用例数从 6 → 14 全覆盖，随 GitHub push 触发 CI 自动化回归

---

## 🚀 kaui快速开始（别在没装依赖时跑）

```bash
#= 1.创建虚拟机
python -m venv venv

# 2.激活（Windows PowerShell）
venv\Scripts\activate

# 3.装依赖，一键还原
pip install -r requirements.txt

# 4.跑----啥都不用带，pytest.ini 自动拼 --html
pytest
```

> 跑完根目录出 `report.html`——**self-contained，人传人打开**。

---

## 📂 项目结构（三层架构）

```
api-auto-framework/
├── config/                  ← 配置层（token / 基础 URL / 统一头）
├── api/                     ← 接口封装层（统一 _make_request 模板）
├── testcases/               ← 用例层（parameterize + YAML 驱动）
├── conftest.py              ← 公共fixture（header 复用）
├── pytest.ini               ← pytest 默认带 --html
├── requirements.txt         ← 22 个依赖清单
└── report.html              ← 🚫 不进 git（.gitignore 已栏）
```

---

## 📊 用例设计（数据驱动 + 参数化）

**接口**：`POST /api/web/draw/sys/draw`（H5 抽奖）  
**覆盖场景**：

```
  ┌─ 结构验证：code / msg / res 字段存在性 → 6 条
  ├─ 成功抽奖：drawCount 1~3 次 + isMerge true/false → 4 条
  ├─ 参数缺失：无id / 无drawCount → 2 条
  ├─ 未登录：token 清空 → 1 条
  └─ 业务异常：奖品无效 / 抽奖次数非法 → 1 条
  --------------------------------------------------
  总计 14 条（YAML id_driven → pytest.mark.parametrize 展开）
```

---

## ✅ 测试报告

`pytest.ini` 写死了 `--html=report.html --self-contained-html`，  
以后 `pytest` 三个字自动出一份：

- 左侧 Passed / Failed 绿红对比
- 每用例耗时毫秒级
- stdout 内嵌（请求/响应全留痕）

---

## 🔄 数据驱动（为什么做到这一步）

1. **YAML 数据模板**分成功/参数缺失/异常三类（`config/test_data_*.yaml`），**加用例不用改代码**
2. `pytest.mark.parametrize("payload,expected_code,expected_key,...", yaml_list)`
   → 用例自动展开，yaml 里加一行数据 → 多一条用例

---

## 🛠 技术栈

| 层 | 工具 | 为什么选 |
|---|---|---|
| 测试框架 | pytest 9.1.1 | 生态最大，conftest / fixture / parametrize 三位一体 |
| HTTP 客户端 | requests 2.34.2 | 中文文档最多，扫一眼就上手 |
| 数据驱动 | PyYAML 6.0.3 | 非程序员也能看到 yaml 就改用例 |
| 报告 | pytest-html 4.2.0 | pip 直装，0 网络坑 → 一分钟落地 |
| 版本管理 | Git + GitHub + SSH | push 指到 GitHub Actions 自动触发 CI |

---

## 🧠 踩坑记录（国内环境专属）

| 坑 | 表现 | 解法 |
|---|---|---|
| Scoop 装 Allure | `Empty reply from server`（GitHub 连不上） | 切 pytest-html，零网络 |
| GitHub 软封老号 | crypto 二字触发的病毒式封禁 | 换干净新号 + SSH 钥匙，秒解 |
| GCM (Git Credential Manager) 弹窗卡死 | HTTPS + OAuth 本地端口监听失败 | 改成 SSH 路线，完全绕过 |
| requirements.txt 逐条补 | 之前只加 `pytest-html` 一行 | `pip freeze >` 全量拉一次 |

---

## 🔜 下一步

- [x] 14 条全绿，pytest.ini 自动化，git push 通道打通
- [ ] GitHub Actions CI：push 触发部署 + download artifact
- [ ] conftest 加 loguru 日志，每用例留痕
- [ ] 邮件 / 钉钉报告推送

---

## 📄 License

MIT — 这个框架是你简历的一块砖，随便拿去用。
