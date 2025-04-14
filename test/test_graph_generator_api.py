#!/usr/bin/env python3
"""
测试 graph_generator API 的脚本
用法: python test_graph_generator_api.py
# 指定不同的主机
python test_graph_generator_api.py --host 192.168.1.100

# 指定不同的端口
python test_graph_generator_api.py --port 9000

# 测试 Mermaid 格式
python test_graph_generator_api.py --format mermaid
"""

import requests
import json
import base64
import os
import argparse
from datetime import datetime

def test_generate_api(host="localhost", port=8081, format_type="graphviz"):
    """测试 /generate API 端点"""
    
    url = f"http://{host}:{port}/api/generate"
    
    # 测试数据
    test_descriptions = [
        "一个简单的流程图，包含三个节点：开始、处理、结束。开始连接到处理，处理连接到结束。",
        "一个组织结构图，CEO 下面有 CTO、CFO 和 COO 三个职位。",
        "一个状态机图，包含三个状态：空闲、工作中、完成。从空闲到工作中的转换条件是'开始'，从工作中到完成的转换条件是'结束'。"
    ]
    
    print(f"\n{'='*50}")
    print(f"开始测试 graph_generator API: {url}")
    print(f"{'='*50}")
    
    success_count = 0
    
    for i, description in enumerate(test_descriptions):
        print(f"\n测试 #{i+1}: {description[:50]}...")
        
        payload = {
            "text": description,
            "format": format_type
        }
        
        try:
            response = requests.post(url, json=payload, timeout=30)
            
            # 检查响应状态码
            if response.status_code == 200:
                result = response.json()
                
                if result.get("success") == True:
                    # 提取并保存图像（如果存在）
                    if "image_data" in result:
                        image_data = result["image_data"]
                        if image_data.startswith("data:"):
                            # 从 data URI 中提取 base64 编码的图像数据
                            image_data = image_data.split(",")[1]
                        
                        # 创建输出目录
                        os.makedirs("test_output", exist_ok=True)
                        
                        # 保存图像
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        filename = f"test_output/graph_{i+1}_{timestamp}.svg"
                        with open(filename, "wb") as f:
                            f.write(base64.b64decode(image_data))
                        
                        print(f"✅ 测试成功! 图像已保存到: {filename}")
                        print(f"   代码: {result.get('code', '')[:100]}...")
                    else:
                        print(f"✅ 测试成功! 但没有返回图像数据")
                    
                    success_count += 1
                else:
                    print(f"❌ API 返回错误: {result.get('error', '未知错误')}")
            else:
                print(f"❌ HTTP 错误: {response.status_code}")
                print(f"   响应: {response.text[:200]}")
        
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
    
    print(f"\n{'='*50}")
    print(f"测试完成: {success_count}/{len(test_descriptions)} 成功")
    print(f"{'='*50}")
    
    return success_count == len(test_descriptions)

def main():
    parser = argparse.ArgumentParser(description="测试 graph_generator API")
    parser.add_argument("--host", default="localhost", help="API 主机名 (默认: localhost)")
    parser.add_argument("--port", type=int, default=8081, help="API 端口 (默认: 8081)")
    parser.add_argument("--format", default="graphviz", choices=["graphviz", "mermaid"], 
                        help="图表格式 (默认: graphviz)")
    
    args = parser.parse_args()
    
    success = test_generate_api(args.host, args.port, args.format)
    
    if success:
        print("\n🎉 所有测试都成功通过!")
    else:
        print("\n⚠️ 部分测试失败，请检查日志获取详细信息。")

if __name__ == "__main__":
    main()