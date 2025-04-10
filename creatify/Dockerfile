# 使用 Python 3.10.12 官方镜像
FROM python:3.10.12-slim

# 设置 python 环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pip.conf /root/.pip/pip.conf

# 容器内创建 myproject 文件夹
ENV APP_HOME=/var/www/html/creatify
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# 将当前目录加入到工作目录中（. 表示当前目录）
ADD . $APP_HOME

RUN /usr/local/bin/python -m pip install --upgrade pip

# 安装项目依赖
RUN pip install -r requirements.txt

# 给start.sh可执行权限
RUN chmod +x ./start.sh

# 数据迁移，并启动服务
ENTRYPOINT /bin/bash ./start.sh