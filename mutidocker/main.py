import requests

def main():
    # 从数据读取服务获取数据
    response = requests.get('http://localhost:5001/data')
    data = response.json()
    
    # 发送到计算服务进行处理
    response = requests.post('http://localhost:5002/calculate', json=data)
    results = response.json()
    
    # 发送到输出服务保存结果
    response = requests.post('http://localhost:5003/save', json=results)
    print(response.json()['message'])

if __name__ == '__main__':
    main() 