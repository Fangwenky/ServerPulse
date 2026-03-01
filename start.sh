#!/bin/bash
# ServerPulse 启动脚本

echo "💻 ServerPulse 服务器监控面板"
echo "=============================="

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 请先安装 Python 3"
    exit 1
fi

# 安装依赖
echo "📦 安装依赖..."
pip install -r requirements.txt

# 启动
echo "🚀 启动面板..."
echo "访问地址: http://localhost:8080"
echo ""

streamlit run dashboard.py --server.port 8080 --server.address 0.0.0.0
