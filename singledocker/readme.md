### 使用以下命令构建 Docker 镜像：
```bash
docker build -t grade-analysis
```
### 运行容器

Linux/Mac
```bash
docker run -v $(pwd):/app grade-analysis
```


结果 result.csv 应当会生成到当前目录下