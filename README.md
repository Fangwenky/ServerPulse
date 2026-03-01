# 💻 ServerPulse - 服务器监控面板

> 轻量级服务器监控解决方案

## 🌟 功能

- 🖥️ **实时监控** - CPU、内存、磁盘、网络
- 📈 **历史趋势** - 了解资源使用变化
- 🔥 **进程监控** - 查看占用资源最多的进程
- 🌐 **远程监控** - 通过 Agent 监控多台服务器

## 🏗️ 架构

```
┌─────────────────┐     ┌─────────────────┐
│  ServerPulse    │────▶│   Dashboard     │
│    Agent        │     │   (Web界面)     │
│  (数据采集)      │     │   (展示)        │
└─────────────────┘     └─────────────────┘
```

## 🚀 快速开始

### 方式一：本地监控（推荐）

```bash
# 安装依赖
pip install psutil streamlit

# 启动面板
streamlit run dashboard.py
```

然后打开 http://localhost:8501

### 方式二：监控远程服务器

在远程服务器上安装 Agent：

```bash
# 安装依赖
pip install psutil

# 启动 Agent
python agent.py
```

Agent 会每10秒采集数据并保存到 `server_metrics.json`

## 📦 文件说明

| 文件 | 说明 |
|------|------|
| `dashboard.py` | Streamlit 监控面板 |
| `agent.py` | 数据采集代理 |
| `index.html` | 纯前端演示版 |

## 🔧 技术栈

- Python 3
- psutil - 系统信息采集
- Streamlit - Web 界面

## 📝 要求

- Python 3.8+
- psutil
- streamlit (仅面板)

---

💻 Made with ❤️
