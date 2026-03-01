#!/usr/bin/env python3
"""
ServerPulse Agent - 服务器监控代理
安装在被监控的服务器上，定时上报数据
"""
import psutil
import time
import json
import requests
import socket
import platform

SERVER_NAME = socket.gethostname()
REPORT_INTERVAL = 10  # seconds

def get_metrics():
    """获取服务器指标"""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    load = psutil.getloadavg() if hasattr(psutil, 'getloadavg') else (0, 0, 0)
    
    # Top processes
    processes = []
    for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
        try:
            p = proc.info
            if p['cpu_percent'] and p['cpu_percent'] > 0:
                processes.append({
                    'name': p['name'],
                    'cpu': round(p['cpu_percent'], 1),
                    'memory': round(p['memory_percent'], 1)
                })
        except:
            pass
    
    processes.sort(key=lambda x: x['cpu'], reverse=True)
    
    return {
        'server': SERVER_NAME,
        'timestamp': time.time(),
        'cpu': cpu,
        'memory_percent': memory.percent,
        'memory_used': memory.used / (1024**3),  # GB
        'memory_total': memory.total / (1024**3),  # GB
        'disk_percent': disk.percent,
        'disk_used': disk.used / (1024**3),  # GB
        'disk_total': disk.total / (1024**3),  # GB
        'load': load,
        'network': get_network(),
        'top_processes': processes[:5]
    }

def get_network():
    """获取网络IO"""
    net = psutil.net_io_counters()
    return {
        'bytes_sent': net.bytes_sent,
        'bytes_recv': net.bytes_recv,
        'packets_sent': net.packets_sent,
        'packets_recv': net.packets_recv
    }

def main():
    print(f"🚀 ServerPulse Agent 启动")
    print(f"🖥️ 服务器: {SERVER_NAME}")
    print(f"📡 平台: {platform.system()} {platform.version()}")
    print(f"⏰ 上报间隔: {REPORT_INTERVAL}秒")
    print("-" * 40)
    
    while True:
        try:
            metrics = get_metrics()
            print(f"📊 CPU: {metrics['cpu']}% | 内存: {metrics['memory_percent']}% | 磁盘: {metrics['disk_percent']}%")
            
            # 本地存储
            with open('server_metrics.json', 'w') as f:
                json.dump(metrics, f, indent=2)
                
        except Exception as e:
            print(f"❌ 错误: {e}")
        
        time.sleep(REPORT_INTERVAL)

if __name__ == "__main__":
    main()
