这是一个django后端测试项目，使用django djangorestframework djangorestframework-simplejwt。

## 目前支持的接口如下：
http://127.0.0.1:8000/signup

http://127.0.0.1:8000/signin

http://127.0.0.1:8000/me

# 项目运行
## 1. 克隆项目到服务器中
$ git clone https://github.com/HZ514/CreatifyBackendAssess.git

## 2. 切换至目录中
$ cd CreatifyBackendAssess

## 3. 运行 docker-compose
docker-compose up -d

## 4. 查看运行的状态
docker-compose ps


测试
curl --location http://127.0.0.1:8555/signup/ --data-raw '{"email": "test@test.com", "password": "123"}'

curl --location http://127.0.0.1:8555/signin/ --data-raw '{"email": "test@test.com", "password": "123"}'

curl --location http://127.0.0.1:8555/me/ --header 'Authorization: Bearer <access_token>'