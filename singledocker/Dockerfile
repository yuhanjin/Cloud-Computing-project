# 使用 Python 3.10 作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制程序文件和数据文件
COPY analysis.py .
COPY Grade\ Table.csv .

# 运行程序
CMD ["python", "analysis.py"]