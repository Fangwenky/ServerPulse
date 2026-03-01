# 💻 ServerPulse - 服务器监控面板

> 一键部署，远程监控你的服务器

## 🎯 目标

在服务器上部署 ServerPulse，通过任意设备远程监控服务器状态。

## 📦 文件说明

| 文件 | 说明 |
|------|------|
| `dashboard.py` | Streamlit 监控面板（需要安装） |
| `agent.py` | 数据采集 Agent |
| `requirements.txt` | Python 依赖 |

## 🚀 快速部署

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动面板

```bash
streamlit run dashboard.py --server.port 8080 --server.address 0.0.0.0
```

### 3. 远程访问

- **局域网**: http://[服务器IP]:8080
- **Tailscale**: http://[Tailscale IP]:8080
- **公网**: 需要配置端口转发或 VPN

## 📱 远程访问设置

### 方案1: Tailscale（推荐）

1. 服务器安装 Tailscale
2. 获取 Tailscale IP（如 100.105.184.113）
3. 从任意设备访问 http://100.105.184.113:8080

### 方案2: 端口映射

路由器上映射端口 8080 → 服务器 IP

## 📊 功能

- 🖥️ CPU 使用率（实时）
- 💾 内存使用情况
- 💿 磁盘使用情况
- 📊 系统负载
- 📡 网络流量
- 🔥 Top 5 进程
- 🔧 系统信息
- ⏰ 自动刷新

## 🛠️ 技术栈

- Python 3.8+
- psutil - 系统信息采集
- Streamlit - Web 界面

## ⚠️ 注意

- 需要服务器有 Python 环境
- 需要稳定的网络连接
- 建议配合 Tailscale 或 VPN 使用

---

💻 Made with ❤️
