from bottle import get, post, run, request, template

import os

@get("/")
def index():
    return template("index")


#### 这个是 客户端请求 服务端就发给一个 index.html 控制界面给客户端
@post("/cmd")
def cmd():
    adss = request.body.read().decode()  #### 接收到 客户端 发过来的数据
    print("### Do cmd:" + adss)
    os.system(adss)
    return "OK"


run(host='0.0.0.0', port=8088, debug=True)  #### 开启服务端
