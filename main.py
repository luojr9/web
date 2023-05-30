from bottle import get, post, run, request, template

import subprocess

#### 这个是 客户端请求 服务端就发给一个 index.html 控制界面给客户端
@get("/")
def index():
    return template("index")


@post("/cmd")
def cmd():
    adss = request.body.read().decode()  #### 接收到 客户端 发过来的数据
    print("### Do cmd:" + adss)
    ret, val = subprocess.getstatusoutput(adss)  # 0表示指令成功执行，1表示失败，256表示没有返回结果
    print('ret=%d' %ret)
    print('val=' + val)
    i = val.find('OnOff: TRUE')
    if i > -1:
        print('OnOff: TRUE')
        return 'on'
    else:
        i = val.find('OnOff: FALSE')
        if i > -1:
            print('OnOff: FALSE')
            return 'off'
    return "OK"


run(host='0.0.0.0', port=8088, debug=True)  #### 开启服务端
