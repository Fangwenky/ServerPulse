#!/usr/bin/env python3
"""
ServerPulse Dashboard - 服务器监控面板
"""
import streamlit as st
import psutil
import json
import os
import time
from datetime import datetime

st.set_page_config(page_title="💻 ServerPulse", page_icon="💻", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0f172a; }
    .title { font-size: 2.5rem; background: linear-gradient(135deg, #22c55e, #16a34a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .card { background: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #334155; }
    .ok { color: #22c55e; }
    .warning { color: #f59e0b; }
    .error { color: #ef4444; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">💻 ServerPulse</p>', unsafe_allow_html=True)
st.markdown(f"### 🖥️ {psutil.os.uname().nodename} | 最后更新: {datetime.now().strftime('%H:%M:%S')}")

# Auto refresh
if st.button("🔄 刷新"):
    st.rerun()

st.markdown("---")

# Get real data
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')
load = psutil.getloadavg() if hasattr(psutil, 'getloadavg') else (0, 0, 0)
net = psutil.net_io_counters()

# Status Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    color = 'error' if cpu > 80 else 'warning' if cpu > 50 else 'ok'
    st.metric("🖥️ CPU", f"{cpu}%", delta_color=color)
with c2:
    color = 'error' if memory.percent > 80 else 'warning' if memory.percent > 50 else 'ok'
    st.metric("💾 内存", f"{memory.percent}%", delta_color=color)
with c3:
    color = 'error' if disk.percent > 90 else 'warning' if disk.percent > 70 else 'ok'
    st.metric("💿 磁盘", f"{disk.percent}%", delta_color=color)
with c4:
    st.metric("📊 负载", f"{load[0]:.2f}")

# Details
c1, c2 = st.columns(2)

with c1:
    st.markdown("### 💾 内存详情")
    st.write(f"已用: {memory.used / (1024**3):.1f} GB / {memory.total / (1024**3):.1f} GB")
    st.progress(memory.percent / 100)
    
    st.markdown("### 💿 磁盘详情")
    st.write(f"已用: {disk.used / (1024**3):.1f} GB / {disk.total / (1024**3):.1f} GB")
    st.progress(disk.percent / 100)

with c2:
    st.markdown("### 📡 网络")
    st.write(f"发送: {net.bytes_sent / (1024**2):.1f} MB")
    st.write(f"接收: {net.bytes_recv / (1024**2):.1f} MB")
    st.write(f"数据包: {net.packets_sent} / {net.packets_recv}")
    
    st.markdown("### 🔧 系统")
    st.write(f"平台: {platform.system()} {platform.release()}")
    st.write(f"CPU 核心: {psutil.cpu_count()}")
    st.write(f"启动时间: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M')}")

# Top Processes
st.markdown("---")
st.markdown("### 🔥 Top 5 进程")

processes = []
for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent', 'status']):
    try:
        p = proc.info
        if p['cpu_percent'] and p['cpu_percent'] > 0:
            processes.append(p)
    except:
        pass

processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)

for i, p in enumerate(processes[:5], 1):
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        st.write(f"{i}. {p['name']}")
    with col2:
        st.write(f"CPU: {p['cpu_percent']:.1f}%")
    with col3:
        st.write(f"内存: {p['memory_percent']:.1f}%")

# Auto refresh
import subprocess
st.markdown("---")
st.caption("💻 ServerPulse | 每5秒自动刷新")
