这是一个django后端测试项目，使用django djangorestframework djangorestframework-simplejwt，使用sqlite。

## 目前支持的接口如下：
http://127.0.0.1:8000/signup

http://127.0.0.1:8000/signin

http://127.0.0.1:8000/me

## 项目运行
### 1. 克隆项目到服务器中
git clone https://github.com/HZ514/CreatifyBackendAssess.git

### 2. 切换至目录中
cd CreatifyBackendAssess

### 3. 构建镜像
docker-compose build

### 4. 运行 docker-compose
docker-compose up -d

### 5. 查看运行的状态
docker-compose ps

### 待完善
#### 1、将自定义的异常类和错误码在视图和中间件中使用起来，得到更友好的错误描述。
#### 2、接口增加完善的校验以及异常日志记录。
#### 3、单元测试


##测试
curl --location http://127.0.0.1:8000/signup/ --data-raw '{"email": "test@test.com", "password": "123"}'

curl --location http://127.0.0.1:8000/signin/ --data-raw '{"email": "test@test.com", "password": "123"}'

curl --location http://127.0.0.1:8000/me/ --header 'Authorization: Bearer <access_token>'